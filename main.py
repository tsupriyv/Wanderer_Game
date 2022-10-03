import random
import pygame
from tkinter import *
from Player import Player
from Tile import Tile


IMAGE_SIZE = 75
WIDTH = 10 * IMAGE_SIZE
HEIGHT = (10 * IMAGE_SIZE)+40

root = Tk()
canvas = Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

class GameAdmin:
    def __init__(self, canvas, root):
        pygame.mixer.init()
        pygame.mixer.music.load("background.mp3")
        self.winning_sound = pygame.mixer.Sound("winning.wav")
        self.winning_sound.set_volume(.1)
        self.game_over_sound = pygame.mixer.Sound("game-over.wav")
        self.game_over_sound.set_volume(.1)
        self.root = root
        self.canvas = canvas
        self.frame = Frame(self.root)
        self.lives_frame = Frame(self.canvas)
        self.lives_frame.pack(side=TOP)
        self.dir = "images/"
        self.count_move = 1
        self.floor_location = []
        self.monsters_loc = []
        self.walls_location = [(0, 1), (1, 1), (3, 0), (6, 3), (6, 1), (3, 1), (7, 3), (7, 8), (1, 3), (1, 4), (2, 3),
                               (6, 6), (4, 3), (5, 3), (5, 1), (6, 5), (5, 5), (4, 5), (0, 6), (0, 7), (0, 8), (0, 9),
                               (1, 6), (2, 6), (2, 9), (2, 8), (4, 8), (5, 8), (8, 8), (9, 0), (9, 3), (9, 4), (9, 5),
                               (8, 5), (7, 1)]
        self.root.floor = PhotoImage(file=self.dir + "floor.png")
        self.root.wall = PhotoImage(file=self.dir + "wall.png")
        self.root.hero_down = PhotoImage(file=self.dir + "hero-down.png")
        self.root.hero_left = PhotoImage(file=self.dir + "hero-left.png")
        self.root.hero_right = PhotoImage(file=self.dir + "hero-right.png")
        self.root.hero_up = PhotoImage(file=self.dir + "hero-up.png")
        self.root.boss = PhotoImage(file=self.dir + "boss.png")
        self.root.skeleton = PhotoImage(file=self.dir + "skeleton.png")
        self.root.game_over_lost = PhotoImage(file=self.dir + "game_over_lost.png")
        self.root.game_over_won = PhotoImage(file=self.dir + "game_over_won.png")
        self.hero = Player(0, 0, self.root.hero_down, name="Hero", root=root)
        boss_location = self.__random_pos__()
        self.monsters_loc.append(boss_location)
        self.boss = Player(boss_location[0], boss_location[1], self.root.boss, name="Boss", root=root)
        skel_1_location = self.__random_pos__()
        self.monsters_loc.append(skel_1_location)
        self.skeleton_1 = Player(skel_1_location[0], skel_1_location[1], self.root.skeleton, name="Skeleton 1",
                                 root=root)
        skel_2_location = self.__random_pos__()
        self.monsters_loc.append(skel_2_location)
        self.skeleton_2 = Player(skel_2_location[0], skel_2_location[1], self.root.skeleton, name="Skeleton 2",
                                 root=root)
        skel_3_location = self.__random_pos__()
        self.monsters_loc.append(skel_3_location)
        self.skeleton_3 = Player(skel_3_location[0], skel_3_location[1], self.root.skeleton, name="Skeleton 3",
                                 root=root)
        self.game_winner = None


        self.button_1 = Button(self.frame, width=20, text="Play Again", fg="black", font=("bold", "16"), bg="light blue", command=self.play_again)
        self.button_2 = Button(self.frame, width=20, text="Exit", fg="black", font=("bold", "16"), bg="pink", command=self.root.destroy)

        self.hero_lives = Label(self.lives_frame, width=20,  fg="black", font=("bold", "16"), text=self.hero.health)
        self.hero_lives.pack(side=LEFT)

        self.monster_lives = Label(self.lives_frame, width=20,  fg="black", font=("bold", "16"), text=(self.skeleton_1.health + self.skeleton_2.health + self.skeleton_3.health + self.boss.health))
        self.monster_lives.pack(side=RIGHT)
        self.header = Frame(self.root, height=30)
        self.canvas.configure(background = "blue")
        # self.header.pack(side=TOP)


    def __random_pos__(self):
        for i in range(10):
            for j in range(10):
                if (i, j) not in self.walls_location and (i, j) != (0, 0) and (i, j) not in self.monsters_loc:
                    self.floor_location.append((i, j))
        rand_lock = random.choice(self.floor_location)
        self.floor_location.remove(rand_lock)
        return rand_lock


    def set_up_keys(self):
        self.root.bind('<Left>', self.left_key)
        self.root.bind('<Right>', self.right_key)
        self.root.bind('<Up>', self.up_key)
        self.root.bind('<Down>', self.down_key)
        self.root.bind('<space>', self.monster_strike_key)
        self.root.bind('<x>', self.hero_strike_key)
        self.root.bind('<X>', self.hero_strike_key)

    def left_key(self, event):
        self.hero.move("left", self.walls_location, self.count_move, self.root.hero_left, self.monsters_loc)
        self.boss.move("left", self.walls_location, self.count_move, self.root.boss, self.monsters_loc)
        self.skeleton_1.move("left", self.walls_location, self.count_move, self.root.skeleton, self.monsters_loc)
        self.skeleton_2.move("left", self.walls_location, self.count_move, self.root.skeleton, self.monsters_loc)
        self.skeleton_3.move("left", self.walls_location, self.count_move, self.root.skeleton, self.monsters_loc)
        self.count_move += 1

    def right_key(self, event):
        self.hero.move("right", self.walls_location, self.count_move, self.root.hero_right, self.monsters_loc)
        self.boss.move("right", self.walls_location, self.count_move, self.root.boss, self.monsters_loc)
        self.skeleton_1.move("right", self.walls_location, self.count_move, self.root.skeleton, self.monsters_loc)
        self.skeleton_2.move("right", self.walls_location, self.count_move, self.root.skeleton, self.monsters_loc)
        self.skeleton_3.move("right", self.walls_location, self.count_move, self.root.skeleton, self.monsters_loc)
        self.count_move += 1

    def up_key(self, event):
        self.hero.move("up", self.walls_location, self.count_move, self.root.hero_up, self.monsters_loc)
        self.boss.move("up", self.walls_location, self.count_move, self.root.boss, self.monsters_loc)
        self.skeleton_1.move("up", self.walls_location, self.count_move, self.root.skeleton, self.monsters_loc)
        self.skeleton_2.move("up", self.walls_location, self.count_move, self.root.skeleton, self.monsters_loc)
        self.skeleton_3.move("up", self.walls_location, self.count_move, self.root.skeleton, self.monsters_loc)
        self.count_move += 1

    def down_key(self, event):
        self.hero.move("down", self.walls_location, self.count_move, self.root.hero_down, self.monsters_loc)
        self.boss.move("down", self.walls_location, self.count_move, self.root.boss, self.monsters_loc)
        self.skeleton_1.move("down", self.walls_location, self.count_move, self.root.skeleton, self.monsters_loc)
        self.skeleton_2.move("down", self.walls_location, self.count_move, self.root.skeleton, self.monsters_loc)
        self.skeleton_3.move("down", self.walls_location, self.count_move, self.root.skeleton, self.monsters_loc)
        self.count_move += 1

    def monster_strike_key(self, event):
        if self.hero.location == self.boss.location and self.boss.is_alive():
            i = 0
            if self.hero.is_alive() and self.boss.is_alive():
                self.boss.strike(self.hero)
            elif self.hero.is_alive():
                self.boss.delete(self.canvas, self.hero)
            elif self.boss.is_alive():
                self.hero.delete(self.canvas)
            print("boss", self.hero.health, self.boss.health)

        elif self.hero.location == self.skeleton_1.location and self.skeleton_1.is_alive():
            i = 0
            if self.hero.is_alive() and self.skeleton_1.is_alive():
                self.skeleton_1.strike(self.hero)
            elif self.hero.is_alive():
                self.skeleton_1.delete(self.canvas, self.hero)
            elif self.skeleton_1.is_alive():
                self.hero.delete(self.canvas)
            print("s1", self.hero.health, self.skeleton_1.health)


        elif self.hero.location == self.skeleton_2.location and self.skeleton_2.is_alive():
            i = 0
            if self.hero.is_alive() and self.skeleton_2.is_alive():
                self.skeleton_2.strike(self.hero)
            elif self.hero.is_alive():
                self.skeleton_2.delete(self.canvas, self.hero)
            elif self.skeleton_2.is_alive():
                self.hero.delete(self.canvas)
            print("s2", self.hero.health, self.skeleton_2.health)


        elif self.hero.location == self.skeleton_3.location and self.skeleton_3.is_alive():
            i = 0
            if self.hero.is_alive() and self.skeleton_3.is_alive():
                self.skeleton_3.strike(self.hero)
            elif self.hero.is_alive():
                self.skeleton_3.delete(self.canvas, self.hero)
            elif self.skeleton_3.is_alive():
                self.hero.delete(self.canvas)
            print("s3", self.hero.health, self.skeleton_3.health)

    def hero_strike_key(self, event):
        if self.hero.location == self.boss.location:
            i = 0
            if self.hero.is_alive() and self.boss.is_alive():
                self.hero.strike(self.boss)
            elif self.hero.is_alive():
                self.boss.delete(self.canvas, self.hero)
            elif self.boss.is_alive():
                self.hero.delete(self.canvas)
            print("boss", self.hero.health, self.boss.health)

        elif self.hero.location == self.skeleton_1.location:
            i = 0
            if self.hero.is_alive() and self.skeleton_1.is_alive():
                self.hero.strike(self.skeleton_1)
            elif self.hero.is_alive():
                self.skeleton_1.delete(self.canvas, self.hero)
            elif self.skeleton_1.is_alive():
                self.hero.delete(self.canvas)
            print("s1", self.hero.health, self.skeleton_1.health)


        elif self.hero.location == self.skeleton_2.location:
            i = 0
            if self.hero.is_alive() and self.skeleton_2.is_alive():
                self.hero.strike(self.skeleton_2)
            elif self.hero.is_alive():
                self.skeleton_2.delete(self.canvas, self.hero)
            elif self.skeleton_2.is_alive():
                self.hero.delete(self.canvas)
            print("s2", self.hero.health, self.skeleton_2.health)


        elif self.hero.location == self.skeleton_3.location:
            i = 0
            if self.hero.is_alive() and self.skeleton_3.is_alive():
                self.hero.strike(self.skeleton_3)
            elif self.hero.is_alive():
                self.skeleton_3.delete(self.canvas, self.hero)
            elif self.skeleton_3.is_alive():
                self.hero.delete(self.canvas)
            print("s3", self.hero.health, self.skeleton_3.health)


    def draw_map(self):
        for x in range(10):
            for y in range(10):
                if (x, y) not in self.walls_location:
                    tile = Tile(x * 75, (y * 75)+40, self.root.floor)
                    tile.create_tile(self.canvas)
                else:
                    tile = Tile(x * 75, (y * 75)+40, self.root.wall)
                    tile.create_tile(self.canvas)
            y = 0

    def create_players(self):
        self.hero.create_player(self.canvas)
        self.skeleton_1.create_player(self.canvas)
        self.skeleton_2.create_player(self.canvas)
        self.skeleton_3.create_player(self.canvas)
        self.boss.create_player(self.canvas)

    def is_game_over(self):
        if self.hero.is_alive() and (not self.boss.is_alive() and not self.skeleton_1.is_alive() and not self.skeleton_2.is_alive() and not self.skeleton_3.is_alive()):
            pygame.mixer.music.stop()
            self.game_over_window()
            self.winning_sound.play()
            self.winning_sound.stop()
            game_over=True
            self.game_winner = "hero"
        elif not self.hero.is_alive() and (self.boss.is_alive() or self.skeleton_1.is_alive() or self.skeleton_2.is_alive() or self.skeleton_3.is_alive()):
            print(not self.hero.is_alive())
            print((self.boss.is_alive() or self.skeleton_1.is_alive() or self.skeleton_2.is_alive() or self.skeleton_3.is_alive()))
            pygame.mixer.music.stop()
            self.game_over_sound.play()
            self.game_over_sound.stop()
            game_over=True
            self.game_winner = "monster"
        else:
            game_over=False
        return game_over

    def play_again(self):
        self.frame.destroy()
        self.canvas.delete("all")
        main()


    def game_over_window(self):
        if self.game_winner == "hero":
            self.canvas.create_image(0, 0, image=self.root.game_over_won, anchor=NW)
            self.winning_sound.play()
        else:
            self.frame.pack()
            self.button_1.pack(side=LEFT, ipadx=40, ipady=20)
            self.button_2.pack(side=RIGHT, ipadx=40, ipady=20)
            self.canvas.create_image(0, 0, image=self.root.game_over_lost, anchor=NW)
            self.game_over_sound.play()




def main():
    game = GameAdmin(canvas, root)
    game.set_up_keys()
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(.02)

    is_game_over=False
    while True:
        game.root.title("Wanderer Game")

        if not is_game_over:
            game.lives_frame.destroy()
            game.lives_frame = Frame(game.root)
            game.hero_lives = Label(game.lives_frame, width=20,  fg="black", font=("bold", "16"), text=game.hero.health)
            game.hero_lives.pack(side=LEFT)
            game.monster_lives = Label(game.lives_frame, width=20,  fg="black", font=("bold", "16"), text=game.skeleton_1.health + game.skeleton_2.health + game.skeleton_3.health + game.boss.health)
            game.monster_lives.pack(side=RIGHT)
            game.draw_map()

            if not game.is_game_over():
                game.lives_frame.pack()
                game.create_players()
            else:
                game.lives_frame.pack()
                game.game_over_window()
                is_game_over=True
        root.update_idletasks()
        root.update()
if __name__ == '__main__':
    main()
    root.mainloop()

