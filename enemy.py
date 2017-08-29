import random;

import pygame;
from pygame.sprite import Sprite


class Enemy(Sprite):
    """敌机"""

    def __init__(self, ai_settings, screen):
        super(Enemy, self).__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        # self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
        # ai_settings.bullet_height)
        self.image = pygame.image.load('image/enemy.bmp')
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randint(0, self.screen_rect.width)
        self.rect.top = self.screen_rect.top
        self.speed_factor = ai_settings.enemy_speed_factor
        self.y = float(self.rect.y)

    def update(self):
        self.y += self.speed_factor
        self.rect.y = self.y

    def draw_enemy(self):
        """Draw the bullet to the screen."""
        self.screen.blit(self.image, self.rect)
        #pygame.draw.rect(self.screen,  self.rect)
