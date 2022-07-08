import player, enemies, game_methods, random, game_objects.key_items, game_objects.chests as chests, game_objects.weapons as weapons

def levelOne(player): 
    while player.hp > 0:

        #search bush 
        menu = input("\nYou wake up in a forest and see a bush. Would you like to search it? (y/n) \n").lower()
        if menu == "y":
            player.coin.addCoin(30)
            print(f"\nYou search the bush and notice something shining. You found 30 gold coins! (Coins: {player.coin.getValue()}) \n")
    
        elif menu == "n":
            print("\nYou decide not to search the bush and continue moving forward. \n")

        #wolf attack  
        print("\nAs you continue forward, you hear rustling in the bushes... A wolf leaps out ready to attack! \n")
        wolf1 = enemies.Wolf("Wolf")
        game_methods.encounter(player, wolf1)


        print("You move past the corpse and begin to take in your surroundings. \nYou notice that you must be in the heart of a forest, as there are trees in every direction. ")

        #choosing a path
        choosing = True
        while choosing == True:
            menu = input("\nWhich direction would you like to travel?\n1. East (River) \n2. West (Civilization) \n3. North (Cave) \n4. South (Deeper Into Woods) \n")
            
            if menu == "1": #east river (crab attack)
                menu = input("\nYou emerge from the brush and discover a beach adjacent to a wide rover flowing south. \nYou notice a wrecked ship lying along the shoreline, would you like to search it? (y/n) \n").lower()
                if menu == "y":
                    print("As you walk towards the wreckage, you feel the ground beneath you begin to give in... \nYou slowly rise to find a giant crab emerging from below! \n")
                    giantcrab1 = enemies.GiantCrab("Crabosaur")
                    game_methods.encounter(player, giantcrab1)
                    giantcrab1.drop(player, "You fashion the Crabosaur's large claw into a makeshift sword that you can use to defend yourself.")

                    print("\nYou proceed to the wreckage and make your way into the captain's quarters of the ship; there you find a chest with something shining inside.")
                    menu = input("Would you like to open it?\n")
                    if menu == "y":
                        chest1 = chests.Chest("Chest")
                        sword1 = weapons.Sword()
                        chest1.addItems(sword1)
                        chest1.open()
                    elif menu == "n":
                        print("\nYou chose not to open the chest and make your way back to the woods. \n")
                elif menu == "n":
                    print("\nYou return to the woods. \n")
            if menu == "2": #west civilization
                pass
            if menu == "3": #north cave
                pass
            if menu == "4": #south woods
                pass
