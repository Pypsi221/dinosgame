import pygame

pygame.init()
W ,H= 1200,700
FPS = 20

window = pygame.display.set_mode((W,H))
pygame.display.set_caption('Dino Game')
pygame.display.set_icon(pygame.image.load('assets/images/player/stand_4.png'))

bg = pygame.transform.scale(pygame.image.load('assets/background/level1.png'), (W, H))

platform_image = pygame.image.load("assets/background/platform.png")



clock = pygame.time.Clock()