import player, random, sys

def classSelection(playerName):
    running = True
    while running == True: 
        print(f"\nHello {playerName}! The next question relates to your class. \nYour class affects your character stats and the playstyle you adopt throughout your adventure.\nPlease select a class from the options below. TIP: You can get more info on a class by typing the $info command preceding your selection.")
        menu = str(input("\n1. Warrior \n2. Merchant \n3. Mage \n"))
        if menu == "1":
            player1 = player.Warrior(playerName)
            break
        elif menu == "$info 1":
            classInfo(player.Warrior("Info"))    
        elif menu == "2":
            player1 = player.Merchant(playerName)
            break
        elif menu == "$info 2":
            classInfo(player.Merchant("Info"))
        elif menu == "3":
            player1 = player.Mage(playerName)
            break
        elif menu == "$info 3":
            classInfo(player.Mage("Info"))
        else:
            print("\nError: Invalid input. Please try again. \n")
    return player1

def classInfo(player):
    running = True
    while running == True:
        print("------------------------------------------------------------------")
        print("                            INFO                                   ")
        print("------------------------------------------------------------------")
        print(f"Class: {player.className} \nHP: {player.hp} \nMagic Affinity: {player.magicAffinity} \nStrength: {player.strength} \nCoin: {player.coin.value}")
        print("------------------------------------------------------------------")
        print("                            BACK ($back)                                   ")
        print("------------------------------------------------------------------")  

        menu = input()
        if menu.lower() == "$back":
            break
        else: 
            print("\nError: You chose an invalid input. Please try again. \n")

def battle(player, enemy):
    print()
    while ((player.hp > 0) and (enemy.hp > 0)):
        if player.speed == enemy.speed:
            if (random.randint(0,9)<=5):
                player.attack(enemy)
                if enemy.hp > 0:
                    enemy.attack(player)
            else:
                enemy.attack(player)
                if player.hp > 0:
                    player.attack(enemy)
        elif player.speed > enemy.speed:
            player.attack(enemy)
            if enemy.hp > 0:
                enemy.attack(player)
        else:
            enemy.attack(player)
            if player.hp > 0:
                player.attack(enemy)
            
        if enemy.hp <= 0:
            enemy.isDead = True
            break
        
        if player.hp <= 0:
            sys.exit()
    
    
def encounter(player, enemy):
    print("------------------------------------------------------------------")
    print(f"                            {enemy.name.upper()}            HP: {enemy.hp}       DMG: {enemy.attackPower}                          ")
    print("------------------------------------------------------------------")

    menuAttack = input(f"\nWhat would you like to do? ($attack/$flee) \n").lower()
    if menuAttack == "$attack":
        battle(player, enemy)
    elif menuAttack == "$flee":
        randNum = random.randint(0,9)
        if (randNum <= 7):
            print("\nYou escaped safely. \n")
        elif (randNum > 7):
            print(f"\nYou try to escape, but the {enemy.name} has cornered you! \n")
            battle(player, enemy)
    # else:
    #     print("\nError: Invalid input. Please try again. \n")
