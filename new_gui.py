#!/bin/python

from entity import *
import pygame
from pygame.locals import *
from pygame.compat import geterror
from pathlib import *

main_dir = os.path.split(os.path.abspath(__file__))[0]
def load_sound(name):
    class NoneSound:
        def play(self):
            pass
    if not pygame.mixer or not pygame.mixer.get_init():
        return NoneSound()
    fullname = os.path.join(main_dir, name)
    try:
        sound = pygame.mixer.Sound(fullname)
    except pygame.error:
        print ('Cannot load sound: %s' % fullname)
        raise SystemExit(str(geterror()))
    return sound

def main():
    FRAMERATE = 60
    pygame.init()
    screen = pygame.display.set_mode((1024,786))
    pygame.display.set_caption('Raiden Clone - Day 0')
    pygame.mouse.set_visible(False)

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0,0,0))

    pygame.mixer.music.load('roboCop3NES.mp3')
    pygame.mixer.music.play(loops=-1)
    explode = load_sound('explosn.wav')
    fire_shot = load_sound('pewpew.wav')

    clock = pygame.time.Clock()
    player = player_ship()
    bad_guy = enemy()
    playersprites = pygame.sprite.LayeredDirty((player))
    enemysprites = pygame.sprite.LayeredDirty((bad_guy))

    playersprites.clear(screen, background)
    enemysprites.clear(screen, background)

    pygame.key.set_repeat(10,10)

    going=True

    bullet_count = 0

    while going:
        clock.tick(FRAMERATE)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            player.move(0,-player.speed)
        if keys[pygame.K_DOWN]:
            player.move(0,player.speed)
        if keys[pygame.K_LEFT]:
            player.move(-player.speed, 0)
        if keys[pygame.K_RIGHT]:
            player.move(player.speed, 0)
        if keys[pygame.K_SPACE]:
            if bullet_count % (int(FRAMERATE/player.weapon.rof)) == 0:
                fire_shot.play() 
                bullet = player.fire()
                playersprites.add(bullet)
            bullet_count += 1

        for event in pygame.event.get():
            if event.type == QUIT:
                going = False
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                going = False
            elif event.type == KEYDOWN and event.key == K_F1: ##DEBUG CODE. DO NOT FORGET TO REMOVE
                bad_guy = enemy()
                if len(enemysprites) == 0:
                    enemysprites.add(bad_guy)
            elif event.type == KEYDOWN and event.key == K_F2: ##DEBUG CODE. DO NOT FORGET TO REMOVE
                player = player_ship()
                if len(playersprites) == 0:
                    playersprites.add(player)
            elif event.type == KEYUP and event.key == K_SPACE:
                bullet_count = 0
            
        playersprites.update()
        enemysprites.update()
      
        for sprite in playersprites:
            #collision = pygame.sprite.spritecollideany(sprite, enemysprites)
            #if collision:
                #explode.play()
                #playersprites.remove(sprite)
            if sprite.visible == 0:
                playersprites.remove(sprite)    
        for sprite in enemysprites:
            collision = pygame.sprite.spritecollideany(sprite, playersprites)
            if collision:
                explode.play()
                enemysprites.remove(sprite)
            if sprite.visible == 0:
                enemysprites.remove(sprite)         

        player_rects = playersprites.draw(screen)
        enemy_rects = enemysprites.draw(screen)

        pygame.display.update(player_rects)
        pygame.display.update(enemy_rects)
    
    pygame.quit()

if __name__=='__main__':
    main()

