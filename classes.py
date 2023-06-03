class Player:
    def __init__(self, name="", intelligence=0, strength=0, health=0):
        self.name = name
        self.intelligence = intelligence
        self.strength = strength
        self.health = health


class Enemy:
    def __init__(self, type="", difficulty="", health=0, max_attack=0, message=""):
        self.type = type
        self.difficulty = difficulty
        self.health = health
        self.max_attack = max_attack
        self.message = message
