# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, condition, location):
        self.name = name
        self.condition = condition
        self.location = location
