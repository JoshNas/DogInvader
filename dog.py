import pygame


class Dog():

    def __init__(self, screen):
        """Initialize the furry fury"""
        self.screen = screen

        # Load the dog image and get its rect
        self.image = pygame.image.load('images/RouxLion.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)

