import random


# Define name to a new player. Empty name not accepted
def new_player_name():
    player_name = ""
    while player_name == "":
        player_name = input("Hello! Give a name to your adventurer!: ")

        if player_name.isspace() or player_name == "":
            print("Hey, you have to give a name to your adventurer!")
            player_name = ""

    return player_name


def new_enemy(player_health):
    enemies_types = {
        "Wolf": {
            "difficulty": "easy",
            "health": 8,
            "max_Attack": 2,
            "message": "message",
        },
        "Bear": {
            "difficulty": "easy",
            "health": 9,
            "max_attack": 2,
            "message": "message",
        },
        "Lion": {
            "difficulty": "medium",
            "health": 10,
            "max_attack": 4,
            "message": "message",
        },
        "Hippo": {
            "difficulty": "medium",
            "health": 11,
            "max_attack": 4,
            "message": "message",
        },
        "Bear": {
            "difficulty": "hard",
            "health": 15,
            "max_attack": 6,
            "message": "message",
        },
    }

    if player_health < 12:
        enemy_difficulty = "easy"
    elif player_health < 15:
        enemy_difficulty = "medium"
    else:
        enemy_difficulty = "hard"

    list_of_possible_enemies = []

    for type in enemies_types:
        if enemy_difficulty in enemies_types[type].values():
            list_of_possible_enemies.append(type)

    enemy = random.choice(list_of_possible_enemies)
