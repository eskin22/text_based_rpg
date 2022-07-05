import pygame


class Enemy():
    def __init__(self, name, attack, hp):
        self.name = name
        self.attack = attack
        self.hp = hp
        print(f"New enemy {name} successfully initialized.")

    def attack(self, player):
        player.hp -= self.attack
        print(f"{self.name} attacks {player.name} and does {self.attack} damage!")

