import pygame
from ..color import COLOR

pygame.init()


class Player:

    def __init__(self, surface):
        self.surface    = surface
        self.size       = 10  # <============= radius
        self.speed      = 10  # <============ speed
        self.x          = 10  # <====== location of the player
        self.y          = 10  # <====== location of the player
        self.isAlive    = True
        self.player     = [self.surface, COLOR["white"], self.x, self.y, self.size]

    def draw(self):
        # Calculate scaling factor based on player size
        # adjust 50 to the max size that the player can grow to
        scaling_factor = self.size / 50.0

        # Calculate camera size based on scaling factor
        min_camera_size = 10
        max_camera_size = 50
        camera_size = min_camera_size + scaling_factor * \
            (max_camera_size - min_camera_size)

        # mouse_x, mouse_y = pygame.mouse.get_pos() # follow the mouse

        # print(f"x: {mouse_x}\ny: {mouse_y}")

        # Update player list with new position
        self.player[2] = self.x
        self.player[3] = self.y


        # Draw player circle with adjusted radius
        pygame.draw.circle(self.player[0], self.player[1], (self.player[2], self.player[3]), self.player[4] + camera_size)
        # self.update(mouse_x, mouse_y)


    def update(self, mouse_x, mouse_y):
        self.x = mouse_x - self.size / 2
        self.y = mouse_y - self.size / 2
