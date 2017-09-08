import pygame;
from pygame.sprite import Group
from settings import Settings;
from ship import Ship;
import game_function as gf;
from game_time import GameTime;
from center_bar import CenterBar;
from game_state import State;


def run_game():
    enemy_size = 0
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    # 创建一个游戏界面
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))  # 窗口大小
    pygame.display.set_caption("Alien Invasion")  # 窗口描述

    back_ground = pygame.image.load("image/bg3.png").convert_alpha()  # 背景
    back_ground = pygame.transform.smoothscale(back_ground, (ai_settings.screen_width, ai_settings.screen_height))

    ship = Ship(screen, ai_settings)
    bullets = Group()
    enemies = Group()
    print("enemiesc" + str(enemies))
    center_bar = CenterBar(screen)
    # 游戏开始
    time = GameTime(screen)
    # 游戏状态
    state = State()
    # 开始游戏主循环
    while True:
        gf.check_events(ship, ai_settings, screen, bullets, time, center_bar, state, enemies)  # 检测按键操作
        if state.game_active:
            # 生成敌机的间隔
            enemy_flag = enemy_size >= ai_settings.enemy_spacing
            if enemy_flag:
                enemy_size = 0
            enemy_size += ai_settings.enemy_speed_factor

            ship.update()  # 更新飞船位置
            gf.update_bullets(ship, ai_settings, screen, bullets)  # 更新子弹位置'
            gf.update_enemies(ai_settings, screen, enemies, ship, enemy_flag, state)  # 更新敌机位置
            gf.update_collisions(bullets, enemies)  # 子弹打中敌机

        gf.update_screen(back_ground, ai_settings, screen, ship, bullets, enemies, time, center_bar,
                         state)  # 将所有元素绘制到画面上


run_game()
