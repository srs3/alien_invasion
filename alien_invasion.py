import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group




def run_game():
    # Initialise game and create a screen object
    pygame.init()
    ai_settings = Settings()

    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(ai_settings, screen)

    # make a group to store bullets in
    bullets = pygame.sprite.Group()


    # Start loop for game
    while True:

        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        gf.update_bullets(bullets)
        gf.udpate_screen(ai_settings, screen, ship, bullets)


run_game()

