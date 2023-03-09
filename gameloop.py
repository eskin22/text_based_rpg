import player, enemy, game_methods, levels.levelOne

def main():
    running = True
    while running == True:
        print("\n------------------------------------------------------------------\n------------------------------------------------------------------")
        print("                            GAME                                   ")
        print("------------------------------------------------------------------\n------------------------------------------------------------------")
        menu = input("\nWould you like to play? (y/n) \n")

        if menu.lower() == "n":
            break
        elif menu.lower() == "y":
            print("\nWelcome! The following is a text-based RPG developed in Python. \nBefore you may embark on your quest, we must establish your character information.")
            playerName = input("\nLet's start with the basics: What is your name? \n")
            player1 = game_methods.classSelection(playerName)
        else:
            print("\nError: You chose an invalid input. Please try again. \n")

        menu = input(f"\n{playerName}, you're about to embark on an adventure. Are you ready to begin? (y/n) \n")
        if menu.lower() == "y":
            levels.levelOne.play(player1)
        else: 
            print("Not going!")
            break
