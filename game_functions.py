"""
This program contains functions for an adventure game.

There are four functions currently in here, those being purchase_item, new_random_monster,
print_wellcome, and print_shop_menu. This program currently just contains these functions,
as well as a few examples of them being used.
"""

#game functions assignment CSCI 150

#town greeting function

def town_menu(player, inventory):
    """Displays the options that the player has in town"""

    print("Your current items:")
    print([(item["name"], item["durab"]) for item in inventory])
    print(f"""
Your health: {player["hp"]}
Your gold: {player["gold"]}

You're in town, what do you want to do? Your actions are:
leave (fight monster), shop (item shop), sleep (restore 10hp for 10 gold), or quit game.""")
        
    action = input("")
    return action

#sleeping function

def sleep(player):
    """This function is called when players chooses the sleep action"""

    print("""
You slept well for the night
          """)

    player["hp"] += 50
    player["gold"] -= 10

#fighting function

def fight(player, inventory):
    """Lets the player fight a monster"""
    
    monster = new_random_monster()

    print(f"""
You leave the town and enter the woods, in the woods
{monster["description"]}
""")

    while True:

        print(f"""Your health: {player["hp"]}. Your gold {player["gold"]}
Monster health: {monster["hp"]}. Monster power: {monster["power"]}""")
        
        if "equipped" in player:
            print(f"You currently have {player["equipped"]["name"]} equipped\n")
        
        action = input("What would you like to do? attack, equip (equip item), run.\n")

        if action == "equip":
            print([item["name"] for item in inventory])
            equip = input("What do you want to equip?\n")
            for item in inventory:
                if equip == item["name"]:
                    print(f"You equipped {item["name"]}")
                    player["equipped"] = item
                else:
                    print("You do not have that item")

        elif action == "attack":
            if "equipped" in player:
                damage = player["equipped"]["power"]
                player["equipped"]["durab"] -= 1
                    
                if player["equipped"]["durab"] <= 0:
                    inventory.remove(player["equipped"])
                    # player["equipped"] = {"name": "nothing"}
                    
            else:
                damage = 10

            monster["hp"] -= damage
            print(f"You attacked for {damage} damage!\n")
                      
            if monster["hp"] <= 0:
                print("you defteated the monster!\n")

                player["gold"] += monster["gold"]

                return player
            
            player["hp"] -= monster["power"]

            if player["hp"] <= 0:

                print("You died!")

                return player

        elif action == "run":

            return player
        
        else:
            print("""Invalid input, please re-enter action.""")

#random monster generator

import random

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
        description = """A small fairy hovers next to you, ethereal in it's presence,
you feel safe and warm, but don't get too close for you don't know its secrets."""

        health = random.randint(20, 100)
        power = random.randint(10, 90)
        money = random.randint(0, 20)

    elif monster_choice == "A goul":
        description = """A goul jumps at you from the shadows, draw your weapon quickly,
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

    player["name"] = input("Please input your name:\n")
    greeting = f"Hello, {player["name"]}!"
    print(f"{greeting.center(width)}")

#print_shop_menu function

def print_shop_menu(player, inventory, shop):
    """Creates and prints a menu with the items names and prices as parameters."""

    print("You enter the local shop in town.\n")
    print("/" + "-" * 22 + "\\")
    print(f"| {shop[0]["name"]:<12}{shop[0]["cost"]:>3} gold |")
    print(f"| {shop[1]["name"]:<12}{shop[1]["cost"]:>3} gold |")
    print("\\" + "-" * 22 + "/")

    print([item["name"] for item in inventory])
    print(f"Your gold: {player["gold"]}")

#purchase item function    

def purchase_item(player, inventory, shop):
    """Lets the player purchase an item from the shop. It takes the players
inventory and the shops items as parameters and returns the updated inventory"""

    while True:
        print_shop_menu(player, inventory, shop)
        purchase = input("What would you like to buy? or do you want to leave?\n")

        if purchase == shop[0]["name"]:
            if player["gold"] >= shop[0]["cost"]:
                inventory.append(shop[0])
                player["gold"] -= shop[0]["cost"]

            else:
                print("""
You don't have enough money for that!""")
                
        elif purchase == shop[1]["name"]:
            if player["gold"] >= shop[1]["cost"]:
                inventory.append(shop[1])
                player["gold"] -= shop[1]["cost"]
                         
            else:
                print("""
You don't have enough money for that!""")
        
        elif purchase == "leave":
            break

        else:
            print("""
    Invalid input, please re-enter your action.""")



#Testing functions - All code below this line is for testing purposes

def test_functions():
    """Only it used when file is run directly, test_functions gives a few
examples of the functions above working."""

    #examples of purchase_item function

    items_bought, money_left = purchase_item(10, 126, 2)

    print(f"you bought {items_bought} items and have ${money_left} left.")

    #2

    items_bought, money_left = purchase_item(2000, 10, 2)

    print(f"you bought {items_bought} items and have ${money_left} left.")

    #3

    items_bought, money_left = purchase_item(2, 4859, 10000)

    print(f"you bought {items_bought} items and have ${money_left} left.")

    #examples of new_random_monster

    monster = new_random_monster()

    print(monster["name"])
    print(monster["health"])
    print(monster["power"])
    print("")

    #2

    monster = new_random_monster()

    print(monster["name"])
    print(monster["description"])
    print(monster["money"])
    print("")

    #3

    monster = new_random_monster()

    print(monster["name"])
    print(monster["description"])
    print(monster["power"])
    print(monster["health"])

    #Examples of print_welcome

    print_welcome("Elisha", 30)

    print_welcome("Bob", 20)

    print_welcome("Jeff", 24)

    #Examples of print_shop_menu

    print_shop_menu("Sword", 1354.34, "Armor", 32.34)

    print_shop_menu("Bagel", 5.76, "Cheese", 3.45)

    print_shop_menu("Spell Book stuff", 730.56, "Health Potion", 78.00)

if __name__ == "__main__":
    test_functions()
