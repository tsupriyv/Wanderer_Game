from tkinter import *

class Tile:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image
        self.is_occupied = False

    def create_tile(self, source):
        source.create_image(self.x, self.y, image=self.image, anchor=NW)

    def update_occupancy(self):
        self.is_occupied = True




class Wall(Tile):
    def __init__(self, x, y, image):
        super().__init__(x, y, image)

    def create_wall(self, source, walls_location):
        if (self.x, self.y) in walls_location:
            source.create_image(self.x, self.y, image=self.image, anchor=NW)


