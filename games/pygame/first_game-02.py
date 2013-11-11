import pygame,sys,random
from collections import deque

#global init
pygame.init()
size = 800,600
textcolor = 233,230,20
speed = -3
up = right = True
down = left = False
screen = pygame.display.set_mode(size)
bg = pygame.image.load("Background.png")
bgrect = bg.get_rect()
pygame.key.set_repeat(65,65)

