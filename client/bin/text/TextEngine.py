import pygame


class Text:
    def __init__(self, content, font, size, color, x, y):
        self.content    = content
        self.font       = font
        self.size       = size
        self.color      = color
        self.x          = x
        self.y          = y

        # Check if font exists in pygame
        if pygame.font.match_font(self.font):
            self.font_obj = pygame.font.Font(self.font, self.size)
        else:
            # Set default font if font does not exist
            self.font_obj = pygame.font.SysFont(None, self.size)
            print(f"Font '{self.font}' not found. Using default font instead.")

        self.surface = self.font_obj.render(self.content, True, self.color)
        self.rect = self.surface.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self, screen):
        screen.blit(self.surface, self.rect)
