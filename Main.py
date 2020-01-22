import pygame
from player import Player

class Game:
    done = False
    keys = []
    key = ''
    mapa = []
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((800, 600))
        done = False
        self.clock = pygame.time.Clock()
        self.player1 = Player(600, 0)

    def main(self):
        time_seconds = pygame.time.get_ticks() / 1000
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
            self.window.fill((255, 255, 255))
            self.player1.draw(self.window)
            self.player1.move(self.key)
            if self.key == "space":
                self.player1.pustBombu()
                self.key = ''
            pygame.display.flip()
            self.clock.tick(30)
        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.main()
