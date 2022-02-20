from pygame import Rect

class Card(Rect):
    def __init__(self, left, top, width, height, number):
        super().__init__(left, top, width, height)
        self.number = number
        self.moving = False