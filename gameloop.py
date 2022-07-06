import player, enemies, game_methods, levels

def main():
    running = True
    while running == True:
        global player1
        player1 = player.Player("Player")
        print("------------------------------------------------------------------\n------------------------------------------------------------------")
        menu = input("\n\nWelcome to the game. Would you like to play? (y/n)")

        if menu.lower() == "n":
            break

        elif menu.lower() == "y":
            playerName = input("\nWhat is your name? \n")
            game_methods.classSelection(playerName)


        else:
            print("\nUh oh. You chose an invalid input. Please try again.\n")

        menu = input("\nOkay, now we're going to go onto the adventure. Are you ready to embark? (y/n)")
        if menu.lower() == "y":
            levels.levelOne(player1)
        else: 
            print("Not going!")
            break
