from Location import Location
import random


class Node:

    def __init__(self, key, loc):
        self.id = key
        self.location = loc
        self.tag = 0
        self.info = ""
        self.weight = 0

