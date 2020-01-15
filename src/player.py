# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self,player_location):
        self.location = player_location

    def __repr__(self):
        return self.location