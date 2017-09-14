import pygame;
from pygame.sprite import Sprite


class Bullet(Sprite):
    """子弹"""

    def __init__(self, ai_settings, screen, ship, shooter):
        super().__init__()
        if shooter == "ship":
            self.image = pygame.image.load('image/my_bollet.png').convert_alpha()
            self.type = "my_bullet"
        else:
            self.image = pygame.image.load('image/enemy_bollet.png').convert_alpha()
            self.type = "enemy_bullet"

        self.screen = screen
        # self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
                             #   ai_settings.bullet_height)
        self.rect = self.image.get_rect()
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.rect.y = ship.rect.y
        self.y = float(self.rect.y)
        # self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        if self.type == "my_bullet":
            self.y -= self.speed_factor
            self.rect.y = self.y
        elif self.type == "enemy_bullet":
            self.y += self.speed_factor
            self.rect.y = self.y

    def draw_bullet(self, screen):
        """Draw the bullet to the screen."""
        screen.blit(self.image, self.rect)
        # pygame.draw.rect(self.screen, self.color, self.rect)
