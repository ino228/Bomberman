import pygame
from player import Player

class Game:
    done = False
    keys = []
    key = ''
    mapa = []
    walls = []
    SIZE = 50
    WIDTH = 12
    HEIGHT = 12
    grassImg = pygame.image.load("img/trava.png")
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((800, 600))
        done = False
        self.clock = pygame.time.Clock()
        self.player1 = Player(600, 0)
    def main(self):
        while not self.done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
                    self.key = 'a'
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_w:
                    self.key = 'w'
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_d:
                    self.key = 'd'
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                    self.key = 's'
                elif event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
                    self.key = "space"
                else:
                    self.key = ''
            for i in range(0, 600, 50):
                for j in range(0, 800, 50):
                    self.window.blit(self.grassImg, (j, i))
            self.player1.draw(self.window)
            self.player1.move(self.key)
            if self.key == "space":
                self.player1.pustBombu()
                self.key = ''
            pygame.display.flip()
            self.clock.tick(60)
        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.main()
