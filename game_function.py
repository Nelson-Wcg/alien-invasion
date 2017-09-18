import random
import sys;
import pygame;
from bullet import Bullet;
from enemy import Enemy;
from game_state import State


def check_events(ship, ai_settings, screen, bullets, center_bar, state, enemies):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        # 点击关闭按钮
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:  # 键盘按下
            check_keydown_events(ship, event, ai_settings, screen, bullets, state)
        elif event.type == pygame.KEYUP:  # 键盘抬起
            check_keyup_events(ship, event, state)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play(mouse_x, mouse_y, center_bar, state, enemies, bullets)


def check_keydown_events(ship, event, ai_settings, screen, bullets, state):
    # ESC退出游戏
    if event.key == pygame.K_ESCAPE:
        sys.exit()
    if event.key == pygame.K_RIGHT and state.game_active:
        ship.move_right = True
    if event.key == pygame.K_LEFT and state.game_active:
        ship.move_left = True
    if event.key == pygame.K_SPACE and state.game_active:
        ship.fire = True
        # fire_bullet(ship, ai_settings, screen, bullets)  # 开火


def check_keyup_events(ship, event, state):
    if event.key == pygame.K_RIGHT:
        ship.move_right = False
    elif event.key == pygame.K_LEFT:
        ship.move_left = False
    elif event.key == pygame.K_SPACE:  # 停火
        ship.fire = False


def update_screen(back_ground, screen, ship, bullets, boss_bullets, enemies, center_bar, state):
    """更新屏幕上的图像，并切换到新屏幕"""
    # screen.fill(ai_settings.bg_color)
    screen.blit(back_ground, (0, 0))

    if not state.game_active:
        center_bar.blitme()
    else:
        for enemy in enemies.sprites():  # 绘制敌机
            enemy.blitme()
    for bullet in bullets.sprites():  # 绘制子弹
        bullet.draw_bullet(screen)
    for bullet in boss_bullets.sprites():  # 绘制子弹
        bullet.draw_bullet(screen)
    state.draw_score()
    ship.blitme()  # 绘制飞船
    # 让最近绘制的屏幕可见
    pygame.display.flip()


def fire_bullet(ship, ai_settings, screen, bullets, bullet_type):
    bullet = Bullet(ai_settings, screen, ship, "ship")
    bullets.add(bullet)


def update_bullets(ship, ai_settings, screen, bullets, time_passed):
    if ship.fire and ship.fire_ticks % ship.fire_gap == 0:
        fire_bullet(ship, ai_settings, screen, bullets, "ship")
    ship.fire_ticks += ai_settings.bullet_speed_factor * time_passed

    bullets.update(time_passed)
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0 and bullet.type == "my_bullet":
            bullets.remove(bullet)
        if bullet.rect.top > screen.get_rect().height and bullet.type == "my_bullet":
            bullets.remove(bullet)


def update_enemies(screen, enemies, ship, state, ai_settings, boss_bullets, time_passed):
    if state.game_score > 0 and (state.game_score > 200) and not state.boss_alive:
        enemies.add(Enemy(ai_settings, screen, "B"))
        state.boss_alive = True
    if state.enemy_size >= ai_settings.enemy_spacing:
        state.enemy_size = 0
        next_enemy = random.randint(0, 100)
        if next_enemy > 85:
            enemy = Enemy(ai_settings, screen, "T")
            enemies.add(enemy)
        else:
            enemy = Enemy(ai_settings, screen, "L")
            enemies.add(enemy)
            # enemy_size = 0
    state.enemy_size += ai_settings.enemy_speed_factor * time_passed
    enemies.update()
    for enemy in enemies.copy():
        if enemy.rect.top > screen.get_rect().height:
            enemies.remove(enemy)
        if enemy.enemy_type == "B" and enemy.fire:  # boss机开火
            if enemy.shotgap >= 0 and enemy.shotgap % ai_settings.bullet_fire_gap == 0:
                bullet = Bullet(ai_settings, screen, enemy, "boss")
                bullet.rect.centerx = random.randint(enemy.rect.centerx - enemy.rect.width / 2,
                                                     enemy.rect.centerx + enemy.rect.width / 2)
                bullet.rect.y = 0
                boss_bullets.add(bullet)
            enemy.shotgap += time_passed
    boss_bullets.update(time_passed)
    # 飞机被撞
    ship_hit(ship, enemies, state, ai_settings, boss_bullets)


def update_collisions(bullets, enemies, boss_bullets, state):
    """子弹对撞"""
    bullet_collisions = pygame.sprite.groupcollide(bullets, boss_bullets, True, True)
    """子弹射中机体"""
    collisions = pygame.sprite.groupcollide(bullets, enemies, True, True)
    if collisions:
        for hited_enemy in collisions.values():
            for enemy in hited_enemy:
                if enemy.enemy_type == "B":
                    enemy.hited -= 1
                    if enemy.hited <= 0:
                        state.game_score += enemy.score
                    else:
                        enemies.add(enemy)
                else:
                    state.game_score += enemy.score


def check_play(mouse_x, mouse_y, center_bar, state, enemies, bullets):
    """点击开始结束按钮"""
    if not state.game_active and center_bar.rect.collidepoint(mouse_x, mouse_y):
        state.game_active = True
        state.game_score = 0
        if enemies:
            for enemy in enemies.copy():
                enemies.remove(enemy)
        if bullets:
            for bullet in bullets.copy():
                bullets.remove(bullet)


def ship_hit(ship, enemies, state, ai_settings, boss_bullets):
    """响应飞机被撞"""
    if pygame.sprite.spritecollideany(ship, enemies) or pygame.sprite.spritecollideany(ship, boss_bullets):
        state.game_active = False
        # state.game_score = 0
        ai_settings.initialize_game_setting()
        ship.fire = False
