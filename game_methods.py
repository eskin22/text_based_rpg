import random, sys
import player_classes.warriorClass, player_classes.merchantClass, player_classes.mageClass, player_classes.testerClass

def classSelection(playerName):
    running = True
    while running == True: 
        print(f"\nHello {playerName}! The next question relates to your class. \nYour class affects your character stats and the playstyle you adopt throughout your adventure.\nPlease select a class from the options below. TIP: You can get more info on a class by typing the $info command preceding your selection.")
        menu = str(input("\n1. Warrior \n2. Merchant \n3. Mage \n"))
        if menu == "1":
            player1 = player_classes.warriorClass.Warrior(playerName)
            break
        elif menu == "$info 1":
            classInfo(player_classes.warriorClass.Warrior("Info"))    
        elif menu == "2":
            player1 = player_classes.merchantClass.Merchant(playerName)
            break
        elif menu == "$info 2":
            classInfo(player_classes.merchantClass.Merchant("Info"))
        elif menu == "3":
            player1 = player_classes.mageClass.Mage(playerName)
            break
        elif menu == "$info 3":
            classInfo(player_classes.mageClass.Mage("Info"))
        else:
            print("\nError: Invalid input. Please try again. \n")
    return player1

def classInfo(player):
    running = True
    while running == True:
        print("\n--------------------------------------------------")
        print("{:^50}".format("INFO"))
        print("--------------------------------------------------")
        print("{:<40}".format("     - Class: " + player.className))
        print("{:<40}".format("     - HP: " + str(player.hp)))
        print("{:<40}".format("     - Magic Affinity: " + str(player.magicAffinity)))
        print("{:<40}".format("     - Strength: " + str(player.strength)))
        print("{:<40}".format("     - Coins: " + str(player.getBankValue())))
        
        print("--------------------------------------------------")
        print("{:^55}".format("BACK ($back) "))
        print("--------------------------------------------------")

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
    print("------------------------------------------------------------------------------------------")
    print("{:>8}{:^68}{:>5}".format("ENEMY: " + enemy.name.upper(), "HP: " + str(enemy.hp), "DAMAGE: " + str(enemy.attackPower)))
    print("------------------------------------------------------------------------------------------")

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
    else:
        print("\nError: Invalid input. Please try again. \n")

def explore(player):
    running = True

    while running == True:
        menuExplore = input("\nWhat would you like to do? TIP: use the $help command to get a list of action commands ")
        
        if menuExplore.startswith("$go"):
            selection = menuExplore[3:]
            if selection.startswith(" f"):
                player.moveForward()
            elif selection.startswith(" b"):
                player.moveBackward()
            elif selection.startswith(" r"):
                player.moveDown()
            elif selection.startswith(" l"):
                player.moveUp()
            else:
                print("ERROR: Invalid input. Please try again. ")

        elif menuExplore.startswith("$ins"):
            player.inspect()

        elif menuExplore.startswith("$int"):
            player.interact()
        
        else:
            print("ERROR: Invalid input. Please try again. ")



