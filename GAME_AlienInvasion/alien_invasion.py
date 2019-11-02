import pygame;

from settings import Settings;
from ship import Ship;
import game_functions as gf;

from pygame.sprite import Group;

from alien import Alien;


class AlienInvasion:
    def __init__(self):
        pygame.init();
        self.settings = Settings();
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height));
        pygame.display.set_caption("Alien Invasion");
        self.ship = Ship(self.screen, self.settings);

        self.bullets = Group();
        self.aliens = Group();
        gf.create_fleet(self.settings,self.screen,self.ship,self.aliens);


    def run_game(self):
        # alien=Alien(self.settings,self.screen);
        while True:
            gf.check_events(self.settings, self.screen, self.ship, self.bullets);
            # self.screen.fill(self.settings.bg_color)
            # self.ship.blitme()
            self.ship.update();

            gf.update_bullet(self.settings, self.screen, self.ship, self.bullets, self.aliens);
            gf.update_aliens(self.settings,self.aliens);

            gf.update_screen(self.settings, self.screen, self.ship, self.bullets, self.aliens);
            # pygame.display.flip()


# Make a game instance, and run the game.
ai = AlienInvasion()
ai.run_game()

# mysetting = Settings();
# myscreen = pygame.display.set_mode((mysetting.screen_width,mysetting.screen_height));
# myship=Ship(myscreen);
#
# def run_game():
#     while True:
#         gf.check_events();
#         gf.update_screen(mysetting,myscreen,myship);
#
# run_game();
