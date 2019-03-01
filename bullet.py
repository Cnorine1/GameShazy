import entity2
import pygame.mask
import movement
from library import *


class bullet(entity2.entity2):
    def __init__(self, origin_x, origin_y, speed, path_to_img, angle=0, behavior='up'):
        super().__init__()
        self.speed = speed
        self.image, self.rect = load_image(path_to_img)
        # self.image = self.image.convert()
        self.imgFile = path_to_img
        # self.rect.centerx, self.rect.top = origin_x, origin_y
        self.off_screen = False
        self.dirty = 1
        self.mask = pygame.mask.from_surface(self.image)
        self.angle = angle

        # self.area = pygame.Rect(COLUMN_WIDTH, 0, SCREEN_WIDTH-(2*COLUMN_WIDTH), SCREEN_HEIGHT)
        self.rect.x = origin_x
        self.rect.y = origin_y

        # if the bullet is a bomb, then we need a timer
        #self.is_bomb = is_bomb
        #self.bomb_timer = 100
        #self.bomb_explode = [False, self.rect.x, self.rect.y]

        self.behaveDic = {
            "up": self.__up__,
            "northWest": self.__northWest__,
            "northEast": self.__northEast__,
            "northNorthEast": self.__northNorthEast__,
            "northNorthWest": self.__northNorthWest__,
            "missle": self.__missle__,
            "down": self.__down__,
            "bomb": self.__bomb__

        }

        self.movement = self.behaveDic[behavior]()

    # def move(self):
    # 	self.rect = self.rect.move(self.angle,-self.speed)
    # 	self.dirty = 1

    def move(self, x, y):

        self.rect = self.rect.move((x, y))
        self.dirty = 1

    def update(self):
        if self.rect.top > SCREEN_HEIGHT or self.rect.bottom < 0 or self.rect.right > SCREEN_WIDTH - COLUMN_WIDTH or self.rect.left < COLUMN_WIDTH:  # checks if the rect is out of bounds, and if so, it is no longer visible, meaning it should be deleted by GUI
            self.visible = 0
            self.dirty = 1
        # if self.is_bomb:
        #     self.bomb_timer -= 1
        #     if self.bomb_timer <= 0:
        #         self.visible = 0
        #         self.is_bomb = False
        #         print('BOOM')
        #         self.bomb_explode[0] = True
        #         self.bomb_explode[1] = self.rect.x
        #         self.bomb_explode[2] = self.rect.y
        # self.image, self.rect = load_image('resources/misc_sprites/explosion1.png')

        self.movement.update(self)

    # if not (COLUMN_WIDTH <= self.rect.right and self.rect.left <= SCREEN_WIDTH-COLUMN_WIDTH):
    # 	self.visible = 0
    # if not (0 <= self.rect.top <= SCREEN_HEIGHT):
    # 	self.visible = 0

    def __up__(self):
        # behaviorArray = ["down","stop","left","stop","up","stop","right"]
        # speedArray = [	  1*self.speed,	1*self.speed]
        return movement.Move(behaviorArray=['up'], moveCountArray=[800], speedArray=[self.speed],
                             angelArray=[self.angle])  # default behavior for object, could increase/decrease speed

    def __northEast__(self):
        return movement.Move(behaviorArray=['northEast'], moveCountArray=[800], speedArray=[self.speed],
                             angelArray=[self.angle])  # default behavior for object, could increase/decrease speed

    def __northNorthEast__(self):
        return movement.Move(behaviorArray=['northNorthEast'], moveCountArray=[800], speedArray=[self.speed * 0.5],
                             angelArray=[self.angle])  # default behavior for object, could increase/decrease speed

    def __northWest__(self):
        return movement.Move(behaviorArray=['northWest'], moveCountArray=[800], speedArray=[self.speed],
                             angelArray=[self.angle])  # default behavior for object, could increase/decrease speed

    def __northNorthWest__(self):
        return movement.Move(behaviorArray=['northNorthWest'], moveCountArray=[800], speedArray=[self.speed * 0.5],
                             angelArray=[self.angle])  # default behavior for object, could increase/decrease speed

    def __missle__(self):

        behaviorArray = ["up", "northWest", "left", "right", "up", "northEast", "right"]
        moveCountArray = [50, 20, 20, 20, 50, 20, 20]
        angleArray = [0, 45, -90, 90, 0, -45, 90]
        speedArray = [1 * self.speed]
        return movement.Move(behaviorArray, moveCountArray, speedArray, angleArray, exitscreen=False)

    def __down__(self):
        return movement.Move(behaviorArray=['down'], moveCountArray=[800], speedArray=[self.speed],
                             angelArray=[self.angle])

    def __bomb__(self):
        return movement.Move(behaviorArray=['up', 'up', 'up', 'up'], moveCountArray=[1, 20, 30, 49],
                             speedArray=[self.speed, self.speed * .7, self.speed * .5, self.speed * .2],
                             angelArray=[self.angle])
