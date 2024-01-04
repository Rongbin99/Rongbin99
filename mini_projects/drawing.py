# Rongbin Gu.
# Drawing.py
# June 9, 2021

# Import a library of functions called 'pygame'
import pygame
from math import pi

# Initialize the game engine
pygame.init()

# Define the colors we will use in RGB format
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  ( 0, 165, 237)
GREEN = (114, 186, 31)
ORANGE =   (255, 69, 38)
PURPLE = (155, 19, 211)
AQUA =  (19, 184, 211)
GREY = (116, 116, 118)
LIGHTGREY = (232, 232, 232)
YELLOW = (255, 183, 31)
GOLDYELLOW = (224, 195, 23)

# Set the height and width of the screen
size = [660, 400]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Computer Drawing by Rongbin Gu")

#Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()

while not done:
    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(10)
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop
    
    # Clear the screen and set the screen background
    screen.fill(WHITE)
#########################################################
    pygame.draw.rect(screen, BLACK, [0, 0, 660, 50])
    pygame.draw.rect(screen, BLACK, [0, 350, 660, 50])
    pygame.draw.aaline(screen,BLACK, [305, 320], [305, 340],True)
    pygame.draw.aaline(screen,BLACK, [310, 320], [310, 330],True)
    pygame.draw.aaline(screen,BLACK, [305, 340], [390,340],True)
    pygame.draw.aaline(screen,BLACK, [310, 330], [500 ,330],True)
    pygame.draw.aaline(screen,BLACK, [500, 330], [500, 320],True)
    pygame.draw.aaline(screen,BLACK, [420, 340], [505, 340],True)
    pygame.draw.aaline(screen,BLACK, [505, 340], [505, 320],True)
    pygame.draw.aaline(screen,BLACK, [305, 290], [305, 240],True)
    pygame.draw.aaline(screen,BLACK, [310, 290], [310, 240],True)
    pygame.draw.rect(screen, BLACK, [390, 335, 10 , 10])
    pygame.draw.rect(screen, BLACK, [410, 335, 10, 10])
    pygame.draw.rect(screen, BLACK, [410, 290, 20, 10])
    pygame.draw.rect(screen, BLACK, [480, 100, 100, 200])
    pygame.draw.rect(screen, BLACK, [120, 70, 290, 170])
    pygame.draw.rect(screen, GREY, [123, 73, 284, 164])
    pygame.draw.rect(screen, ORANGE, [230, 120, 30, 30])
    pygame.draw.rect(screen, GREEN, [265, 120, 30, 30])
    pygame.draw.rect(screen, BLUE, [230, 155, 30, 30])
    pygame.draw.rect(screen, YELLOW, [265, 155, 30, 30])
    pygame.draw.rect(screen, BLACK, [235, 240, 60, 50])
    pygame.draw.rect(screen, BLACK, [150, 290, 230, 10])
    pygame.draw.circle(screen, PURPLE, [530, 135],30)
    pygame.draw.circle(screen, AQUA, [530, 200],30)
    pygame.draw.circle(screen, PURPLE, [530, 265],30)
    pygame.draw.polygon(screen, AQUA, [[30, 80], [90, 90], [50, 130]])
    pygame.draw.polygon(screen, PURPLE, [[90, 90], [50, 130], [110, 140]])
    pygame.draw.polygon(screen, AQUA, [[50, 130], [110, 140], [70, 180]])
    pygame.draw.polygon(screen, PURPLE, [[50, 130], [70, 180], [20, 170]])
    pygame.draw.polygon(screen, AQUA, [[20, 170], [70, 180], [40, 220]])
    pygame.draw.polygon(screen, PURPLE, [[70, 180], [40, 220], [90, 230]])
    pygame.draw.polygon(screen, AQUA, [[40, 220], [90, 230], [60, 270]])
    pygame.draw.polygon(screen, PURPLE, [[40, 220], [60, 270], [20, 260]])
    pygame.draw.polygon(screen, AQUA, [[20, 260], [60, 270], [20, 310]])
    pygame.draw.polygon(screen, PURPLE, [[60, 270], [80, 320], [20, 310]])
    pygame.draw.polygon(screen, AQUA, [[60, 270], [110, 280], [80, 320]])
    pygame.draw.polygon(screen, PURPLE, [[110, 280], [80, 320], [130, 330]])
    pygame.draw.rect(screen, BLACK, [45, 190, 35, 110])
    pygame.draw.aaline(screen,GOLDYELLOW, [45, 190], [80, 190],True)
    pygame.draw.aaline(screen,GOLDYELLOW, [45, 210], [80, 210],True)
    pygame.draw.aaline(screen,GOLDYELLOW, [45, 300], [80, 300],True)
    pygame.draw.aaline(screen,GOLDYELLOW, [45, 190], [45, 190],True)
    pygame.draw.aaline(screen,GOLDYELLOW, [80, 190], [80, 300],True)
    pygame.draw.aaline(screen,GOLDYELLOW, [50, 213], [75, 213],True)
    pygame.draw.aaline(screen,GOLDYELLOW, [50, 213], [50, 219],True)
    pygame.draw.aaline(screen,GOLDYELLOW, [50, 221], [75, 221],True)
    pygame.draw.aaline(screen,GOLDYELLOW, [75, 217], [75, 223],True)
    pygame.draw.aaline(screen,GOLDYELLOW, [75, 227], [75, 233],True)
    pygame.draw.aaline(screen,GOLDYELLOW, [50, 230], [75, 230],True)
    pygame.draw.aaline(screen,GOLDYELLOW, [75, 235], [75, 240],True)
    pygame.draw.aaline(screen,GOLDYELLOW, [62.5, 235], [62.5, 240],True)
    pygame.draw.aaline(screen,GOLDYELLOW, [50, 235], [50, 240],True)
    pygame.draw.aaline(screen,GOLDYELLOW, [62.5, 235], [75, 235],True)
    pygame.draw.aaline(screen,GOLDYELLOW, [50, 240], [62.5, 240],True)
    pygame.draw.aaline(screen,GOLDYELLOW, [50, 245], [75, 245],True)
    pygame.draw.aaline(screen,GOLDYELLOW, [75, 242], [75, 248],True)
    pygame.draw.aaline(screen,GOLDYELLOW, [50, 250], [50, 257],True)
    pygame.draw.aaline(screen,GOLDYELLOW, [75, 250], [75, 257],True)
    pygame.draw.aaline(screen,GOLDYELLOW, [50, 250], [75, 250],True)
    pygame.draw.aaline(screen,GOLDYELLOW, [50, 257], [75, 257],True)
    pygame.draw.aaline(screen,GOLDYELLOW, [50, 260], [75, 260],True)
    pygame.draw.aaline(screen,GOLDYELLOW, [62.5, 260], [62.5, 266],True)
    pygame.draw.aaline(screen,GOLDYELLOW, [75, 260], [75, 266],True)
    pygame.draw.aaline(screen,GOLDYELLOW, [50, 265], [62.5, 260],True)
    pygame.draw.aaline(screen,GOLDYELLOW, [62.5, 266], [75, 266],True)
    pygame.draw.aaline(screen,GOLDYELLOW, [50, 269], [75, 269],True)
    pygame.draw.aaline(screen,GOLDYELLOW, [50, 269], [50, 274],True) #
    pygame.draw.aaline(screen,GOLDYELLOW, [62.5, 269], [62.5, 274],True) #
    pygame.draw.aaline(screen,GOLDYELLOW, [75, 269], [75, 274],True) #
    pygame.draw.rect(screen, GOLDYELLOW, [50, 276, 2, 2])
    pygame.draw.aaline(screen,GOLDYELLOW, [50, 280], [75, 280],True)
    pygame.draw.aaline(screen,GOLDYELLOW, [50, 280], [50, 285],True)
    pygame.draw.aaline(screen,GOLDYELLOW, [75, 280], [75, 285],True)
    pygame.draw.aaline(screen,GOLDYELLOW, [50, 287], [50, 291],True)
    pygame.draw.aaline(screen,GOLDYELLOW, [75, 287], [75, 291],True)
    pygame.draw.aaline(screen,GOLDYELLOW, [50, 287], [75, 287],True)
    pygame.draw.aaline(screen,GOLDYELLOW, [50, 291], [75, 291],True)
    pygame.draw.aaline(screen,GOLDYELLOW, [50, 293], [75, 293],True)
    pygame.draw.aaline(screen,GOLDYELLOW, [75, 293], [63, 295],True)
    pygame.draw.aaline(screen,GOLDYELLOW, [63, 295], [75, 297],True)
    pygame.draw.aaline(screen,GOLDYELLOW, [50, 297], [75, 297],True)
    pygame.draw.rect(screen, LIGHTGREY, [20, 300, 620, 20])
    pygame.draw.rect(screen, LIGHTGREY, [50, 320, 30, 30])
    pygame.draw.rect(screen, LIGHTGREY, [580, 320, 30, 30])
#########################################################
    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()

# Be IDLE friendly
pygame.quit()
