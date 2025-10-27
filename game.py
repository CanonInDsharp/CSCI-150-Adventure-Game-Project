"""Core gameplay loop, lets you preform different actions from town
the loop ends if player health or money goes below zero"""

import game_functions as gf

gf.print_welcome(input("Please input the name of player: "), 50)

player_gold = 100
player_hp = 100
life = True

while (player_hp > 0) and (player_gold > 0):
        
        print(f"""
Your health: {player_hp}. Your gold: {player_gold}.
You're in town, what do you want to do? Or actions are:
leave (fight monster), sleep (restore 10hp for 10 gold), or quit game.
              """)
        
        action = input("leave town, sleep, or quit: ")

        if action == "leave":

            player_hp, player_gold = gf.fight(player_hp, player_gold)
        
        elif action == "sleep":

            player_hp, player_gold = gf.sleep(player_hp, player_gold)
        
        elif action == "quit":
            break
            
        else:
            print("""
Invalid input.
                  """)
            
print("Thank you for playing!")

