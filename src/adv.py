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


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Load room with items
room['outside'].items = ['stick', 'lantern oil']
room['foyer'].items = ['leather boots']
room['overlook'].items = ['telescope', 'binoculars']
room['narrow'].items = ['painting']
room['treasure'].items = ['dry blood']

#
# Main
#

# Start in outside room with an empty rucksack
location = 'outside'
items = ['rucksack']

# Make a new player object that is currently in the 'outside' room.

class PlayerOne(Player):
    def __init__(self, name, condition, location, items):
        self.name = name
        self.condition = condition
        self.location = location
        self.items = items
        
player_info = PlayerOne('Dylan', 'healthy', location, items)
print(player_info.items)

SCREEN_WIDTH = 50

# Write a loop that:
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
# If the user enters "q", quit the game.

def moveDirection(direction):
    """A helper function that changes the location of the player."""
    if direction == 'north' and hasattr(room[player_info.location], 'n_to') and (room[player_info.location].n_to != room[player_info.location]):        
        if hasattr(room[player_info.location], 'n_to'):
            # cur_rm_desc = room[player_info.location]
            to_rm_desc = room[player_info.location].n_to
            for i in room.keys():                
                if player_info.location == i and hasattr(room[player_info.location], 'n_to'):                    
                    for i in room.keys():
                        if to_rm_desc == room[i]:
                            player_info.location = i
        print('Current room: ', player_info.location)
        print(f'You are currently in {player_info.location}:\n\nRoom description:\n{room[player_info.location]}\n\n')
    elif direction == 'south' and hasattr(room[player_info.location], 's_to') and (room[player_info.location].s_to != room[player_info.location]):        
        if hasattr(room[player_info.location], 's_to'):
            # cur_rm_desc = room[player_info.location]
            to_rm_desc = room[player_info.location].s_to
            for i in room.keys():                
                if player_info.location == i and hasattr(room[player_info.location], 's_to'):                    
                    for i in room.keys():
                        if to_rm_desc == room[i]:
                            player_info.location = i
        print('Current room: ', player_info.location)
        print(f'You are currently in {player_info.location}:\n\nRoom description:\n{room[player_info.location]}\n\n')
    elif direction == 'east' and hasattr(room[player_info.location], 'e_to') and (room[player_info.location].e_to != room[player_info.location]):        
        if hasattr(room[player_info.location], 'e_to'):
            # cur_rm_desc = room[player_info.location]
            to_rm_desc = room[player_info.location].e_to
            for i in room.keys():                
                if player_info.location == i and hasattr(room[player_info.location], 'e_to'):                    
                    for i in room.keys():
                        if to_rm_desc == room[i]:
                            player_info.location = i
        print('Current room: ', player_info.location)
        print(f'You are currently in {player_info.location}:\n\nRoom description:\n{room[player_info.location]}\n\n')
    elif direction == 'west' and hasattr(room[player_info.location], 'w_to') and (room[player_info.location].w_to != room[player_info.location]):        
        if hasattr(room[player_info.location], 'w_to'):
            # cur_rm_desc = room[player_info.location]
            to_rm_desc = room[player_info.location].w_to
            for i in room.keys():                
                if player_info.location == i and hasattr(room[player_info.location], 'w_to'):                    
                    for i in room.keys():
                        if to_rm_desc == room[i]:
                            player_info.location = i
        print('Current room: ', player_info.location)
        print(f'You are currently in {player_info.location}:\n\nRoom description:\n{room[player_info.location]}\n\n')            
    else: print("You can't go that way")
# look function that checks room for items

def look():
    if len(room[player_info.location].items) == 0:
        print('Oof dusty.')
    else:
        print('The horrors you see are: ')
        for i in room[player_info.location].items:
            print(i) 

def take():
    if len(room[player_info.location].items) == 0:
        print("Room's been cleaned out. By sombody... \n or something! Or was it me? <<hiccup>>")
    else:    
        player_info.items = player_info.items + room[player_info.location].items
        room[player_info.location].items = []
        print("You've added some weight to your rucksack. (type 'items' to see what you have)")

def check_bag():
    if len(player_info.items) == 0:
        print('nothing in here yet\nkeep your eyes peeled')
    else:
        print('Your items:')
        for i in player_info.items:
            print(i)
    
                
class GameControls(cmd.Cmd):
    prompt = '\n>> '

    # The default() method is called when none of the other do_*() command methods match.
    def default(self, arg):
        print('I do not understand that command. Type "help" for a list of commands.')

    # A very simple "quit" command to terminate the program:
    def do_quit(self, arg):
        """Quit the game."""
        return True # this exits the Cmd application loop in GameControls.cmdloop()
    
    def do_north(self, arg):
        """Move somewhere. Quietly."""
        moveDirection('north')
    
    def do_south(self, arg):
        """Move somewhere. Quietly."""
        moveDirection('south')
    
    def do_east(self, arg):
        """Move somewhere. Quietly."""
        moveDirection('east')
    
    def do_west(self, arg):
        """Move somewhere. Quietly."""
        moveDirection('west')
    def do_location(self, arg):
        """Where am I?"""
        print(player_info.location)
    def do_look(self, arg):
        """Be a nosy dungeon dweller"""
        look()
    def do_take(self, arg):
        take()
    def do_items(self, arg):
        """What's in the old bag?"""
        check_bag()
            
    def help_combat(self):
        print('Combat is not implemented in this program.')
        
if __name__ == '__main__':
    print('Space Survival Horror Game!')
    print('===========================')
    print()
    print('Game Controls:')
    print('north south east west')
    print()
    print('(Type "help" for commands.)')
    GameControls().cmdloop()
    print('Visit us again...')