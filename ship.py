import pygame

class Ship:
    """A class to manage the ship"""

    def __init__(self, ai_game):
        """Initiallize the ship and set its starting position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.Settings = ai_game.Settings

        # load ship img and its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()


        #start each new ship at the bottom center screen
        self.rect.midbottom = self.screen_rect.midbottom

        # store decimal value for the ship's horizontal position
        self.x = float(self.rect.x)

        self.moving_right = False
        self.moving_left = False


    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.Settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.Settings.ship_speed

        # update rect object from self.x
        self.rect.x = self.x


    def blitme(self):
        """Draw ship at its current location"""
        self.screen.blit(self.image, self.rect)
