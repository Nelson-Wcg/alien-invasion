class Settings():
    def __init__(self):
        """初始化游戏设置"""
        self.screen_width = 500
        self.screen_height = 700
        self.bg_color = (255, 255, 255)

        self.bullet_width = 3
        self.bullet_height = 7
        self.bullet_color = (60, 60, 60)
        self.bullet_speed_factor = 1  # 子弹速度
        self.bullet_fire_gap = 100  # 子弹间隔

        self.enemy_speed_factor = 0.5  # 敌机下落速度
        self.enemy_spacing = 100  # 敌机垂直间距

        self.top_bar = 10
