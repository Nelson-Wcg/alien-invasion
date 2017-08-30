import pygame;
from pygame.sprite import Group
from settings import Settings;
from ship import Ship;
import game_function as gf;
from game_time import GameTime;


def run_game():
    enemy_size = 0
    bullet_size = 0
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    # 创建一个游戏界面
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # 创建一艘飞船
    ship = Ship(screen, ai_settings)
    bullets = Group()
    enemies = Group()
    # 游戏开始
    time = GameTime(screen)
    # 开始游戏主循环
    while True:
        # 生成敌机的间隔
        enemy_flag = enemy_size >= ai_settings.enemy_spacing
        if enemy_flag:
            enemy_size = 0
        enemy_size += ai_settings.enemy_speed_factor

        gf.check_events(ship, ai_settings, screen, bullets, time)  # 检测按键操作
        ship.update()  # 更新飞船位置
        gf.update_enemies(ai_settings, enemies, enemy_flag, screen)  # 更新敌机位置
        gf.update_bullets(ship, ai_settings, screen, bullets)  # 更新子弹位置
        gf.update_collisions(bullets, enemies)  # 子弹打中敌机

        gf.update_screen(ai_settings, screen, ship, bullets, enemies, time)  # 将所有元素绘制到画面上


run_game()
