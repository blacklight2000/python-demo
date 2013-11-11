bif = 'Background.jpg'
mif = 'Background.png'
import pygame, sys
from pygame.locals import *
screen = pygame.display.set_mode((640,360),0,16)
background = pygame.image.load(bif).convert()
mouse_c = pygame.image.load(mif).convert_alpha()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    screen.blit(background,(0,0))


