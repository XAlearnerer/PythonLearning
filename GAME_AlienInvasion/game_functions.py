import sys;
import pygame;

def check_keydown(event,ship):
    if event.key == pygame.K_RIGHT:
        # ship.rect.centerx += 1;
        ship.moving_right = True;
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True;

def check_keyup(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False;
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False;

def check_events(ship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit();
        elif event.type == pygame.KEYDOWN:
            # if event.key == pygame.K_RIGHT:
            #     # ship.rect.centerx += 1;
            #     ship.moving_right = True;
            # elif event.key == pygame.K_LEFT:
            #     ship.moving_left = True;
            check_keydown(event,ship);
        elif event.type == pygame.KEYUP:
            # if event.key == pygame.K_RIGHT:
            #     ship.moving_right = False;
            # elif event.key == pygame.K_LEFT:
            #     ship.moving_left = False;
            check_keyup(event, ship);


def update_screen(ai_setting, screen, ship):
    screen.fill(ai_setting.bg_color);
    ship.blitme();
    # 让最近绘制的屏幕显示
    pygame.display.flip();
