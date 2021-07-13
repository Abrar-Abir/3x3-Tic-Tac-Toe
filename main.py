import pygame, sys
from pygame.locals import *
import random
# Variable Declaration
title = "Tic-Tac-Toe"
message = "Click to move!"
play = "Press s to start!"
occupied = "The cell is already occupied!"
win = "You won!"
lose = "Sorry!, try again."
tie = "The game is a tie!"
cells = [0, 1, 2, 3, 4, 5, 6, 7, 8]
moves = []
cross = []
circle = []
# Initialize program
pygame.init()
font01 = pygame.font.Font(pygame.font.get_default_font(), 30)
font02 = pygame.font.Font(pygame.font.get_default_font(), 15)

# Assign FPS a value
FPS = 15
FramePerSec = pygame.time.Clock()
 
# Color
BLUE  = (0, 0, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Functions
def check(cell1, cell2, cell3):
	term1 = max(cell1, cell2, cell3)
	term3 = min(cell1, cell2, cell3)
	return 2*(cell1 + cell2 + cell3) - 3*(term1 + term3) == 0

def match(cells):
	length = len(cells)
	if length > 2:
		for i in range(length):
			for j in range(length - i - 1):
				for k in range(length - i - j- 1):
					if check(cells[i], cells[i+1:][j], cells[i+j+1:][k]):
						message = "Game Over!"
						messageDisplay = font01.render(message, True, GREEN)
						pygame.draw.rect(screen, BLACK, (100, 400, 400, 500), 0)
						screen.blit(messageDisplay, dest=(100, 410))
						return True
	return False
def drawCross(cells):
	cell = random.choice(cells)
	row, column = cell//3 + 1, cell%3 + 1
	pygame.draw.line(screen, WHITE, (column*100 + 10, row*100 + 10), (column*100 + 90, row*100 + 90), 10)
	pygame.draw.line(screen, WHITE, (column*100 + 10, row*100 + 90), (column*100 + 90, row*100 + 10), 10)
	cross.append((row - 1)*3 + (column - 1))
	cells.remove((row - 1)*3 + (column - 1))
def pos2grid (position): # row 1-3, column 1-3
	x, y = position
	return (y - 100)//100 + 1, (x - 100)//100 + 1
#def drawCirc(position):
	#row, column = pos2grid (position)
	#pygame.draw.circle(screen, WHITE, (column*100 + 50, row*100 + 50), 40, 10)
def clickMouse(position):
	x, y = position
	if x > 400 or y > 400 or x < 100 or y < 100:
		message = "You clicked out of Board!"
	elif x % 100 < 5 or x % 100 > 95 or y % 100 < 5 or y % 100 > 95:
		message = "You clicked on the border!"
	else:
		message = "Nice Move!"
		row, column = pos2grid (position)
		pygame.draw.circle(screen, WHITE, (column*100 + 50, row*100 + 50), 40, 10)
		cell = (row - 1)*3 + (column - 1)
		
		if cell in cells:
			cells.remove(cell)
			circle.append(cell)
	messageDisplay = font01.render(message, True, GREEN)
	pygame.draw.rect(screen, BLACK, (100, 400, 400, 500), 0)
	screen.blit(messageDisplay, dest=(100, 410))
# Display
screen = pygame.display.set_mode((500,500))
screen.fill(BLACK)
pygame.display.set_caption(title)
 
# Board
pygame.draw.line(screen, WHITE, (200, 100), (200, 400), 10)
pygame.draw.line(screen, WHITE, (300, 100), (300, 400), 10)
pygame.draw.line(screen, WHITE, (100, 200), (400, 200), 10)
pygame.draw.line(screen, WHITE, (100, 300), (400, 300), 10)
titleDisplay = font01.render(title, True, (255, 255, 255))
screen.blit(titleDisplay, dest=(170,50))
move01 = font02.render("Computer: X", True, BLUE)
screen.blit(move01, dest=(393,20))
move02= font02.render("You: O", True, BLUE)
screen.blit(move02, dest=(440,40))
messageDisplay = font01.render(message, True, GREEN)
screen.blit(messageDisplay, dest=(100, 410))
#screen,blit(messageDisplay, dest=(110, 410))
pygame.display.update()

# Beginning Game Loop
while True:
	pygame.display.update(100, 100, 400, 500)
	drawCross(cells)
	for event in pygame.event.get():
		if event.type == pygame.MOUSEBUTTONUP:
			pos = pygame.mouse.get_pos()
			clickMouse(pos)
			if match(circle) == False:
				drawCross(cells)
				if match(cross):
					#pygame.quit()
					cross = []
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	
	FramePerSec.tick(FPS)
