import player, enemies, game_methods, levels, game_objects.weapons, game_objects.chests, game_objects.objects

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

#levels.levelOne(player1)

chest2 = game_objects.chests.Chest("Captain's Chest")
chest2.open(player1)


