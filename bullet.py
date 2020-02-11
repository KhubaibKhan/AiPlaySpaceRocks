import pygame
from setting import *


class Bullet():
    def __init__(self, bullet_img, bullet_x, bullet_y):
        self.bulletX = bullet_x
        self.bulletY = bullet_y
        self.bullet_img = bullet_img
        (width, height) = bullet_img.get_size()
        self.bullet_width = width
        self.bullet_height = height
    def getBulletX(self):
        return self.bulletX
    def getBulletY(self):
        return self.bulletY
    def setBulletY(self, y):
        self.bulletY = y
    def update(self, screen):
        # self.bulletX += x
        self.bulletY -= BULLET_SPEED
        self.canMove(SCREEN_WIDTH, SCREEN_HEIGHT)
        screen.blit(self.bullet_img, (self.bulletX, self.bulletY))
    def canMove(self, screen_width, screen_height):
        if self.bulletX < 0:
            self.bulletX = 0
        elif self.bulletX > screen_width - self.bullet_width:
            self.bulletX = screen_width - self.bullet_width
    def reInit(self, x, y):
        self.buleltX = x
        self.bulletY = y
        
