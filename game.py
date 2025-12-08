"""Core gameplay loop, lets you preform different actions from town,
the loop ends if player health or money goes to or below zero"""

import game_functions as gf

shop = [
       {"name": "Sword", "type": "weapon", "power": 100, "cost": 100, "durab": 5, "equipped": False},
       {"name": "Poison", "type": "item", "power": 10000, "cost": 800, "durab": 1, "equipped": False},
       {"name": "Armor", "type": "clothes", "power": 1, "cost": 200, "durab": 50, "equipped": False}
]

player = gf.load_save()
gf.print_welcome(player, 50)

while (player["stats"]["hp"] > 0) and (player["stats"]["gold"] > 0):
    
    action = gf.town_menu(player).strip().lower()

    if action == "map":
        gf.display_map(player)
        if player["stats"]["location"] == [6, 4]:
            gf.fight(player)
        else:
            pass

    elif action == "shop":
        gf.purchase_item(player, shop)

    elif action == "casino":
        gf.casino(player)
        
    elif action == "sleep":
        gf.sleep(player)

    elif action == "save":
        gf.save(player)

    elif action == "quit":
        print("Thank you for playing!")
        break

    else:
        print("\nInvalid input, please re-enter your action.\n")

