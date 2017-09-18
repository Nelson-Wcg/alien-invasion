import pygame;


class State():
    def __init__(self, screen, ai_settings):
        self.game_active = False
        self.boss_alive = False
        self.game_score = 0  # 得分
        self.enemy_size = 0
        self.ai_settings = ai_settings
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

    def draw_score(self):
        self.score_image = self.font.render(str(self.game_score), True, self.text_color,
                                            self.ai_settings.bg_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen.get_rect().width - self.ai_settings.top_bar
        self.score_rect.top = self.ai_settings.top_bar
        self.screen.blit(self.score_image, self.score_rect)
