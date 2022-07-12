import game_objects.weapons as weapons

class Enemy():
    def __init__(self, name):
        self.name = name
        self.hp = None
        self.attackPower = None
        self.speed = None
        self.item = None
        self.isDead = False

    def attack(self, player):
        player.hp -= self.attackPower
        if player.hp <= 0:
            player.hp = 0
        print(f"{self.name} attacks {player.name} and does {self.attackPower} damage! You have {player.hp} health remaining.")
        if player.hp <= 0:
            print("\n------------------------------------------------------------------")
            print("                    You have been slain!")
            print("------------------------------------------------------------------")

            print("\n------------------------------------------------------------------\n------------------------------------------------------------------")
            print("                         GAME OVER!                                   ")
            print("------------------------------------------------------------------\n------------------------------------------------------------------")

    def drop(self, player, introString):
        menu = input(f"\n{introString}\nWould you like to add the {self.item.name} to your inventory? (y/n)\n").lower()
        if menu == "y":
            player.inventory.append(self.item)
            print(f"\n{self.item.name} added to inventory. \n")
            if (isinstance(self.item, weapons.Weapon)):
                menu = input("Would you like to equip it now? (y/n)\n").lower()
                if menu == "y":
                    player.equipWeapon(self.item)
                elif menu == "n":
                    pass
        elif menu == "n":
            print(f"\nThe {self.item.name} was not added. You continue on. \n")

    



