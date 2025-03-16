import pygame
from settings import *
from levels import*
pygame.init()

level1_objects,key,basket = draw_level(level1)

player = Player(50, H -90, 40, 50, 10, player_images)
portal = MapObject(1500,700,80,80, portal_image) 

level_objects.add(portal)
level1_objects.add(player)


game = True
while game:
    key_pressed = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    window.blit(bg,(0,0))
    for obj in level1_objects:
        window.blit(obj.image ,camera.apply(obj))
    camera.update(player)

    player.update()
    platforms.update()

    if pygame.sprite.spritecollide(player,coins,True):
        coins_count += 1

    window.blit(pygame.transform.scale(coin_image,(55,50)),(10,10))
    coin_txt = font1.render(f"{coins_count}",True,(255,255,255))
    window.blit(coin_txt,(55,20))

    if pygame.sprite.collide_rect(player,key):
        window.blit(get_key_txt,(W // 2,50))
        if key_pressed[pygame.K_e]:
            is_key = True
            key.rect.x = -200

    if  pygame.sprite.collide_rect(player,basket) and is_key:
        window.blit(open_basket_txt,(W // 2,50))
        if key_pressed[pygame.K_e]:
            coins_count += 30
            basket.rect.x  = -300

    if  pygame.sprite.collide_rect(player,basket) and not  is_key:
        window.blit(open_basket_txt,(W // 2,50))
       

       

    pygame.display.update()
    clock.tick(FPS)
