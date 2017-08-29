class Settings():
    def __init__(self):
        """初始化游戏设置"""
        self.screen_width = 500
        self.screen_height = 700
        self.bg_color = (255, 255, 255)

        self.bullet_width = 2
        self.bullet_height = 5
        self.bullet_color = (60, 60, 60)
        self.bullet_speed_factor = 1

        self.enemy_speed_factor = 0.5
