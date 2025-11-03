"""Core gameplay loop, lets you preform different actions from town,
the loop ends if player health or money goes to or below zero"""

import game_functions as gf

player = {"name": "", "hp": 100, "gold": 1000, "location": "town", "life": True}
inventory = []
shop = [
       {"name": "Sword", "type": "weapon", "power": 100, "cost": 100, "durab": 10},
       {"name": "Poison", "type": "item", "power": 10000, "cost": 800, "durab": 1}
]

gf.print_welcome(player, 50)

while (player["hp"] > 0) and (player["gold"] > 0):
    # player["equipped"] = {"name": "nothing"}
    action = gf.town_menu(player, inventory)

    if action == "leave":
            gf.fight(player, inventory)

    elif action == "shop":
            gf.purchase_item(player, inventory, shop)
        
    elif action == "sleep":
            gf.sleep(player)
        
    elif action == "quit":
            player["hp"] = 0
            
    else:
        print("""
Invalid input, please re-enter your action.""")
            
print("Thank you for playing!")

