from Location import Location


class Node:

    def __init__(self, id, location):
        self.id = id
        self.location = location
        self.tag = 0

    def get_id(self):
        return self.id

    def get_location(self):
        return self.location

    def get_tag(self):
        return self.tag

    def __str__(self):
        return f"Node(location: {self.location}, id: {self.id}"

    def __repr__(self):
        return f"Node(location: {self.location}, id: {self.id}"