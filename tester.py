import player, enemies, game_methods, levels, game_objects.weapons, game_objects.chests, game_objects.objects, rooms

player1 = player.Tester("Blake")
#player2 = player.Tester("Caileigh")

wolf1 = enemies.Wolf("Wolf")

ogre1 = enemies.Ogre("Ogre")

woodenSword1 = game_objects.weapons.WoodenSword()
dagger1 = game_objects.weapons.Dagger()
sword1 = game_objects.weapons.Sword()
dildo1 = game_objects.objects.Dildo()

# chest1 = game_objects.chests.Chest("Chest")
# chest1.addItems(sword1, dagger1, woodenSword1)
# chest1.open(player1)

testRoom = rooms.TestRoom()

player1.location = testRoom

player1.location.getLocation()
player1.moveUp()
player1.location.getLocation()
player1.moveForward()
player1.location.getLocation()
player1.moveDown()
player1.location.getLocation()
player1.moveBackward()
player1.location.getLocation()
player1.getLocation()


