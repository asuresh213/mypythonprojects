import pygame
import time
import random

x = pygame.init()
w = 500
h = 500
gameDisplay = pygame.display.set_mode((w, h))
pygame.display.set_caption('Snake')

pygame.display.update()

game_exit = False
x = 100
y = 100
ls = 5
ws = 5
turned = False


def text_objects(text, font):
    textSurface = font.render(text, True, (0, 0, 0))
    return textSurface, textSurface.get_rect()


def message_display(score):
    largeText = pygame.font.Font('freesansbold.ttf', 10)
    TextSurf, TextRect = text_objects("Score = %s" % score, largeText)
    TextRect.center = (w-30, 10)
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()


def Snake(ls, ws, SnakeList):
    for XnY in SnakeList:
        pygame.draw.rect(gameDisplay, (0, 0, 0, 10), [XnY[0], XnY[1], 5, 5])


def Newfood():
    foodx = random.randrange(1, w/5)
    foody = random.randrange(1, h/5)
    food = [foodx, foody]
    return food


lost = False
xvel = 0
yvel = 0
food = [20, 10]
SnakeList = []
SnakeLength = 1
framerate = 0.09
Score = 0


while(not game_exit):
    message_display(Score)

    for event in pygame.event.get():

        if(event.type == pygame.QUIT):
            game_exit = True

        if(event.type == pygame.KEYDOWN):

            if(event.key == pygame.K_UP):
                if(yvel != 5):
                    xvel = 0
                    yvel = -5

            if(event.key == pygame.K_DOWN):
                if(yvel != -5):
                    xvel = 0
                    yvel = 5

            if(event.key == pygame.K_LEFT):
                if(xvel != 5):
                    xvel = -5
                    yvel = 0

            if(event.key == pygame.K_RIGHT):
                if(xvel != -5):
                    xvel = 5
                    yvel = 0
    x += xvel
    y += yvel

    gameDisplay.fill((255, 255, 255))
    pygame.draw.rect(gameDisplay, (255, 0, 0), [5*food[0],  5*food[1], 5, 5])

    SnakeHead = []
    SnakeHead.append(x)
    SnakeHead.append(y)
    SnakeList.append(SnakeHead)

    if(len(SnakeList) > SnakeLength):
        del(SnakeList[0])
    Snake(ls, ws, SnakeList)

    if(SnakeHead[0] == 5*food[0] and SnakeHead[1] == 5*food[1]):
        SnakeLength += 1
        Score += 1
        if(framerate > 0.03):
            framerate -= 0.02
        food = Newfood()
        pygame.draw.rect(gameDisplay, (0, 255, 0), [5*food[0], 5*food[1], 5, 5])

    if(x < 0 or x > w or y < 0 or y > h):
        game_exit = True
        print("LOST")

    if(SnakeLength > 1):
        for touch in SnakeList[:SnakeLength-2]:
            if(SnakeHead == touch):
                print("LOST")
                game_exit = True

    time.sleep(framerate)
    pygame.display.update()


pygame.quit()
quit()
