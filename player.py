import entity2
import pygame
import bullet
import weapon
from library import *



class player(entity2.entity2):
    def __init__(self, init_wep, imgFile, scheme):
        super().__init__()
        self.weapon = weapon.Weapon(init_wep)
        self.control_scheme = scheme ##placeholder
        self.point_total = 0
        self.image, self.rect = load_image(imgFile, -1)

        self.area = pygame.Rect(COLUMN_WIDTH, 0, SCREEN_WIDTH-(2*COLUMN_WIDTH), SCREEN_HEIGHT)

        self.rect.topleft = 500,600
        self.speed = 10
        self.bullet_count = 0
        self.dirty = 2

    def move(self, new_x, new_y):
        if self.rect.left < self.area.left: ###I hate this function. I need to make it better. -Chris
            self.rect.left = self.area.left
        elif self.rect.right > self.area.right:
            self.rect.right = self.area.right
        elif self.rect.top < self.area.top:
            self.rect.top = self.area.top
        elif self.rect.bottom > self.area.bottom:
            self.rect.bottom = self.area.bottom
        else:
            self.rect = self.rect.move((new_x, new_y))
        #self.dirty = 1

    def fire(self):
        origin_x = (self.rect.left + self.rect.right) / 2
        origin_y = self.rect.top

        return self.weapon.weapon_func(origin_x, origin_y)
        #return bullet.bullet(origin_x, origin_y, 5, self.weapon.weapon_image)
    
    def control(self, keys, FRAMERATE):
        addBullet=False
        if self.control_scheme=="arrows":
            if keys[pygame.K_UP]:
                self.move(0,-self.speed)
            if keys[pygame.K_DOWN]:
                self.move(0,self.speed)
            if keys[pygame.K_LEFT]:
                self.move(-self.speed, 0)
            if keys[pygame.K_RIGHT]:
                self.move(self.speed, 0)
            ##this if/else statement must stay together
            if keys[pygame.K_SPACE]:
                if self.bullet_count % (int(FRAMERATE/self.weapon.rof)) == 0:
                    addBullet=True
                self.bullet_count += 1
            else:
                self.bullet_count = 0
            ##end if/else            
            if keys[pygame.K_1]:

                self.weapon = weapon.Weapon('spitfire')
            if keys[pygame.K_2]:

                self.weapon = weapon.Weapon('spitfire2')

            if keys[pygame.K_3]:
                self.weapon = weapon.Weapon('spitfire3')


        return addBullet