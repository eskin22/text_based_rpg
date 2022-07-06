import player

def classSelection(playerName):
    running = True
    while running == True: 
            print(f"\nHello {playerName}! The next question relates to your class. In this game there are a variety of classes that you can choose from.\nPlease select a class from the options below, you can get more info on a class by typing the $info command following the selection.")
            menu = str(input("\n1. Warrior \n2. Merchant \n3. Mage \n"))
            if menu == "1":
                player1 = player.Warrior(playerName)
                break
            elif menu == "$info 1":
                classInfo(player.Warrior("Info"))    
            elif menu == "2":
                player1 = player.Merchant(playerName)
                return player1
                break
            elif menu == "$info 2":
                classInfo(player.Merchant("Info"))
            elif menu == "3":
                player1 = player.Mage(playerName)
                break
            elif menu == "$info 3":
                classInfo(player.Mage("Info"))

def classInfo(player):
    running = True
    while running == True:
        print("------------------------------------------------------------------\n------------------------------------------------------------------")
        print("                            INFO                                   ")
        print(f"Class: {player.className} \nHP: {player.hp} \nMagic Affinity: {player.magicAffinity} \nStrength: {player.strength} \nCoin: {player.coin.value}")
        print("\n------------------------------------------------------------------")
        print("                            BACK ($back)                                   ")

        menu = input()
        if menu.lower() == "$back":
            break
        else: 
            print("Uh oh, wrong input. Please try again.")

    


def encounter(player, enemy):
    player.attack(enemy)
