import sys;
import pygame;
from bullet import Bullet;


def check_events(ship, ai_settings, screen, bullets):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        # 点击关闭按钮
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:  # 键盘按下
            check_keydown_events(ship, event, ai_settings, screen, bullets)
        elif event.type == pygame.KEYUP:  # 键盘抬起
            check_keyup_events(ship, event)


def check_keydown_events(ship, event, ai_settings, screen, bullets):
    if event.key == pygame.K_RIGHT:
        ship.move_right = True
    elif event.key == pygame.K_LEFT:
        ship.move_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ship, event, ai_settings, screen, bullets)


def check_keyup_events(ship, event):
    if event.key == pygame.K_RIGHT:
        ship.move_right = False
    elif event.key == pygame.K_LEFT:
        ship.move_left = False


def update_screen(ai_settings, screen, ship, bullets):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环都重绘屏幕
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # 让最近绘制的屏幕可见
    pygame.display.flip()


def fire_bullet(ship, event, ai_settings, screen, bullets):
    bullet = Bullet(ai_settings, screen, ship)
    bullets.add(bullet)


def update_bullets(bullets):
    bullets.update()
