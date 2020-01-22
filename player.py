import pygame
from bomb import Bomb


class Player:
    x = 0
    y = 0
    size = 50
    isBomb = False
    count_bomb = 2
    bombs = []
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self, key):
        if key == 'a':
            self.x -= 10
        if key == 'd':
            self.x += 10
        if key == 'w':
            self.y -= 10
        if key == 's':
            self.y += 10
    def draw(self, window):
        for i in self.bombs:
            print(self.bombs)
            i.draw(window)
            vybuchnuta = i.vybuch()
            if vybuchnuta:
                self.bombs.remove(i)
        pygame.draw.rect(window, (0, 0, 255), [self.x, self.y, self.size, self.size])
    def pustBombu(self):
        if len(self.bombs) < self.count_bomb:
            bomb = Bomb(self.x, self.y, pygame.time.get_ticks() / 1000)
            self.bombs.append(bomb)

