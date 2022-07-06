import player

def levelOne(player):
    running = True 
    while running == True:
        menu = input("\nYou wake up in a forest and see a bush. Would you like to search it? (y/n) \n").lower()
        if menu == "y":
            player.coin.addCoin(30)
            print(f"\nYou search the bush and notice something shining. You found 30 gold coins! (Coins: {player.coin.getValue()})")
    
        elif menu == "n":
            print("\nYou decide not to search the bush and continue moving forward. \n")
          
        print("\nAs you continue forward, you stumble upon a tribe of gnolls! \n")

        menu = input("\nWhat would you like to do? (attack/run)\n").lower()
        if menu == "$attack":
            print("You attack the gnolls!")