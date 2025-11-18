"""This program contains functions for an adventure game.

There are four functions currently in here, those being purchase_item, new_random_monster,
print_wellcome, and print_shop_menu. This program currently just contains these functions,
as well as a few examples of them being used."""

import json
import os
import pygame
import random

#game functions assignment CSCI 150

def display_map(player):
    pygame.init()

    CELL = 32
    GRID = 10
    W = CELL * GRID
    H = CELL * GRID

    screen = pygame.display.set_mode((320, 320))
    clock = pygame.time.Clock()

    px, py = player["stats"]["location"]
    town = [0, 0]
    monster = [5, 5]

    left_town_once = False
    left_monster_once = False
    running = True

    while running:
        screen.fill((255, 255, 255))

        for x in range(GRID):
            for y in range(GRID):
                rect = pygame.Rect(x * CELL, y * CELL, CELL, CELL)
                pygame.draw.rect(screen, (200, 200, 200), rect, 1)

        tx, ty = town
        pygame.draw.circle(screen, (0, 180, 0), (tx * CELL + CELL//2, ty * CELL + CELL//2), CELL//3)

        mx, my = monster
        pygame.draw.circle(screen, (200, 0, 0), (mx * CELL + CELL//2, my * CELL + CELL//2), CELL//3)

        pygame.draw.rect(screen, (50, 100, 255), pygame.Rect(px * CELL, py * CELL, CELL, CELL))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    px = max(0, px - 1)
                elif event.key == pygame.K_RIGHT:
                    px = min(GRID - 1, px + 1)
                elif event.key == pygame.K_UP:
                    py = max(0, py - 1)
                elif event.key == pygame.K_DOWN:
                    py = min(GRID - 1, py + 1)

        if [px, py] != town:
            left_town_once = True
        if [px, py] != monster:
            left_monster_once = True

        if [px, py] == monster and left_monster_once:
            player["stats"]["location"] = monster
            running = False
            pygame.quit()
            fight(player)

        if [px, py] == town and left_town_once:
            player["stats"]["location"] = town
            running = False
            pygame.quit()
            town_menu(player)

        clock.tick(60)

#load save function

def load_save():
    """gives the player the choice to load previous saves"""

    game_saves = []
    for item in os.listdir():
        if item.endswith(".json"):
            game_saves.append(item)

    if game_saves:
        choice = input("Load a save? (yes or no)\n")

        if choice == "yes":
            print(game_saves)
            while True:
                save_choice = input("Which save?\n")
                file_name = save_choice + ".json"
                if file_name in game_saves:
                    with open(file_name, "r") as f:
                        player = json.load(f)
                        print(f"loaded {file_name}")
                    return player
                else:
                    print("Save not found")
        elif choice == "no":
            print("You started a new game")
            return
        else:
            print("INVALID INPUT")
    else:
        print("No saves found.\n")

def save(player):
    """Lets player save thier progress as a game save"""

    save_name = input("Name of your save?:\n")
    if not save_name.endswith(".json"):
        save_name += ".json"

    with open(save_name, "w") as f:
        json.dump(player, f)
    print(f"Game saved as {save_name}")

#town greeting function

def town_menu(player):
    """Displays the options that the player has in town"""

    print("Your current items:")
    print([(item["name"], item["durab"]) for item in player["inventory"]])
    print(f"""
Your health: {player["stats"]["hp"]}
Your gold: {player["stats"]["gold"]}

You're in town, what do you want to do? Your actions are:
fight (fight monster), shop (item shop), sleep (restore 50hp for 10 gold), save, or quit game.""")
        
    action = input("")
    return action

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

    print(f"You leave the town and enter the woods, in the woods\n{monster["description"]}\n")

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
                return player
            
            player["stats"]["hp"] -= monster["power"]

            if player["stats"]["hp"] <= 0:
                print("You died!\n")
                return player

        elif action == "leave":
            display_map(player)
        
        else:
            print("Invalid input, please re-enter action.\n")

#random monster generator

def new_random_monster():
    """ 
    Generates a new random monster with a name, description and stats.
    Returns monster_choice, description, health, power, money.
    """
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
        purchase = input("What would you like to buy? or do you want to leave?\n")

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
