import sys;
import pygame;
from bullet import Bullet;
from enemy import Enemy;


def check_events(ship, ai_settings, screen, bullets, time):
    """响应按键和鼠标事件"""
    time.prep_time(ai_settings)
    for event in pygame.event.get():
        # 点击关闭按钮
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:  # 键盘按下
            check_keydown_events(ship, event, ai_settings, screen, bullets)
        elif event.type == pygame.KEYUP:  # 键盘抬起
            check_keyup_events(ship, event)


def check_keydown_events(ship, event, ai_settings, screen, bullets):
    # ESC退出游戏
    if event.key == pygame.K_ESCAPE:
        sys.exit()
    if event.key == pygame.K_RIGHT:
        ship.move_right = True
    if event.key == pygame.K_LEFT:
        ship.move_left = True
    if event.key == pygame.K_SPACE:
        ship.fire = True
        # fire_bullet(ship, ai_settings, screen, bullets)  # 开火


def check_keyup_events(ship, event):
    if event.key == pygame.K_RIGHT:
        ship.move_right = False
    elif event.key == pygame.K_LEFT:
        ship.move_left = False
    elif event.key == pygame.K_SPACE:  # 停火
        ship.fire = False


def update_screen(ai_settings, screen, ship, bullets, enemies, time):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环都重绘屏幕
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    for enemy in enemies.sprites():
        enemy.draw_enemy()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    time.draw(screen)
    # 让最近绘制的屏幕可见
    pygame.display.flip()


def fire_bullet(ship, ai_settings, screen, bullets):
    bullet = Bullet(ai_settings, screen, ship)
    bullets.add(bullet)


def update_bullets(ship, ai_settings, screen, bullets):
    print("ticks:"+str(ship.fire_ticks)+"  gap:"+str(ship.fire_gap)+"  bullet_speed:"+str(ai_settings.bullet_speed_factor))
    if ship.fire and ship.fire_ticks % ship.fire_gap==0:
        fire_bullet(ship, ai_settings, screen, bullets)
    ship.fire_ticks += ai_settings.bullet_speed_factor

    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def update_enemies(ai_settings, enemies, flag, screen):
    if flag:
        enemy = Enemy(ai_settings, screen)
        enemies.add(enemy)
        enemy_size = 0
    enemies.update()
    for enemy in enemies.copy():
        if enemy.rect.top > screen.get_rect().height:
            enemies.remove(enemy)


def update_collisions(bullets, enemies):
    """子弹射中机体"""
    collisions = pygame.sprite.groupcollide(bullets, enemies, True, True)
