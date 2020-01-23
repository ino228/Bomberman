import pygame

class Wall:
    x = 0
    y = 0
    breakable = False
    wallImg = None
    def __init__(self, x, y, breakable):
        self.x = x
        self.y = y
        self.breakable = breakable
        self.wallImg = pygame.image.load("img/mur.png")
    def draw(self, window):
        window.blit(self.wallImg, (self.x, self.y))