from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance", """North of you, the cave mount beckons."""),

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
    print("\nYou've come from far away seeking to gain treasure in this dungeon.")
    name = input("\nWhat is your name? ")
    player = Player(name, room['outside'])
    print(
        f"\nWelcome {name}.\nAfter a long nights rest you feel ready to enter the dungeon.\n{player.room.desc}")
    print("\nControls::\n 'n' to go North.\n 's' to go South.\n 'e' to go East.\n 'w' to go West.\n 'q' to Quit.")
    player_input = ''
    while player_input != 'q':
        player_input = input("\nWhich direction do you head? ")
        new_room = player.room.check_room(player_input)
        if new_room == 'Quit':
            print("\nGame has ended.")
        elif new_room != None:
            player.room = new_room
            print(f"\nYou enter the {player.room.name}")
            print(f"\n{player.room.desc}")
        else:
            print("\nThere is no passage this way.\n You walk into a wall.")


game()
