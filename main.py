import functions
import classes
import random
import os
import sys


# Create new player and assign name to them
player_name = functions.new_player_name().capitalize()
player_points = {"intelligence": 0, "strength": 0, "health": 0}
points_left = 20

player = classes.Player(player_name)

print(
    f"\nWelcome {player.name}! Before you start your adventure, we will assign points to your skills. You have 3 skills: 'Intelligence', 'Strength' and 'Health'. Your skill points will be assigned randomly. When you are satisfied with your skill points, type 'y'\n"
)


# assign skill points to player
while True:
    player.intelligence = random.randint(5, 10)
    player.strength = random.randint(5, 10)
    player.health = random.randint(5, 10)

    print(
        f"Intelligence: {player.intelligence}, Strength: {player.strength}, Health: {player.health}"
    )
    ready = input(
        "Do you want to start your journey with these skill points? Type 'y' if you are ready to start. Otherwise press enter: "
    ).lower()

    if ready == "y":
        if sys.platform.startswith("win32"):
            os.system("cls")
        else:
            os.system("clear")
        break
    else:
        if sys.platform.startswith("win32"):
            os.system("cls")
        else:
            os.system("clear")
        continue

print(
    f"Great! You start with Intelligence: {player.intelligence}, Strength: {player.strength}, Health: {player.health}"
)
