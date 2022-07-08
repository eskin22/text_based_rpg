import player, enemies, game_methods, random, game_objects.key_items, game_objects.chests as chests, game_objects.weapons as weapons

def levelOne(player): 
    while player.hp > 0:

        print("------------------------------------------------------------------")
        print("                         LEVEL ONE                                   ")
        print("------------------------------------------------------------------")

        #intantiate enemies
        wolf1 = enemies.Wolf("Wolf")
        giantcrab1 = enemies.GiantCrab("Crabosaur")

        #instantiate chest
        chest1 = chests.LevelOneChest()

        #search bush (coins)
        menu = input("\nYou wake up in a forest and see a bush. Would you like to search it? (y/n) \n").lower()
        if menu == "y":
            player.addCoin(10)
            print(f"\nYou search the bush and notice something shining. You found 30 gold coins! (Coins: {player.coin.getValue()}) \n")

        #decide not to search bush (no coins)
        elif menu == "n":
            print("\nYou decide not to search the bush and continue moving forward. \n")

        #wolf attack  
        print("\nAs you continue forward, you hear rustling in the bushes... A wolf leaps out ready to attack! \n")
        game_methods.encounter(player, wolf1)
        print("You move past the corpse and begin to take in your surroundings. \nYou notice that you must be in the heart of a forest, as there are trees in every direction. ")

        #stop at crossroads, choose path
        while player.hp > 0:
            menu = input("\nWhich direction would you like to travel?\n1. East (River) \n2. West (Civilization) \n3. North (Cave) \n4. South (Deeper Into Woods) \n")
            
            #east (river, sunken ship)
            if menu == "1": 

                #crab attack (get crab sword)
                menu = input("\nYou emerge from the brush and discover a beach adjacent to a wide rover flowing south. \nYou notice a wrecked ship lying along the shoreline, would you like to search it? (y/n) \n").lower()
                if menu == "y":
                    if giantcrab1.isDead == True:
                        pass
                    else:
                        print("As you walk towards the wreckage, you feel the ground beneath you begin to give in... \nYou slowly rise to find a giant crab emerging from below! \n")
                        game_methods.encounter(player, giantcrab1)
                        giantcrab1.drop(player, "You fashion the Crabosaur's large claw into a makeshift sword that you can use to defend yourself.")

                    #go to sunken ship
                    chest1.intro()
                    if menu == "y":
                        chest1.open(player)
                        print("\nAfter searching the chest in the wreckage, you retread back the way you came into the woods.")
                    elif menu == "n":
                        print("\nYou chose not to open the chest and make your way back to the woods. \n")
                elif menu == "n":
                    print("\nYou return to the woods. \n")

            #west (civilization)
            if menu == "2": 
                pass
            
            #north (cave)
            if menu == "3": 
                pass
            
            #south (deeper into the woods)
            if menu == "4":
                pass
