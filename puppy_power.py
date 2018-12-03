import pygame
from settings import Settings
from dog import Dog
import game_functions as gf


def run_game():
    # Initialize game and create a screen object
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption('Roux the Day')

    # make a puppy
    dog = Dog(screen)

    # Set background color
    settings.bg_color = (230, 230, 230)

    # Start the main loop for game
    while True:
        gf.check_events()
        gf.update_screen(settings, screen, dog)


run_game()
