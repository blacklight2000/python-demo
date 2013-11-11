bif = 'Background.jpg'
mif = 'Background.png'
import pygame, sys
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((640,360))
background = pygame.image.load(bif)
pygame.key.set_repeat(65,65)

