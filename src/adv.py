from room import Room
from player import Player

import argparse

import cmd, sys, textwrap
    
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}
location = 'outside'
player = {
    "name": 'Dylan',
    "condition": 'healty',
    "location": Player(location)
}

print('Player Location: ', player['location'])

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


#
# Main
#

SCREEN_WIDTH = 80

# desc = 'The town square is a large open space with a fountain in the center. Streets lead in all directions.'

# for line in textwrap.wrap(desc, SCREEN_WIDTH):
#     print(line)

# Start in outside room

location = 'Outside Cave Entrance'

# Make a new player object that is currently in the 'outside' room.

class PlayerOne(Player):
    def __init__(self, name, condition, location):
        self.name = name
        self.condition = condition
        self.location = location
player_info = PlayerOne('Dylan', 'healthy', location)

print(player_info)
# Write a loop that:
#
# * Prints the current room name
def status(location):
    print('hi from the outside')
    
# * Prints the current description (the textwrap module might be useful here).

# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

status(location)

def moveDirection(direction):
    """A helper function that changes the location of the player."""
    print(PlayerOne.location)



# for i in room:
#     print(f'You are currently in {i}:\n\nRoom description:\n{room[i]}\n\n')
    
class GameControls(cmd.Cmd):
    prompt = '\n>> '

    # The default() method is called when none of the other do_*() command methods match.
    def default(self, arg):
        print('I do not understand that command. Type "help" for a list of commands.')

    # A very simple "quit" command to terminate the program:
    def do_quit(self, arg):
        """Quit the game."""
        return True # this exits the Cmd application loop in TextAdventureCmd.cmdloop()
    
    def do_north(self, arg):
        """Move somewhere. Quietly."""
        moveDirection('north')

    def help_combat(self):
        print('Combat is not implemented in this program.')
        
if __name__ == '__main__':
    print('Space Survival Horror Game!')
    print('===========================')
    print()
    print('(Type "help" for commands.)')
    print()
    GameControls().cmdloop()
    print('Thanks for playing!')