class Node:

    def __init__(self, myID: int, pos: tuple = None):
        self.id = myID
        self.pos = pos
        self.tag = 0
        self.info = ""
        self.weight = 0

    def get_id(self):
        return self.id

    def get_tag(self):
        return self.tag

    def __str__(self):
        return str(self.id)

    def __repr__(self):
        return f"Node id: {self.id}, pos: {self.pos}"

    def location_toString(self):
        return f"({self.pos[0]},{self.pos[1]},{self.pos[2]})"