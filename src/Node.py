from Location import Location


class Node:

    def __init__(self, id: int, location: tuple = None):
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
        return str(self.id)

    def location_toString(self):
        return f"{self.location[0]},{self.location[1]},{self.location[2]}"