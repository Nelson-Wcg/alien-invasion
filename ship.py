import pygame;


class Ship():
    def __init__(self, screen):
        """初始化飞船并设置初始位置"""
        self.screen = screen
        # 加载飞船图像病获取七外接矩形
        self.image = pygame.image.load('image/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # 将每艘飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.move_left = False
        self.move_right = False

    def update(self):
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += 1
        elif self.move_left and self.rect.left >0:
            self.rect.centerx -= 1

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
