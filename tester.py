
import player_classes.testerClass, enemies.levelOneEnemies, game_methods
import rooms.testRooms
import game_objects.objects as objects, game_objects.weapons as weapons, game_objects.food as food, game_objects.key_items as key_items, game_objects.misc_items as misc_items
import chests.testChests

#initialize player
player1 = player_classes.testerClass.Tester("Blake")

#initialize testing room
testRoomA = rooms.testRooms.TestRoomA()
player1.location = testRoomA

#initialize enemies
wolf1 = enemies.levelOneEnemies.Wolf()

#initialize objects
sword1 = weapons.Sword()
sword2 = weapons.Sword()
mace1 = weapons.Mace()
cake1 = food.Cake()
glowingAmber1 = key_items.GlowingAmber()
childToy1 = misc_items.ChildsToy()

#initilize chests
chest2 = chests.testChests.TestChestA()

player1.setLocation(2,4)
player1.interact()

chest2.viewInventory()







