import sys
import pygame
from Settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
    """ Overall class to manage game assets and behavior"""

    def __init__(self):
        """ INitializing the game and creating game resources"""

        pygame.init()
        self.Settings = Settings()

        self.screen = pygame.display.set_mode((self.Settings.screen_width, self.Settings.screen_height))
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.Settings.screen_width = self.screen.get_rect().width
        self.Settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasions")
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        """ Start main game loop for the game"""
        while True:
            #watch for keyboard events and mouse events
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)


    def _check_keydown_events(self, event):
            if event.key == pygame.K_RIGHT:
                self.ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                self.ship.moving_left = True
            elif event.key == pygame.K_q:
                sys.exit()
            elif event.key == pygame.K_SPACE:
                self._fire_bullet()


    def _check_keyup_events(self, event):
            if event.key == pygame.K_RIGHT:
                self.ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                self.ship.moving_left = False




    def _fire_bullet(self):
        """ Create a new bullet and add it to the bullets group"""
        if len(self.bullets) < self.Settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_screen(self):
        self.screen.fill(self.Settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        # make then most recently drawn screen available
        pygame.display.flip()

    def _update_bullets(self):
        """ Update position of the bullets and get rid of old bullets"""
        # update bullet positions
        self.bullets.update()

        # get rid of bullets that have disappered
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

if __name__ == '__main__':
    # make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()