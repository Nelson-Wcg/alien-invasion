import time;
import pygame;


class GameTime():
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        self.begin_time = 0
        self.ticks = int(time.time())
        self.time_image = None
        self.time_rect = None
        self.flag = 100  # 加快游戏进程间隔

    def prep_time(self, ai_settings):
        """时间格式化"""
        if self.begin_time == 0:
            self.begin_time = self.ticks
        self.ticks = int(time.time())
        game_time = self.ticks - self.begin_time
        self.time_image = self.font.render(str(game_time), True, self.text_color,
                                           ai_settings.bg_color)
        self.time_rect = self.time_image.get_rect()
        self.time_rect.right = self.screen.get_rect().width - ai_settings.top_bar
        self.time_rect.top = ai_settings.top_bar
        # 每隔100秒速度提升
        if game_time > 0 and game_time % self.flag == 0:
            ai_settings.enemy_speed_factor += (ai_settings.enemy_speed_factor * 0.5)
            self.flag = self.flag * 2

    def draw(self, screen):
        self.screen.blit(self.time_image, self.time_rect)
