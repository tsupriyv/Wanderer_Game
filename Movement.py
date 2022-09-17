class Movement:
    def __init__(self, player):
        self.player = player

    def left(self, event):
        self.player.move()
        print("left M")
        print(self.player.x)
