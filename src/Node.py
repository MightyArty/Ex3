from Location import Location


class Node:

    def __init__(self, id, location):
        self.id = id
        self.location = location

    def __str__(self):
        return f"Node(location: {self.location}, id: {self.id}"

    def __repr__(self):
        return f"Node(location: {self.location}, id: {self.id}"