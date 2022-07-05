import player, enemies

def main():
    running = True
    while running == True:
        print("------------------------------------------------------------------")
        menu = input("\n\nWelcome to the game. Would you like to play? (y/n)")

        if menu.lower() == "n":
            break

        elif menu.lower() == "y":
            player_name = input("\nWelcome to the game. You're about to embark on an incredible adventure; but first things first: What is your name? \n")
            print(f"\nHello {player_name}! The next question relates to your class. In this game there are a variety of classes that you can choose from.\nPlease select a class from the options below:")
            menu = str(input("\n1. Warrior\n"))
            if menu == "1":
                player1 = player.Warrior(player_name)
                print("\nYou selected the warrior class!")
            menu = input("\nQuit? (y) \n")
            if menu.lower() == "y":
                print("\nGame Over. Goodbye! \n")
                break
            else:
                "\nTry again\n"

        else:
            print("\nUh oh. You chose an invalid input. Please try again.\n")
