import pygame;


class Ship():
    def __init__(self, screen, ai_setting):
        self.screen = screen;
        self.screen_rect = screen.get_rect();

        # 加载飞船图像 并获取其外接矩阵
        self.image = pygame.image.load("pictures//ship.jpg");
        self.rect = self.image.get_rect();

        # 将飞船放置在底部
        # self.rect.centerx = self.screen_rect.centerx;
        # self.rect.bottom = self.screen_rect.bottom;
        self.rect.midbottom = self.screen_rect.midbottom;

        self.moving_right = False;
        self.moving_left = False;

        self.center = float(self.rect.centerx);
        self.ship_speed = ai_setting.ship_speed;

    def update(self):
        # if self.moving_right:
        #     self.rect.centerx += 1;
        # if self.moving_left:
        #     self.rect.centerx -= 1;
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ship_speed;
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.center -= self.ship_speed;
        self.rect.centerx = self.center;

    def blitme(self):
        # 在指定位置放置飞船
        self.screen.blit(self.image, self.rect);
        #pygame.display.flip();
