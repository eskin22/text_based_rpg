import os
from game_objects.objects import MiscItem
import player, game_methods
import player_classes.testerClass
import levels.levelOne, rooms.levelOneRooms, rooms.testerRoom
import game_objects.weapons as weapons, game_objects.food as food, game_objects.key_items as key_items, game_objects.misc_items as misc_items, game_objects.chests as chests
import enemies.enemyWolf, enemies.enemyOgre
import inventory

player1 = player_classes.testerClass.Tester("Blake")


chest1 = chests.CaptainChest()

player1.inventory.addItems(weapons.Dagger(), weapons.Greatsword(), food.Cake(), key_items.GlowingAmber(), misc_items.ChildsToy(), misc_items.RuinedArtwork(), misc_items.Torch(), weapons.Mace(), food.CheeseWedge())

print(chest1.inventory)
player1.takeItems(chest1, weapons.Dagger())

# inventory1.addItems(weapons.Dagger())
# inventory1.addItems(food.Cake())
# inventory1.addItems(key_items.GlowingAmber())

# print(inventory1.foodsList)



