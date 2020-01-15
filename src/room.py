# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, room_name, room_desc):
        self.name = room_name
        self.description = room_desc
        
    def __repr__(self):
        return self.description
