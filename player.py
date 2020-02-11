import pygame
from setting import *


class Player():
    def __init__(self, player_img, player_x, player_y):
        self.playerX = player_x
        self.playerY = player_y
        self.player_img = player_img
        (width, height) = player_img.get_size()
        self.player_width = width
        self.player_height = height
        self.health = PLAYER_HEALTH
    def getPlayerX(self):
        return self.playerX
    def getPlayerY(self):
        return self.playerY
    def update(self, screen, x=0, y=0):
        self.playerX += x
        self.playerY += y
        self.canMove(SCREEN_WIDTH, SCREEN_HEIGHT)
        screen.blit(self.player_img, (self.playerX, self.playerY))
    def getHealth(self):
        return self.health
    def damage(self):
        self.health -= 1
        return self.health
    def canMove(self, screen_width, screen_height):
        if self.playerX < 0:
            self.playerX = 0
        elif self.playerX > screen_width - self.player_width:
            self.playerX = screen_width - self.player_width
