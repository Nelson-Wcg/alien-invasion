import pygame;
from pygame.locals import *
from pygame.sprite import Group
from settings import Settings;
from ship import Ship;
import game_function as gf;
from center_bar import CenterBar;
from game_state import State;


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    # 创建一个游戏界面
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height), NOFRAME)  # 窗口大小
    pygame.display.set_caption("Alien Invasion")  # 窗口描述

    back_ground = pygame.image.load("image/bg3.png").convert()  # 背景
    # -+ back_ground = pygame.transform.smoothscale(back_ground, (ai_settings.screen_width, ai_settings.screen_height))

    ship = Ship(screen, ai_settings)
    bullets = Group()
    enemies = Group()
    center_bar = CenterBar(screen)
    # 游戏状态
    state = State(screen, ai_settings)
    boss_bullets = Group()
    clock = pygame.time.Clock()
    # 开始游戏主循环
    while True:
        time_passed = clock.tick()
        gf.check_events(ship, ai_settings, screen, bullets, center_bar, state, enemies)  # 检测按键操作
        if state.game_active:
            ship.update(time_passed)  # 更新飞船位置
            gf.update_bullets(ship, ai_settings, screen, bullets, time_passed)  # 更新子弹位置'
            gf.update_enemies(screen, enemies, ship, state, ai_settings, boss_bullets, time_passed)  # 更新敌机位置
            gf.update_collisions(bullets, enemies, boss_bullets, state)  # 子弹打中敌机

        gf.update_screen(back_ground, screen, ship, bullets, boss_bullets, enemies, center_bar,
                         state)  # 将所有元素绘制到画面上


run_game()
