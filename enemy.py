import pygame
import numpy as np
from setting import *


class Enemy():
    def __init__(self, enemy_img):
        self.enemyX = np.random.uniform(low=0, high=735, size=((1)))
        self.enemyY = np.random.uniform(low=-50, high=0, size=((1)))
        self.enemy_img = enemy_img
        (width, height) = enemy_img.get_size()
        self.enemy_width = width
        self.enemy_height = height
        self.health = ENEMY_HEALTH
    def getEnemyX(self):
        return self.enemyX
    def getEnemyY(self):
        return self.enemyY
    def getHealth(self):
        return self.health
    def damage(self):
        self.health -= 1
        return self.health
    def update(self, screen, x=0, y=0):
        self.enemyY += y
        self.canMove(SCREEN_WIDTH, SCREEN_HEIGHT)
        screen.blit(self.enemy_img, (self.enemyX, self.enemyY))
    def canMove(self, screen_width, screen_height):
        if self.enemyX < 0:
            self.playerX = 0
        elif self.enemyY > screen_height:
            self.reInit()
    def reInit(self):
        self.health = ENEMY_HEALTH
        self.enemyX = np.random.uniform(low=0, high=735, size=((1)))
        self.enemyY = np.random.uniform(low=-50, high=0, size=((1)))