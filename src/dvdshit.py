
import pygame
import os

from constants import *


class Display:
    def __init__(self):
        self.x = X_START
        self.y = Y_START
        self.x_sp = X_SPEED
        self.y_sp = Y_SPEED

    @staticmethod
    def show_something(surface: pygame.Surface):
        rect = (HEIGHT, WIDTH, HEIGHT, WIDTH)
        color = (200, 200, 200)
        pygame.draw.rect(surface, color, rect)

    @staticmethod
    def update_blit(surface: pygame.Surface, x, y):
        path = os.path.join(f"image/shit.png")
        img = pygame.image.load(path)

        # img_center = x, y

        surface.blit(img, (x, y))

    def moving(self, surface: pygame.Surface):
        """
        Move picture on some walk.
        :param surface: screen
        """
        x2 = self.x + self.x_sp
        y2 = self.y + self.y_sp

        self.x, self.y = x2, y2

        if not (0 <= x2 <= WIDTH - 320):
            self.x_sp = -self.x_sp

        if not (0 <= y2 <= HEIGHT - 210):
            self.y_sp = -self.y_sp

        self.update_blit(surface, x2, y2)

