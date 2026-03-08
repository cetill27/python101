import sys

import pygame

from ship import Ship
from settings import Settings

class AlienInvasion:
    """Overall class to manage game assets and behaviour"""
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings  = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship =Ship(self)

      
        
    def run_game(self):
        """Start the main loop for the game """
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
            self.clock.tick(60)
        #Make the most revently drawn screen visible
            pygame.display.flip()

            
    def _check_events(self):
        #Watch for keyaboard and mouse events
         for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type ==pygame.KEYDOWN:
                if event.key ==pygame.K_RIGHT:
                    self.ship.moving_right = True
                elif event.type == pygame.KEYUP:
                    if event.key==pygame.K_RIGHT:
                        self.ship.moving_right = False


    def _update_screen(self):
         #Redraw the screen during each pass through the loop
            self.screen.fill(self.settings.bg_color)       
            self.ship.blitme() 
            

if __name__ =='__main__':
    #Make a game instance , and run the game 
    ai  =AlienInvasion()
    ai.run_game() 