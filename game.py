"""Core gameplay loop, lets you preform different actions from town,
the loop ends if player health or money goes to or below zero"""

import game_functions as gf

shop = [
       {"name": "Sword", "type": "weapon", "power": 100, "cost": 100, "durab": 2, "equipped": False},
       {"name": "Poison", "type": "item", "power": 10000, "cost": 800, "durab": 1, "equipped": False},
       {"name": "Armor", "type": "clothes", "power": 1, "cost": 200, "durab": 50, "equipped": False}
]

player = gf.load_save()
if not player:
    player = {
       "stats": {"name": None, "hp": 100, "gold": 2000, "location": [0, 0], "life": True},
       "inventory": []
       }

gf.print_welcome(player, 50)

while (player["stats"]["hp"] > 0) and (player["stats"]["gold"] > 0):
    action = gf.town_menu(player).strip().lower()

    if action == "fight":
        gf.display_map(player)

    elif action == "shop":
        gf.purchase_item(player, shop)
        
    elif action == "sleep":
        gf.sleep(player)

    elif action == "save":
        gf.save(player)

    elif action == "quit":
        break

    else:
        print("\nInvalid input, please re-enter your action.\n")
            
print("Thank you for playing!")

