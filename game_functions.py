"""This program contains functions for an adventure game.There are many functions currently
in here, some of those being purchase_item, new_random_monster, print_wellcome, 
and print_shop_menu."""

import json
import os
import pygame
import random

#game functions assignment CSCI 150

def display_map(player):
    pygame.init()

    CELL = 32
    GRID = 10

    screen = pygame.display.set_mode((CELL * 10, CELL * 10))
    clock = pygame.time.Clock()

    px, py = player["stats"]["location"]
    town_location = [0, 0]
    monster_location = [6, 4]

    left_town_once = False
    left_monster_once = False

    while True:
        screen.fill((255, 255, 255))

        for x in range(GRID):
            for y in range(GRID):
                rect = pygame.Rect(x * CELL, y * CELL, CELL, CELL)
                pygame.draw.rect(screen, (200, 200, 200), rect, 1)

        tx, ty = town_location
        pygame.draw.circle(screen, (0, 180, 0), (tx * CELL + CELL//2, ty * CELL + CELL//2), CELL//3)
        mx, my = monster_location
        pygame.draw.circle(screen, (200, 0, 0), (mx * CELL + CELL//2, my * CELL + CELL//2), CELL//3)

        pygame.draw.rect(screen, (50, 100, 255), pygame.Rect(px * CELL, py * CELL, CELL, CELL))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return None

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    px = max(0, px - 1)
                if event.key == pygame.K_RIGHT:
                    px = min(GRID - 1, px + 1)
                if event.key == pygame.K_UP:
                    py = max(0, py - 1)
                if event.key == pygame.K_DOWN:
                    py = min(GRID - 1, py + 1)

        player["stats"]["location"] = px, py

        if [px, py] != town_location:
            left_town_once = True
        if [px, py] != monster_location:
            left_monster_once = True

        if [px, py] == monster_location and left_monster_once:
            pygame.quit()
            return player

        if [px, py] == town_location and left_town_once:
            pygame.quit()
            return player

        clock.tick(60)

#load save function

def load_save():
    """gives the player the ability to load previous saves"""

    game_saves = []
    for item in os.listdir():
        if item.endswith(".json"):
            game_saves.append(item)

    if game_saves:
        while True:
            choice = input("Load a save? (yes or no)\n")
            if choice == "yes":
                print(game_saves)
                while True:
                    save_choice = input("Which save?\n")
                    file_name = save_choice + ".json"
                    if file_name in game_saves:
                        with open(file_name, "r") as file:
                            player = json.load(file)
                            print(f"loaded {file_name}")
                        return player
                    else:
                        print("Save not found")
            elif choice == "no":
                print("You started a new game")
                player = {"stats": {"name": None, "hp": 100, "gold": 2000, "location": [0, 0], "life": True},
       "inventory": []}
                return player
            else:
                print("INVALID INPUT")
    else:
        print("No saves found.\n")

def save(player):
    """Lets player save thier progress as a game save"""

    save_name = input("Name of your save?:\n")
    if not save_name.endswith(".json"):
        save_name += ".json"

    with open(save_name, "w") as file:
        json.dump(player, file)
    print(f"Game saved as {save_name}")

#town greeting function

def town_menu(player):
    """Displays the options that the player has in town"""
    
    print("")
    print("Your current items:")
    print([(item["name"], item["durab"]) for item in player["inventory"]])
    print(f"""
Player: {player["stats"]["name"]}
Player health: {player["stats"]["hp"]}
Player gold: {player["stats"]["gold"]}

You're in town, what do you want to do? Your actions are:
map (find and fight monster), shop (item shop), casino (go to the casino),
sleep (restore 50hp for 10 gold), save, or quit game.""")
        
    action = input("")
    return action

#casino function

def casino(player):
    """Lets the player try to gain gold through an dice interactive game"""

    print("""---You go to the casino---
You see 3 humanoid figures rolling dice, they offer to let you join in,
do you accept? (yes or no)\n""")
    
    dice1 = ["Fairy", "Witch", "Siren", "Goul", "Dragon", "Kraken"]
    dice2 = ["Sword", "Dagger", "Rock", "Crossbow", "Fists", "Jem of Fortune"]
    dice_power = {"Fairy": 1, "Witch": 2, "Siren": 3, "Goul": 4, "Dragon": 5, "Kraken": 6,
"Fists": 1, "Rock": 2, "Dagger": 3, "Sword": 4, "Crossbow": 5, "Jem of Fortune": 6}
    
    while True:
        casino_choice = input("")

        if casino_choice == "yes":
            print("""\nYou pick up the two monster dice, they explain
that you need to roll one at a time.\n""")
            
            input("Press any key to roll\n")

            roll1 = random.choice(dice1)
            roll2 = random.choice(dice2)

            print(f"""\nYou rolled the {roll1}!
This monster has a power level of {dice_power[roll1]}!\n""")

            while True:
                print(f"""You have {player["stats"]["gold"]} gold,
how much would you like to bet? Keep in mind that
a more powerful monster yeilds more reward.\n""")
                bet1 = int(input(""))
                if bet1 >= player["stats"]["gold"]:
                    print("You don't have that much gold!")
                else:
                    break
            
            bet2 = (bet1 * dice_power[roll1] // 6)
            print(f"""\nYou bet {bet1} gold, if you win you will gain {bet2} gold,
you now you can roll the second dice.\n""")
            input("Press any key to roll second dice\n")
            print(f"\nYou rolled the {roll2}!\n")

            if dice_power[roll2] > dice_power[roll1]:
                print(f"You won {bet2} gold!")
                player["stats"]["gold"] += bet2
            else:
                print("You lost! D:")
                player["stats"]["gold"] -= bet1

            print("\nDo you want to play again? (yes or no)\n")
            
        elif casino_choice == "no":
            print("---You leave the casino---")
            break

        else:
            print("Invalid input. Please re-enter choice")

#sleeping function

def sleep(player):
    """Lets the player sleep"""

    print("\nYou slept well for the night\n")

    player["stats"]["hp"] += 50
    player["stats"]["gold"] -= 10

#fighting function

def fight(player):
    """Lets the player fight a monster"""

    monster = new_random_monster()
    print(f"You leave town and enter the woods, in the woods\n{monster["description"]}\n")
    while True:

        print(f"""Your health: {player["stats"]["hp"]}. Your gold {player["stats"]["gold"]}
Monster health: {monster["hp"]}. Monster power: {monster["power"]}""")
        
        for item in player["inventory"]:
            if item["equipped"] == True:
                print(f"You currently have {item["name"]} equipped\n")
        
        action = input("What would you like to do? attack, equip (equip item), leave.\n")

        if action == "equip":
            for item in player["inventory"]:
                print(item["name"])

            equip = input("What do you want to equip?\n")
            for item in player["inventory"]:
                if equip == item["name"]:
                    print(f"You equipped {item["name"]}")
                    item["equipped"] = True
                else:
                    print("You do not have that item")

        elif action == "attack":
            damage = 10
            for item in player["inventory"]:
                if item["equipped"] == True:
                    damage = item["power"]
                    item["durab"] -= 1
                        
                    if item["durab"] <= 0:
                        player["inventory"].remove(item)

            monster["hp"] -= damage
            print(f"You attacked for {damage} damage!\n")
                      
            if monster["hp"] <= 0:
                print("you defteated the monster!\n")
                player["stats"]["gold"] += monster["gold"]
                display_map(player)
            
            player["stats"]["hp"] -= monster["power"]

            if player["stats"]["hp"] <= 0:
                print("You died!\n")
                return player

        elif action == "leave":
            display_map(player)
            return None
            
        
        else:
            print("Invalid input, please re-enter action.\n")

#random monster generator

def new_random_monster():
    """ Generates a new random monster with a name, description and stats.
    Returns monster_choice, description, health, power, money."""

    monster_list = ["A witch", "A fairy", "A goul"]
    monster_choice = random.choice(monster_list)

    if monster_choice == "A witch":
        description = """There is a witch sitting in a hollowed out tree in front of you,
you don't know what its intentions are yet."""

        health = random.randint(50, 100)
        power = random.randint(50, 90)
        money = random.randint(0, 100)

    elif monster_choice == "A fairy":
        description = """a small fairy hovers next to you, ethereal in it's presence,
you feel safe and warm, but don't get too close for you don't know its secrets."""

        health = random.randint(20, 100)
        power = random.randint(10, 90)
        money = random.randint(0, 20)

    elif monster_choice == "A goul":
        description = """a goul jumps at you from the shadows, draw your weapon quickly,
for gouls are known to be very viloent and difficult to reason with."""

        health = random.randint(100, 5000)
        power = random.randint(80, 90)
        money = random.randint(0, 200)
    
    return {"name": monster_choice, 
            "description": description, 
            "hp": health, 
            "power": power, 
            "gold": money}

#print_welcome function

def print_welcome(player, width):
    """Creates and prints a welcome greeting string with the given name and width specified."""

    if not player["stats"]["name"]:
        player["stats"]["name"] = input("Please input your name:\n")
    greeting = f"Hello, {player["stats"]["name"]}!"
    print(f"{greeting.center(width)}")

#print_shop_menu function

def print_shop_menu(player, shop):
    """Creates and prints a menu with the items names and prices as parameters."""

    print("You enter the local shop in town.\n")
    print("/" + "-" * 22 + "\\")
    for item in shop:
        print(f"| {item["name"]:<12}{item["cost"]:>3} gold |")
    print("\\" + "-" * 22 + "/")

    print([item["name"] for item in player["inventory"]])
    print(f"Your gold: {player["stats"]["gold"]}")

#purchase item function    

def purchase_item(player, shop):
    """Lets the player purchase an item from the shop. It takes the players
inventory and the shops items as parameters and returns the updated inventory and stats"""

    while True:
        print_shop_menu(player, shop)
        purchase = input("What would you like to buy? Or do you want to leave?\n")

        for item in player["inventory"]:
            if purchase == item["name"]:
                print("You already have that!")
    
        for item in shop:
            if purchase == item["name"]:
                if player["stats"]["gold"] >= item["cost"]:
                    player["inventory"].append(item)
                    player["stats"]["gold"] -= item["cost"]

                else:
                    print("\nYou don't have enough money for that!")
        
        if purchase == "leave":
            break

        else:
            print("\nInvalid input, please re-enter your action.")

#Testing functions - All code below this line is for testing purposes

def test_functions():
    display_map()

if __name__ == "__main__":
    test_functions()
