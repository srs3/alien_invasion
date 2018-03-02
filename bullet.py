import pygame
from pygame.sprite import Sprite

#using sprite enables you to group related elements in your game and act on all the grouped elements at once

class Bullet(Sprite):
    """ A class to manage bullets fired from the ship"""

    def __init__(self, ai_settings, screen, ship):
        super().__init__()
        self.screen = screen

        # bullet is created at (0,0) and then set to the correct position
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # store the bullet's position as a decimal value
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def udpate(self, ai_settings):
        # update the decimal position of bullet
        self.y -= self.speed_factor
        #update the rect position
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

