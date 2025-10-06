#game functions assignment CSCI 150

def purchase_item(itemPrice, startingMoney, quantityToPurchase = 1):
    """ 
    Allows you to purchase quantityToPurchase items, each costing itemPrice,
    with startingMoney available. Returns items_purchased and money_left. 
    """
    max_affordable = startingMoney // itemPrice
    items_bought = min(quantityToPurchase, max_affordable)
    money_left = startingMoney - (items_bought * itemPrice)
    return items_bought, money_left

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
        description = """
        There is a witch sitting in a hollowed out tree in front of you,
        you don't know what its intentions are yet.
        """
        health = random.randint(20, 50)
        power = random.randint(200, 1000)
        money = random.randint(500, 5000)

    elif monster_choice == "A fairy":
        description = """
        A small fairy hovers next to you, ethereal in it's presence,
        you feel safe and warm, but don't get too close for you don't know its secrets.
        """
        health = random.randint(2, 5)
        power = random.randint(10, 10000)
        money = random.randint(0, 20)

    elif monster_choice == "A goul":
        description = """
        A goul jumps at you from the shadows, draw your weapon quickly,
        for gouls are known to be very viloent and difficult to reason with.
        """
        health = random.randint(2000, 10000)
        power = random.randint(100, 500)
        money = random.randint(1, 500)
    
    return {"name": monster_choice, 
            "description": description, 
            "health": health, 
            "power": power, 
            "money": money}

#print_welcome function

def print_welcome(name, width):
    """
    Creates and prints a welcome greeting string with the given name and width specified.
    """
    greeting = f"Hello, {name}!"
    print(f"{greeting.center(width)}")

#print_shop_menu function

def print_shop_menu(item1Name, item1Price, item2Name, item2Price):
    """
    Creates and prints a menu with the items names and prices as parameters.
    """
    if len(item1Name) > 12:
        item1Name = f"{item1Name[0:10]}…"
    if len(item2Name) > 12:
        item2Name = f"{item2Name[0:10]}…"

    price1 = f"${item1Price:.2f}"
    price2 = f"${item2Price:.2f}"

    print("/" + "-" * 22 + "\\")
    print(f"| {item1Name:<12}{price1:>8} |")
    print(f"| {item2Name:<12}{price2:>8} |")
    print("\\" + "-" * 22 + "/")

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
