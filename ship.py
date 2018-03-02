import pygame

class Ship():

    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('Images/alienship2.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        # the line below gives us the y coordinate of the bottom of the image
        self.rect.centery = self.screen_rect.bottom - 20
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)
        self.bottom = float(self.rect.bottom)
        self.centery = float(self.rect.centery)

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        # self.center is a variable which will store the total movement left or right depending on the ship_speed_factor
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.top > 0:
            self.centery -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.ai_settings.ship_speed_factor


        self.rect.centerx = self.center
        self.rect.centery = self.centery


    def blitme(self):
        """draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)