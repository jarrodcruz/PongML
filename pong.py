
import pygame
import sys

pygame.init()
clock = pygame.time.Clock()

screen_height = 960
screen_width = 1280
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong')

while True:
    if key.get_pressed[K_q]:
        quitGame()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quitGame()
            
def quitGame():
    pygame.quit()
    sys.exit()