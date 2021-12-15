from Loaction import Location


class Node:
    id = 0
    location = Location

    def __init__(self, id, location):
        self.id = id
        self.location = location(0, 0, 0)
