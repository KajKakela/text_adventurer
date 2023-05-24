# Define name to a new player. Empty name not accepted
def new_player_name():
    player_name = ""
    while player_name == "":
        player_name = input("Hello! Give a name to your adventurer!: ")

        if player_name.isspace() or player_name == "":
            print("Hey, you have to give a name to your adventurer!")
            player_name = ""

    return player_name
