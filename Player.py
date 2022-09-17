import random
import pygame
from tkinter import *
pygame.init()


class Player:

    def __init__(self, x, y, image, name, root):
        self.move_sound = pygame.mixer.Sound("walk.mp3")
        self.move_sound.set_volume(.1)
        self.fight_sound = pygame.mixer.Sound("fight.wav")
        self.fight_sound.set_volume(.5)
        self.x = x
        self.y = y
        self.root = root
        self.image = image
        self.name = name
        self.location = (self.x, self.y)
        self.is_deleted = False
        self.health = 20

    def create_player(self, source):
        if not self.is_deleted:
            source.create_image(self.x * 75, self.y * 75, image=self.image, anchor=NW)

    def delete(self, source, opponent=None):
        source.delete(self)
        self.image = None
        if opponent is not None and self.is_deleted is False:
            opponent.health += 10
        # self.is_deleted = True

    def update_image(self, image):
        self.image = image

    def move(self, func, walls_location, count_move, image, monster_location, speed=1):
        self.move_sound.play()

        # if self.name != "Hero":
        if func == "left" and self.x > 0 and (self.x - 1, self.y) not in walls_location:
            self.update_image(image)
            if self.name == "Hero":
                self.x -= speed
            else:
                if count_move % 2 == 0:
                    self.x -= speed


        elif func == "right" and self.x < 9 and (self.x + 1, self.y) not in walls_location:
            self.update_image(image)
            if self.name == "Hero":
                self.x += speed
            else:
                if count_move % 2 == 0:
                    self.x += speed


        elif func == "up" and self.y > 0 and (self.x, self.y - 1) not in walls_location:
            self.update_image(image)
            if self.name == "Hero":
                self.y -= speed
            else:
                if count_move % 2 == 0:
                    self.y -= speed


        elif func == "down" and self.y < 9 and (self.x, self.y +1) not in walls_location:
            self.update_image(image)
            if self.name == "Hero":
                self.y += speed
            else:
                if count_move % 2 == 0:
                    self.y += speed
        self.location = (self.x, self.y)


    def strike(self, opponent):
        self.fight_sound.play()
        if self.name == "Hero":
            opponent.health -= random.randint(1, 10)
        elif self.name == "Boss":
            opponent.health -= random.randint(1, 6)
        else:
            opponent.health -= random.randint(1, 5)
        if opponent.health <= 0:
            opponent.is_deleted = True
            opponent.x = 0
            opponent.y = 0

    def is_alive(self):
        if not self.is_deleted:
            return True
        else:
            return False

