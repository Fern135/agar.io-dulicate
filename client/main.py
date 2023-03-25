import pygame
import time
from sys import exit

#region src
from bin.color import COLOR
from bin.player.player import Player
# from bin.assets.LoadBg import LoadBackground
from bin.text.TextEngine import Text
#endregion

WIDTH, HEIGHT = 800, 800

pygame.init()
surface = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("Agar.io Dup")

def render(surface, pos=()):
    surface.blit(surface, pos)

player = Player(surface)
# bg = LoadBackground(surface, "imgPath") #TODO: implement loading of background
txt = Text("this is a test", None, 26, COLOR['silver'], 100, 100)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        elif event.type == pygame.MOUSEMOTION: # only updates if the mouse moves 
            # Update the player's position based on mouse movement
            mouse_x, mouse_y = pygame.mouse.get_pos()
            time.sleep(0.05)
            player.update(mouse_x, mouse_y)


    #game code
    player.draw()
    txt.draw()


    pygame.display.update()
    clock.tick(60)