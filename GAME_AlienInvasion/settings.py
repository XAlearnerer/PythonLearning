class Settings():
    # 屏幕设置
    def __init__(self):
        self.screen_width = 1200;
        self.screen_height = 800;
        # self.bg_color = (230, 230, 230);
        self.bg_color = (250, 250, 250);
        self.ship_speed = 1.5;

        self.bullet_speed = 1;

        self.bullet_width = 3;
        #self.bullet_width = 3000;
        self.bullet_height = 15;
        self.bullet_color = (60, 60, 60);
        self.bullet_allowed = 3;

        # aliens 右移速度
        self.alien_speed = 0.3;
        # aliens 下移速度
        self.alien_drop_speed = 15;
        # aliens 移动方向
        self.fleet_direction = 1;
