import random;

import pygame;
from pygame.sprite import Sprite


class Enemy(Sprite):
    """敌机"""

    def __init__(self, ai_settings, screen, enemy_type):
        super(Enemy, self).__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        # self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
        # ai_settings.bullet_height)
        self.enemy_type = enemy_type;
        if self.enemy_type == "T":
            self.image = pygame.image.load('image/enemy_small.png').convert_alpha()
            self.score = 5
        elif self.enemy_type == "L":
            self.image = pygame.image.load('image/enemy.png').convert_alpha()
            self.score = 10
        elif self.enemy_type == "B":
            self.image = pygame.image.load('image/boss.png').convert_alpha()
            self.score = 500
            self.hited = 50
            self.shotgap = 0
            self.fire = False
        # self.image = pygame.transform.smoothscale(self.image, (50, 50))  # 缩小图片
        self.rect = self.image.get_rect()
        if self.enemy_type == "B":
            self.rect.bottom = 0
            self.rect.centerx = self.screen_rect.width / 2
        else:
            self.rect.centerx = random.randint(int(self.rect.width / 2), self.screen_rect.width - int(self.rect.width))
            self.rect.bottom = 0
        self.speed_factor = float(ai_settings.enemy_speed_factor)
        self.y = float(self.rect.y)

    def update(self):
        # 判断不同敌机不同运动方式
        # print("self.speed_factor"+ str(self.speed_factor))
        self.speed_factor = float(self.ai_settings.enemy_speed_factor)
        if self.enemy_type == "T":
            self.y += self.speed_factor + 0.5
        elif self.enemy_type == "L":
            self.y += self.speed_factor
        elif self.enemy_type == "B":
            if self.rect.bottom < self.rect.height:
                self.y += self.speed_factor / 2
            else:
                self.fire = True
        self.rect.y = self.y

    def blitme(self):
        """Draw the bullet to the screen."""
        self.screen.blit(self.image, self.rect)
