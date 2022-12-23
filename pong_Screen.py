
import pygame
import sys

pygame.init()
clock = pygame.time.Clock()
#setting up the game window
screen_height = 960
screen_width = 1280
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong')
running = True

#game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



def moveUp():
    return
def moveDown():
    return
def checkHit():
    return
def updateGameWindow():
     return   
pygame.quit()
sys.exit()