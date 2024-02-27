import pygame
import sys

from constants import *
from dvdshit import *


class Main:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("DVD FOR DANYA")
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.display = Display()

    def mainloop(self):
        screen = self.screen  # SURFACE
        while True:
            self.display.moving(screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)

            pygame.display.update()


main = Main()
main.mainloop()
