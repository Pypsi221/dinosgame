import pygame

pygame.init()
W ,H= 1200,700
FPS = 20
coins_count = 0
is_key = False


window = pygame.display.set_mode((W,H))
pygame.display.set_caption('Dino Game')
pygame.display.set_icon(pygame.image.load('assets/images/player/stand_4.png'))

clock = pygame.time.Clock()
'''''ГРУПИ'''
coins = pygame.sprite.Group()
platforms = pygame.sprite.Group()
""""КАРТИНКИ"""
bg = pygame.transform.scale(pygame.image.load('assets/background/bg.jpg'), (W, H))

platform_image = pygame.image.load("assets/background/platform.png")



player_images = [
    pygame.image.load("assets/images/player/stand_1.png"),
    pygame.image.load("assets/images/player/stand_2.png"),
    pygame.image.load("assets/images/player/stand_3.png"),
    pygame.image.load("assets/images/player/stand_4.png"),
    pygame.image.load("assets/images/player/move_right_1.png"),
    pygame.image.load("assets/images/player/move_right_2.png"),
    pygame.image.load("assets/images/player/move_right_3.png"),
    pygame.image.load("assets/images/player/move_right_4.png"),
    pygame.image.load("assets/images/player/move_right_5.png"),
    pygame.image.load("assets/images/player/move_right_6.png"),
    pygame.image.load("assets/images/player/move_left_1.png"),
    pygame.image.load("assets/images/player/move_left_2.png"),
    pygame.image.load("assets/images/player/move_left_3.png"),
    pygame.image.load("assets/images/player/move_left_4.png"),
    pygame.image.load("assets/images/player/move_left_5.png"),
    pygame.image.load("assets/images/player/move_left_6.png"),
]
coin_image = pygame.image.load('assets/images/coin/coin.png')
portal_image = pygame.image.load('assets/images/portal/portal.png')
basket_image = pygame.image.load('assets/images/basket/basket.png')
key_image = pygame.image.load('assets/images/key/key.jpg')
door_image = pygame.image.load('assets/images/door/door.jpg')

""""ШРИФИММ"""
pygame.font.init()
font1 = pygame.font.Font(None,60)

