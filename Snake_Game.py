import pygame
import random
pygame.init()           #initializing pygame

black = (0,0,0)
white = (255,255,255)
blue = (0,0,255)
red = (255,0,0)
green = (0,255,0)

window_width = 800
window_height = 600

window = pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption("Snake Game")

icon = pygame.image.load("apple.png")      #game icon image
pygame.display.set_icon(icon)

headImage = pygame.image.load("SnakeHead.png")
appleImage = pygame.image.load("apple.png")

clock = pygame.time.Clock()

AppleThickness = 20
block_size = 20  #pixels covered per keypress/movement. Also the thickness(size) of the snake.     
FPS = 24  #game FPS

# SCORE DISPLAYING FUNCTION:
def score(score):
    text = smallFont.render("Score: "+str(score), True, white)
    window.blit(text, [0,0]) # top-left

# START SCREEN FUNCTION:
def start_screen():
    start = True
    while start:               #While loop for authenticating/configuring key presses. 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    start = False
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

        window.fill(black)
        message_to_screen("Welcome to Snake Game!", green, -100, "large")
        message_to_screen("The objective of the game is to eat red apples.", white, -30, "small")
        message_to_screen("The more apples you eat, the longer you get.", white, 10, "small")
        message_to_screen("If you run into yourself, or the edges, you die!", white, 50, "small")
        message_to_screen("Press 'SPACE BAR' to play and pause or 'ESC' to exit.", white, 180, "small")
        pygame.display.update()
        clock.tick(15)    #FPS

# GAME PAUSE FUNCTION:
def pause_game():
    message_to_screen("Paused!",white,-70,"large")
    message_to_screen("Press 'SPACEBAR' to continue or 'ESC' to quit.",white,30,"small")
    pygame.display.update()
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = False
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
        clock.tick(5)   #FPS


direction = "right"    #direction the snake faces at the start of the game.
# SNAKE FUNCTION (To extend the size of snake after it eats the apple.)
def snake(block_size,snakeList):
# drawing/blitting the snake head:
    if direction == "right":                       
        head = pygame.transform.rotate(headImage, 270)
    if direction == "left":
        head = pygame.transform.rotate(headImage, 90)
    if direction == "up":
        head = headImage
    if direction == "down":
        head = pygame.transform.rotate(headImage, 180)

    window.blit(head, (snakeList[-1][0], snakeList[-1][1]))       #(x,y) pair
    for element in snakeList[:-1]:              #element = x and y element
        pygame.draw.rect(window,green,[element[0],element[1],block_size,block_size]) 
    
# MESSAGE/TEXT FUNCTION:
smallFont = pygame.font.SysFont("verdana",25)
mediumFont = pygame.font.SysFont("verdana",40)
largeFont = pygame.font.SysFont("verdana",55)

def text_object(message,color,size):           #Text is surrounded by an invisible rectangle.
    if size == "small":
        textSurface = smallFont.render(message,True,color)
    elif size == "medium":
        textSurface = mediumFont.render(message,True,color)
    elif size == "large":
        textSurface = largeFont.render(message,True,color)
    return textSurface,textSurface.get_rect()

def message_to_screen(message, color, y_displacement=0, size="small"):
    textSurface,textRect = text_object(message,color,size)       #textSurface and textRect are tuples.
    # screen_text = font.render(message,True,color)
    # window.blit(screen_text,[window_width/2,window_height/2])  # [x-axis,y-axis]
    textRect.center = (window_width/2),(window_height/2) + y_displacement
    window.blit(textSurface,textRect)

def randomAppleGenerator():
    randmAppleX = random.randrange(0,window_width-AppleThickness)      # (start,stop)     
    randmAppleY = random.randrange(0,window_height-AppleThickness)
    return randmAppleX, randmAppleY

# MAIN GAME LOOP:
def gameLoop():
    global direction
    direction = "right"
    lead_x = window_width / 2    #x-axis (points according to the x-axis at which the snake initiates.) 
    lead_y = window_height / 2   #y-axis (points according to the y-axis at which the snake initiates.)

    lead_x_change = 10       # changing the value will make the snake running instantly the game is started. 
    lead_y_change = 0

    snakeList = []         # will be used to increase the size of snake every time it eats the apple.
    snakeLength = 1        # length of snake

    gameExit = False
    gameOver = False

    randmAppleX,randmAppleY = randomAppleGenerator()

    while not gameExit:
        while gameOver == True:
            window.fill(black)
            message_to_screen("Game Over!", red, -50, size="large")
            message_to_screen("Press 'esc' to exit and 'r' to play again.", white, 50, size="small")
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = False
                    gameExit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        gameExit = True
                        gameOver = False #for stopping while loop 
                    if event.key == pygame.K_r:
                        gameLoop()  
        for event in pygame.event.get():
            # print(event)        To get all events
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direction = "left"
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    direction = "right"
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    direction = "up"
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    direction = "down"
                    lead_y_change = block_size
                    lead_x_change = 0
                elif event.key == pygame.K_SPACE:      # calling pause game function on pressing spacebar.
                    pause_game()

            #If you want the snake to stop after releasing the key:
            # if event.type == pygame.KEYUP:    
            #     if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            #         lead_x_change = 0

        # Defining boundaries for the snake:
        if lead_x >= window_width-block_size or lead_x <= 0 or lead_y >= window_height-block_size or lead_y <= 0: 
            gameOver = True
        
        lead_x += lead_x_change
        lead_y += lead_y_change
        window.fill(black)     #background color

        # drawing/blitting the apple:
        window.blit(appleImage,(randmAppleX, randmAppleY))

        # pygame.draw.rect(window,red,[randmAppleX,randmAppleY,AppleThickness,AppleThickness])   #[ x-axis, y-axis, width, length]

        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        if len(snakeList) > snakeLength:          # to maintain the length of the snake throughout
            del snakeList[0]

        # Following is to prevent from crashing the snake into itself:
        for eachSegment in snakeList[:-1]:     #snake list excluding the last element because it is the head.   
            if eachSegment == snakeHead:
                gameOver = True

        snake(block_size,snakeList)                #calling the snake function.                             

        # The code-line that will be below will be drawn over the upper one.
        score(snakeLength-1)        # calling score function.
        pygame.display.update()

        # Eating and Re-Appearing of the Apple:

        # if lead_x == randmAppleX and lead_y == randmAppleY:
        #     randmAppleX = random.randrange(0,window_width-block_size,10)      
        #     randmAppleY = random.randrange(0,window_height-block_size,10)
        #     snakeLength += 1        # Everytime the sanke eats the apple it gets +1 in length

        # Small snake but big apple:
        
        # if lead_x >= randmAppleX and lead_x <= randmAppleX + AppleThickness:
        #     if lead_y >= randmAppleY and lead_y <= randmAppleY + AppleThickness:
        #         randmAppleX = random.randrange(0,window_width-block_size)      
        #         randmAppleY = random.randrange(0,window_height-block_size)
        #         snakeLength += 1    

        # More precise code:

        if lead_x > randmAppleX and lead_x < randmAppleX + AppleThickness or lead_x + block_size > randmAppleX and lead_x + block_size < randmAppleX + AppleThickness:
            if lead_y > randmAppleY and lead_y < randmAppleY + AppleThickness or lead_y + block_size > randmAppleY and lead_y + block_size < randmAppleY + AppleThickness:
                randmAppleX,randmAppleY = randomAppleGenerator()                
                snakeLength += 1    

        clock.tick(FPS)   #game FPS
    pygame.quit()      #uninitializing pygame
start_screen()       #calling start screen function 
gameLoop()



