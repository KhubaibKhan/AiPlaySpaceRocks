import pygame
import numpy as np
from pygame import mixer


# Init
pygame.init()

# Screen
screen = pygame.display.set_mode((800, 600))#width height

# Background
backgroundImg = pygame.image.load('2352.jpg')
backgroundImg = pygame.transform.scale(backgroundImg, (800, 600))

# Background sound
mixer.music.load('disco_dancing.wav')
mixer.music.play(-1)

# Title and icon
pygame.display.set_caption("Space fuckers")
icon = pygame.image.load("rocket.png")
icon = pygame.transform.scale(icon, (30, 30))
pygame.display.set_icon(icon)


# player
playerImg = pygame.image.load('penis.png')
playerImg = pygame.transform.scale(playerImg, (70, 70))
playerX = 370
playerY = 400

# Movement of player
player_change = 0


# Enemy
EnemyImg = []
EnemyImg = []
EnemyX = []
EnemyY = []
enemy_changeX = []
enemy_changeY = []
num_enemies = 6

enemyImg = pygame.image.load('buttocks.png')

for i in range(num_enemies):
    EnemyImg.append(pygame.transform.scale(enemyImg, (70, 70)))
    EnemyX.append(np.random.uniform(low=0, high=735, size=((1))))
    EnemyY.append(np.random.uniform(low=50, high=150, size=((1))))

# Movement of Enemy
    enemy_changeX.append(4)
    enemy_changeY.append(30)


# Bullet
bulletImg = pygame.image.load('bullet.png')
bulletImg = pygame.transform.scale(bulletImg, (40, 40))
bulletX = 0
bulletY = 480

# Movement of Bullet
bullet_changeX = 0
bullet_changeY = 7

bullet_state = "ready"

def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y, i):
    screen.blit(EnemyImg[i], (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x+16, y+16))

def isCollided(enemyX, enemyY, bulletX, bulletY):
    distance = np.sqrt((enemyX - bulletX)**2 + (enemyY - bulletY)**2)
    if distance < 27:
        return True
    else:
        return False


# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
scoreX = 10
scoreY = 10

def show_score(X, Y):
    score = font.render("Fucked: " + str(score_value), True, (0, 0, 0))
    screen.blit(score, (X, Y))

over_font = pygame.font.Font('freesansbold.ttf', 64)

def game_over_text():
    over_text = over_font.render("GAME OVER: ", True, (0, 0, 0))
    screen.blit(over_text, (200, 250))

# Game loop
running = True
while(running):
    # Background colour
    screen.fill((255, 255, 255))
    # Background image
    # screen.blit(playerImg, (1, 530))
    # for i in range(40):
    #     screen.blit(playerImg, (30*i, 530))
    # Checking for inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_change = -1
            if event.key == pygame.K_RIGHT:
                player_change = 1
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    # bullet_sound = mixer.Sound('laser.wav')
                    # bullet_sound.play()
                    bulletX = playerX
                    fire_bullet(playerX, playerY);
                # bulletY = playerY
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player_change = 0
            if event.key == pygame.K_RIGHT:
                player_change = 0
        


    playerX += player_change
    # Player
    if playerX < 0 :
        playerX = 0
    elif playerX > 736:
        playerX = 736
    # Enemy
    for i in range(num_enemies):
        # Game oer
        if EnemyY[i] >= 350:
            for j in range(num_enemies):
                EnemyY[j] == 2000
            game_over_text()
            break
        EnemyX[i] += enemy_changeX[i]
        if EnemyX[i] < 0 :
            enemy_changeX[i] = 1
            EnemyY[i] += enemy_changeY[i]
        elif EnemyX[i] > 736:
            enemy_changeX[i] = -1
            EnemyY[i] += enemy_changeY[i]
            # Collision
        collision = isCollided(EnemyX[i], EnemyY[i], bulletX, bulletY)
        if collision:
            collision_sound = mixer.Sound('omg.wav')
            collision_sound.play()
            bulletY = playerY
            bullet_state = "ready"
            score_value += 1
            EnemyX[i] = np.random.uniform(low=0, high=735, size=((1)))
            EnemyY[i] = np.random.uniform(low=50, high=150, size=((1)))
        enemy(EnemyX[i], EnemyY[i], i);

    # bullet movement
    if bulletY <= 0:
        bulletY = playerY
        bullet_state = "ready"

    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bullet_changeY

    # Calling the player function
    player(playerX, playerY)
    # Show score
    show_score(scoreX, scoreY)
    # updating the display
    pygame.display.update()
