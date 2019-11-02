import sys;
import pygame;

from bullet import Bullet
from alien import Alien


def check_keydown(event, ai_setting, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        # ship.rect.centerx += 1;
        ship.moving_right = True;
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True;
    elif event.key == pygame.K_SPACE:
        if len(bullets) < ai_setting.bullet_allowed:
            new_bullet = Bullet(ai_setting, screen, ship);
            bullets.add(new_bullet);


def check_keyup(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False;
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False;


def check_events(ai_setting, screen, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit();
        elif event.type == pygame.KEYDOWN:
            # if event.key == pygame.K_RIGHT:
            #     # ship.rect.centerx += 1;
            #     ship.moving_right = True;
            # elif event.key == pygame.K_LEFT:
            #     ship.moving_left = True;
            check_keydown(event, ai_setting, screen, ship, bullets);

        elif event.type == pygame.KEYUP:
            # if event.key == pygame.K_RIGHT:
            #     ship.moving_right = False;
            # elif event.key == pygame.K_LEFT:
            #     ship.moving_left = False;
            check_keyup(event, ship);


def update_screen(ai_setting, screen, ship, bullets, aliens):
    screen.fill(ai_setting.bg_color);
    ship.blitme();

    # aliens.blieme();
    aliens.draw(screen);

    for bullet in bullets:
        bullet.draw_bullet();

    # 让最近绘制的屏幕显示
    pygame.display.flip();


def update_bullet(ai_setting, screen, ship, bullets, aliens):
    # 使用的是 Group类型的bullets， 所以要重载 update() 函数
    bullets.update();
    # 删除消失的子弹
    for bull in bullets:
        if bull.rect.bottom <= 0:
            bullets.remove(bull);
    # print(len(self.bullets));

    # 检查重叠 有子弹击中外星人后 删除相应子弹与外星人
    collisions=pygame.sprite.groupcollide(bullets,aliens,True,True);

    if len(aliens)==0:
        bullets.empty();
        create_fleet(ai_setting, screen, ship, aliens);


def get_number_rows(ai_settings, ship_height, alien_height):
    available_space_y = (ai_settings.screen_height - (5 * alien_height) - ship_height);
    number_rows = int(available_space_y / (2 * alien_height));
    return number_rows;


def get_number_aliens_x(ai_settings, alien_width):
    available_space_x = ai_settings.screen_width - 2 * alien_width;
    number_aliens_x = int(available_space_x / (2 * alien_width));
    return number_aliens_x;


def create_alien(ai_settings, screen, aliens, ali_number, row_number):
    alien = Alien(ai_settings, screen);
    alien_width = alien.rect.width;
    alien.x = alien_width + 2 * alien_width * ali_number;
    alien.rect.x = alien.x;
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number;
    aliens.add(alien);


def create_fleet(ai_settings, screen, ship, aliens):
    alien = Alien(ai_settings, screen);
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width);
    row_number = get_number_rows(ai_settings, ship.rect.height, alien.rect.height);

    for rnum in range(row_number):
        for ali_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, ali_number, rnum);


def check_fleet_edges(ai_settings, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_edges(ai_settings, aliens);
            break;


def change_fleet_edges(ai_settings, aliens):
    # 使aliens下降 并 更改方向
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.alien_drop_speed;

    ai_settings.fleet_direction *= -1;


def update_aliens(ai_settings, aliens):
    check_fleet_edges(ai_settings, aliens);
    aliens.update();



