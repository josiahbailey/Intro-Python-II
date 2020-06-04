from room import Room
from player import Player
from item import Item, Equipment, Consumable

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance", """North of you, the cave mount beckons.""", [Item('Dungeon Key'), Equipment("Beginner Sword", {"weapon": 5})]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasury': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasury']
room['treasury'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


def game():
    # Introduction
    print("\nYou've come from far away seeking to gain treasure in this dungeon.")
    name = input("\nWhat is your name? ")
    player = Player(name, room['outside'])
    print(
        f"\nWelcome {name}.\nAfter a long nights rest you feel ready to enter the dungeon.\n{player.room.desc}")
    print("\nControls::\n 'm' to move\n 'i' opens invetory\n 'q' to Quit.")
    player_input = ''

    # Game Loop
    while player_input != 'q':
        current_room = room[player.room.name]
        items = current_room.items
        # Check if the player wants the items
        if len(items) > 0:
            for item in items:
                print(f"\nThere is a {item.name} laying on the ground")
                player_input = input("Do you wish to take it y or n?")
                if player_input == 'y':
                    player.pickup(item)
        # Player Choice
        player_input = input("\nWhat do you want to do? ")
        # M means player chose to move
        if player_input == 'm':
            print(
                "\n 'w' to go North.\n 's' to go South.\n 'a' to go West.\n 'd' to go East.\n")
            new_room = player.room.move_room(player_input)
            if new_room == 'Quit':
                print("\nGame has ended.")
            elif new_room != None:
                player.move(new_room)
                print(f"\nYou enter the {player.room.name}")
                print(f"\n{player.room.desc}")
            else:
                print("\nThere is no passage this way. You walk into a wall.")
        # I means player chose to view invetory
        elif player_input == 'i':
            print("\n INVENTORY")
            count = 0
            for item in player.inv:
                count += 1
                print(f"slot: {count} name: {item.name} type: {item.type}\n")
            player_input = input(
                "Press 'i' again to interact with items or 'b' to go back: ")
            if player_input == 'i':
                player_input = input(
                    "Select slot number of item or press 'b' to go back: ")
                if player_input != 'b':
                    item = player.inv[int(player_input) - 1]
                    print(
                        f"type: {item.type}\n name: {item.name} effect: {item.effect}")


game()
