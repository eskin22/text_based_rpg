import player, enemy, game_methods, random, game_objects.key_items as key_items, game_objects.objects as objects, game_objects.chests as chests, game_objects.weapons as weapons

def play(player): 
    while player.hp > 0:

        print("------------------------------------------------------------------")
        print("                         LEVEL ONE                                   ")
        print("------------------------------------------------------------------")

        #intantiate enemies
        wolf1 = enemy.Wolf("Wolf")
        giantcrab1 = enemy.GiantCrab("Crabosaur")

        #instantiate chest
        chest1 = chests.CaptainChest()

        #search bush (coins)
        menuMain = input("\nYou wake up in a forest and see a bush. Would you like to search it? (y/n) \n").lower()
        if menuMain == "y":
            coins = objects.Coins(30)
            player.addCoins(coins)
            print(f"\nYou search the bush and notice something shining. You found 30 gold coins! (Coins: {player.showBankValue()}) \n")

        #decide not to search bush (no coins)
        elif menuMain == "n":
            print("\nYou decide not to search the bush and continue moving forward. \n")

        #wolf attack  
        print("\nAs you continue forward, you hear rustling in the bushes... A wolf leaps out ready to attack! \n")
        game_methods.encounter(player, wolf1)
        print("You move past the corpse and begin to take in your surroundings. \nYou notice that you must be in the heart of a forest, as there are trees in every direction. ")

        #stop at crossroads, choose path
        while player.hp > 0:
            menu0 = input("\nWhich direction would you like to travel?\n1. East (River) \n2. West (Civilization) \n3. North (Cave) \n4. South (Deeper Into Woods) \n")
            
            #east (river, sunken ship)
            if menu0 == "1": 

                #crab attack (get crab sword)
                menu1 = input("\nYou emerge from the brush and discover a beach adjacent to a wide rover flowing south. \nYou notice a wrecked ship lying along the shoreline, would you like to search it? (y/n) \n").lower()
                if menu1 == "y":
                    if giantcrab1.isDead == True:
                        pass
                    else:
                        print("As you walk towards the wreckage, you feel the ground beneath you begin to give in... \nYou slowly rise to find a giant crab emerging from below! \n")
                        game_methods.encounter(player, giantcrab1)
                        giantcrab1.drop(player, "You fashion the Crabosaur's large claw into a makeshift sword that you can use to defend yourself.")

                    #go to sunken ship
                    menu2 = chest1.intro()
                    if menu2 == "y":
                        chest1.open(player)
                        print("\nAfter searching the chest in the wreckage, you retread back the way you came into the woods.")
                    elif menu2 == "n":
                        print("\nYou chose not to open the chest and make your way back to the woods. \n")
                    # else:
                    #     print("\nError: Invalid input. Please try again. \n")
                elif menu1 == "n":
                    print("\nYou return to the woods. \n")

                # else:
                #     print("\nError: Invalid input. Please try again. \n")

            #west (civilization)
            if menu0 == "2": 
                pass
            
            #north (cave)
            if menu0 == "3": 
                pass
            
            #south (deeper into the woods)
            if menu0 == "4":
                pass

            # else:
            #     print("\nError: Invalid input. Please try again. \n")