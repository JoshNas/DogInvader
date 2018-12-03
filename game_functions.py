import sys
import pygame


def check_events():
    """"Respond to key presses and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def update_screen(settings, screen, dog):
    """"Updates images on the screen and flip to the new screen"""
    # Redraw screen during each pass through loop
    screen.fill(settings.bg_color)
    dog.blitme()

    # Make the most recently drawn screen visible
    pygame.display.flip()
