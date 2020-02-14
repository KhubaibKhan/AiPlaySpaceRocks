import pygame
import numpy as np
from player import Player
from setting import *
from enemy import Enemy
from bullet import Bullet
from pygame import mixer


# Pyagme init
pygame.init()

# Background music
mixer.music.load("audio/disco_dancing.wav")
mixer.music.play(-1)

# Functions
def load_image(file_name, sizex, sizey):
    image = pygame.image.load(file_name)
    image = pygame.transform.scale(image, (sizex, sizey))
    return image
def distance(player_x, player_y, enemy_x, enemy_y):
    return np.sqrt((player_x - enemy_x)**2 + (player_y - enemy_y)**2)
def showScore(X, Y):
    score = font.render("Score: " + str(score_value), True, (0, 0, 0))
    screen.blit(score, (X, Y))
def gameOver():
    over_text = over_font.render("GAME OVER", True, (0, 0, 0))
    screen.blit(over_text, (200, 250))

# show score
score_value = 0
font = pygame.font.Font("freesansbold.ttf", 32)
scoreX = 10
scoreY = 10

# Game over screen
over_font = pygame.font.Font("freesansbold.ttf", 64)

# Making the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# Setting the title and the logo
pygame.display.set_caption("Space Rocks")
# icon = load_image("icon.png", 30, 30)


# Initialize the player
player_img = load_image("images/space-ship.png", 60, 60)
player = Player(player_img, 370, 500)
player_move = 0

# Initialize the enemy
enemy_image = load_image("images/stone.png", 60, 60)
enemy_list = []
for i in range(NUM_ENEMIES):
    enemy_list.append(Enemy(enemy_image))
enemy_move_x = ENEMY_SPEED
enemy_move_y = ENEMY_SPEED

# Initialize the bullet
bullet_image = load_image("images/bullet.png", 30, 30)
bullet_state = "ready"
bullet_list = []
bullet_fire = 0
bullet_move = 0

# Game loop
running = True
while(running):
    # Screen colour
    screen.fill((255, 255, 255))
    # Checking for inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_move = -PLAYER_SPEED
            elif event.key == pygame.K_RIGHT:
                player_move = PLAYER_SPEED
            elif event.key == pygame.K_SPACE:
                bullet_list.append(Bullet(bullet_image, player.getPlayerX(), player.getPlayerY()))
                bullet_state = "running"
                bullet_move = BULLET_SPEED
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player_move = 0
            elif event.key == pygame.K_RIGHT:
                player_move = 0
            elif event.key == pygame.K_SPACE:
                bullet_fire = 0


    # Check for collision
    # Player and rock collision
    for i in range(NUM_ENEMIES):
        if distance(player.getPlayerX(), player.getPlayerY(), enemy_list[i].getEnemyX(), enemy_list[i].getEnemyY()) < 30:
            enemy_list[i].reInit()
            if player.damage() <= 0:
                gameOver()
                running=False
                break
                
    # Rock and bullet collision
    for i in range(len(bullet_list)):
        for j in range(NUM_ENEMIES):
            if distance(bullet_list[i].getBulletX(), bullet_list[i].getBulletY(), enemy_list[j].getEnemyX(), enemy_list[j].getEnemyY()) < 40:
                if enemy_list[j].damage() <= 0:
                    score_value += 1
                    enemy_list[j].reInit()
                bullet_list[i].setBulletY(-100)

    # Enemy movement
    for i in range(NUM_ENEMIES):
        enemy_list[i].update(screen, enemy_move_x, enemy_move_y)

    # Player movement
    player.update(screen, player_move)

    # Bullet movement
    for i in range(len(bullet_list)):
        bullet_list[i].update(screen)

    # Removing the unwanting bullets
    for i in range(len(bullet_list)):
        if i >= len(bullet_list):
            break
        elif bullet_list[i].getBulletY() < 0:
            bullet_list.remove(bullet_list[i])
            # print("removed")
    showScore(scoreX, scoreY)
    # Updating the display
    pygame.display.update()