import pygame

class Bomb:
    x = 0
    y = 0
    r = 0
    time_duration = 3
    time_start = 0
    def __init__(self, x, y, seconds):
        self.x = x
        self.y = y
        self.r = 25
        self.time_start = seconds
        self.bomb = pygame.image.load("img/bomba.png")
        self.bomb = pygame.transform.scale(self.bomb, (50, 50))
    def draw(self, window):
        window.blit(self.bomb, (self.x, self.y))
    def vybuch(self):
        if self.time_start + self.time_duration < pygame.time.get_ticks() / 1000:
            return True
        else:
            return False
