import pygame

pygame.init()

class LoadBackground:

    def __init__(self, screen, img_path):
        self.image = pygame.image.load(img_path).convert()
        self.screen = screen

    def draw(self):
        self.screen.blit(self.image, (0, 0))
