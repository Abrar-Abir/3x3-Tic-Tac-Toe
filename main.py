import pygame, sys
from pygame.locals import *

# Variable Declaration
title = "Tic-Tac-Toe"

makeMove = "Make your move by clicking on the cell."
play = "Press s to start!"
occupied = "The cell is already occupied!"
win = "You won!"
lose = "Sorry!, try again."
tie = "The game is a tie!"
# Initialize program
pygame.init()
font01 = pygame.font.Font(pygame.font.get_default_font(), 30)
font02 = pygame.font.Font(pygame.font.get_default_font(), 15)

# Assign FPS a value
FPS = 15
FramePerSec = pygame.time.Clock()
 
# Setting up color objects
BLUE  = (0, 0, 255)
# RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
# Setup a 300x300 pixel display with caption
screen = pygame.display.set_mode((500,500))
screen.fill(BLACK)
pygame.display.set_caption(title)
 
# Creating Lines and Shapes
pygame.draw.line(screen, WHITE, (200, 100), (200, 400), 10)
pygame.draw.line(screen, WHITE, (300, 100), (300, 400), 10)
pygame.draw.line(screen, WHITE, (100, 200), (400, 200), 10)
pygame.draw.line(screen, WHITE, (100, 300), (400, 300), 10)
#pygame.draw.line(screen, BLUE, (150,130), (170,170))
#pygame.draw.line(screen, GREEN, (130,170), (170,170))
#pygame.draw.circle(screen, BLACK, (100,50), 30)
#pygame.draw.circle(screen, BLACK, (200,50), 30)
#pygame.draw.rect(screen, BLUE, (395, 0, 490, 95), 5)
#pygame.draw.rect(screen, BLACK, (110, 260, 80, 5))
titleDisplay = font01.render(title, True, (255, 255, 255))
screen.blit(titleDisplay, dest=(170,50))
move01 = font02.render("Computer: X", True, BLUE)
screen.blit(move01, dest=(393,20))
move02= font02.render("You: O", True, BLUE)
screen.blit(move02, dest=(440,40))
pygame.display.update()
# Beginning Game Loop
while True:
    pygame.display.update(100, 100,400, 500)
    #for event in pygame.event.get():
        #if event.type == QUIT:
            #pygame.quit()
            #sys.exit()
   
    #FramePerSec.tick(FPS)
