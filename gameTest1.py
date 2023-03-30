import sys, pygame, random
from pygame.locals import *

# Set up pygame
pygame.init()
mainClock = pygame.time.Clock()

#set the windows
WINDOWWIDTH = 400
WINDOWHEIGHT = 400
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Collision Detection')

# set colors
BLACK = (0,0,0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

#Set up the player and food data structures
foodCounter = 0
NEWFOOD = 40
FOODSIZE = 20
player = pygame.Rect(300, 100, 40, 40)
playerImage = pygame.image.load('image.png')
foods = []
for i in range(20):
    foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH - FOODSIZE),
        random.randint(0, WINDOWHEIGHT - FOODSIZE), FOODSIZE, FOODSIZE))
# Set up movement variables
moveLeft = False
moveRight = False
moveUp = False
moveDown = False

MOVESPEED = 6

# Run the game loop
while True:
    #Check for events.
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            # Change the keyboard variables
            if event.key == K_LEFT or event.key == K_a:
                moveRight = False
                moveLeft = True
            if event.key == K_RIGHT or event.key == K_d:
                moveLeft = False
                moveRight = True
            if event.key == K_UP or event.key == K_w:
                moveDown = False
                moveUp = True
            if event.key == K_DOWN or event.key == K_s:
                moveUp = False
                moveDown = True
        if event.type == KEYUP:
            # Change the keyboard variables
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_LEFT or event.key == K_a:
                moveLeft = False
            if event.key == K_RIGHT or event.key == K_d:
                moveRight = False
            if event.key == K_UP or event.key == K_w:
                moveUp = False
            if event.key == K_DOWN or event.key == K_s:
                moveDown = False
            if event.key == K_x:
                player.top = random.randint(0, WINDOWHEIGHT - player.height)
                player.left = random.randint(0, WINDOWWIDTH - player.width)

        if event.type == MOUSEBUTTONUP:
            foods.append(pygame.Rect(event.pos[0], event.pos[1], FOODSIZE, FOODSIZE))
    foodCounter += 1
    if foodCounter >= NEWFOOD:
        #add new food
        foodCounter = 0
        foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH - FOODSIZE), random.randint(0, WINDOWHEIGHT - FOODSIZE), FOODSIZE, FOODSIZE))

    # draw white background onto the surgace
    windowSurface.fill(WHITE)

    #Move the Player
    if moveDown and player.bottom < WINDOWHEIGHT:
        player.top += MOVESPEED
    if moveUp and player.top > 0:
        player.top -= MOVESPEED
    if moveLeft and player.left > 0:
        player.left -= MOVESPEED
    if moveRight and player.right < WINDOWWIDTH:
        player.right += MOVESPEED

    # Draw the player onto the surface
    pygame.draw.rect(windowSurface, BLACK, player)

    # Draw the block onto the surface
    windowSurface.blit(playerImage, player)

    #check whether the player had intersected with any food squares.
    for food in foods[:]:
        if player.colliderect(food):
            foods.remove(food)

    #Draw the food.
    for i in range(len(foods)):
        pygame.draw.rect(windowSurface, GREEN, foods[i])

    #Draw the Window onto the screensize
    pygame.display.update()
    mainClock.tick(40)
