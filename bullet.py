import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """
    Class that manages the bullets
    Inherits from the pygame.sprite module
    """

    def __init__(self, ai_game):
        """ Create a bullet fired from the ship """
        super().__init__()
        self.screen = ai_game.screen
        self.Settings = ai_game.Settings
        self.color = self.Settings.bullet_color

        # create bullet rect at (0, 0) and then set the correct position
        self.rect = pygame.Rect(0, 0, self.Settings.bullet_width, self.Settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # Store the bullet's position as a decimal value
        self.y = float(self.rect.y)

    def update(self):
        """ Move the bullet up the screen"""
        # update the decimal position of the bullet
        self.y -= self.Settings.bullet_speed
        # update the rect position
        self.rect.y = self.y

    def draw_bullet(self):
        """ Draw the bullet to the screen """

        pygame.draw.rect(self.screen, self.color, self.rect)
