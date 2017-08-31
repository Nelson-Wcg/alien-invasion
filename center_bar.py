import pygame;
from pygame.locals import *;


class CenterBar():
    white = 255, 255, 255
    blue = 0, 0, 200

    def __init__(self, screen):
        self.screen = screen
        myfont = pygame.font.Font(None, 60)
        self.play_image = myfont.render("play", True, self.blue)
        self.rect = self.play_image.get_rect()
        self.rect.center = self.screen.get_rect().center
        self.show = False

    def blitme(self):
        self.screen.blit(self.play_image, self.rect)

    def click(self):
        pass
