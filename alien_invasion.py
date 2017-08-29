import pygame;
from pygame.sprite import Group
from settings import Settings;
from ship import Ship;
from enemy import Enemy;
import game_function as gf;


def run_game():
    enemy_size = 0
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    # 创建一个游戏界面
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # 创建一艘飞船
    ship = Ship(screen)
    bullets = Group()
    enemies = Group()
    # 开始游戏主循环
    while True:
        enemy_size += 1
        flag = enemy_size >= 50
        if flag:
            enemy_size = 0
        gf.check_events(ship, ai_settings, screen, bullets)
        ship.update()
        gf.update_enemies(ai_settings, enemies, flag, screen)
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, bullets, enemies)


run_game()
