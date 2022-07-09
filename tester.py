import player, enemies, game_methods, levels, game_objects.weapons, game_objects.chests, game_objects.objects, rooms.levelOneRooms

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

# square1 = rooms.levelOneRooms.Square()
# square2 = rooms.levelOneRooms.Square()
# square3 = rooms.levelOneRooms.Square()
# square4 = rooms.levelOneRooms.Square()
# square5 = rooms.levelOneRooms.Square()
# square6 = rooms.levelOneRooms.Square()
# square7 = rooms.levelOneRooms.Square()
# square8 = rooms.levelOneRooms.Square()
# square9 = rooms.levelOneRooms.Square()
# list = [square1, square2, square3]

alien1 = enemies.Alien("Alien")
game_methods.encounter(player1, alien1)



