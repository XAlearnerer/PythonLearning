
import pygame;

from settings import Settings;
from ship import Ship;
import game_functions as gf;

class AlienInvasion:
    def __init__(self):
        pygame.init();
        self.settings = Settings();
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height));
        pygame.display.set_caption("Alien Invasion");
        self.ship = Ship(self.screen,self.settings);


    def run_game(self):
        while True:
            gf.check_events(self.ship);
            # self.screen.fill(self.settings.bg_color)
            # self.ship.blitme()

            self.ship.update();
            gf.update_screen(self.settings, self.screen, self.ship);
            pygame.display.flip()


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