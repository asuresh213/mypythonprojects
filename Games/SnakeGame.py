import pygame
import time
import random
# setting up the screen
x = pygame.init()
w = 500
h = 500
gameDisplay = pygame.display.set_mode((w, h))
pygame.display.set_caption('Snake')

pygame.display.update()


# ------------------------------------------- USER FUNCTIONS--------------------
font = pygame.font.SysFont(None, 20)


def Lost(msg, color):
    screen_text = font.render(msg, True, color)
    gameDisplay. blit(screen_text, [0, h/2])


def text_objects(text, font):
    textSurface = font.render(text, True, (0, 0, 0))
    return textSurface, textSurface.get_rect()


def message_display(score, highscores):

    largeText = pygame.font.Font('freesansbold.ttf', 10)
    TextSurf1, TextRect1 = text_objects("Score = %s" % score, largeText)
    TextSurf2, TextRect2 = text_objects("High Score = %s" % max(highscores), largeText)
    TextRect1.center = (w-30, 10)
    TextRect2.center = (w-40, 20)
    gameDisplay.blit(TextSurf1, TextRect1)
    gameDisplay.blit(TextSurf2, TextRect2)

    pygame.display.update()


def Snake(ls, ws, SnakeList):
    for XnY in SnakeList:
        pygame.draw.rect(gameDisplay, (0, 255, 0), [XnY[0], XnY[1], 5, 5])


def Newfood():
    foodx = random.randrange(1, w/5)
    foody = random.randrange(1, h/5)
    food = [foodx, foody]
    return food

# ------------------------------------------------------------------------------

# ---------------------------------- MAIN GAME METHOD --------------------------


def gameloop():

    # INITIALIZING ALL VARIABLES

    highscores = [0]
    game_exit = False
    game_over = False
    Paused = False
    lost = False
    xvel = 0
    yvel = 0
    food = [20, 10]
    SnakeList = []
    SnakeLength = 1
    framerate = 0.09
    Score = 0
    x = 100
    y = 100
    ls = 5
    ws = 5
# ----------------------- MAIN GAME LOOP ----------------------------------------
    while(not game_exit):
        if(Paused == False):
            if(game_over == False):
                message_display(Score, highscores)

            for event in pygame.event.get():

                # All the key functionality.

                if(event.type == pygame.QUIT):
                    game_exit = True

                if(event.type == pygame.KEYDOWN):

                    if(event.key == pygame.K_UP):
                        # to make sure that the snake wasnt going down previously
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

                    if(event.key == pygame.K_SPACE):
                        Paused = True

            # updating velocities of the snake based on the keypressed
            x += xvel
            y += yvel

            gameDisplay.fill((255, 255, 255))
            # drawing the food at a random location on the canvas
            pygame.draw.rect(gameDisplay, (255, 0, 0), [5*food[0],  5*food[1], 5, 5])

            # track the snake
            SnakeHead = []
            SnakeHead.append(x)
            SnakeHead.append(y)
            SnakeList.append(SnakeHead)

            # make sure the snake isn't arbitrarily long
            if(len(SnakeList) > SnakeLength):
                del(SnakeList[0])
            Snake(ls, ws, SnakeList)

            # updating scores and creating new food
            if(SnakeHead[0] == 5*food[0] and SnakeHead[1] == 5*food[1]):
                SnakeLength += 1
                Score += 1
                if(framerate > 0.03):
                    framerate -= 0.02
                food = Newfood()

            # boundaries and losing
            if(x < 0 or x > w or y < 0 or y > h):
                game_over = True

            if(SnakeLength > 1):
                for touch in SnakeList[:SnakeLength-2]:
                    if(SnakeHead == touch):
                        game_over = True

            time.sleep(framerate)
            pygame.display.update()

            # Game over functionality
            if(game_over == True):
                highscores.append(Score)
                gameDisplay.fill((255, 255, 255))
                Lost("Game over. Press space to start again. Press Q to quit", (0, 0, 0))
                message_display(Score, highscores)
                pygame.display.update()
                for event in pygame.event.get():
                    print(event.key)
                    if(event.type == pygame.KEYDOWN):
                        if(event.key == pygame.K_SPACE):
                            x = 100
                            y = 100
                            xvel = 0
                            yvel = 0
                            framerate = 0.1
                            Score = 0
                            SnakeLength = 1
                            SnakeList = []
                            game_over = False
                        if(event.key == pygame.K_q):
                            game_exit = True

        # Pause/Resume functionality
        if(Paused == True):
            gameDisplay.fill((255, 255, 255))
            Lost("Paused. Press Space to resume", (0, 0, 0))
            pygame.display.update()
            for event in pygame.event.get():
                if(event.type == pygame.KEYDOWN):
                    if(event.key == pygame.K_SPACE):
                        Paused = False
    pygame.quit()
    quit()
# -------------------------------------------------------------------------------


gameloop()
