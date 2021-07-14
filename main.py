import pygame, sys
from pygame.locals import *
import random

# Variable Declaration
title = "Tic-Tac-Toe"
cells = [0, 1, 2, 3, 4, 5, 6, 7, 8]
cross = []
circle = []
start = False
play = False
player = 2

# Initialize program
pygame.init()
font01 = pygame.font.Font(pygame.font.get_default_font(), 30)
font02 = pygame.font.Font(pygame.font.get_default_font(), 15)

# Assign FPS a value
FPS = 15
FramePerSec = pygame.time.Clock()
 
# Color
RED = (255, 0, 0)
BLUE  = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Display
screen = pygame.display.set_mode((500,500))
screen.fill(BLACK)
pygame.display.set_caption(title)

# Functions

def message(line):
	messageDisplay = font01.render(line, True, GREEN)
	pygame.draw.rect(screen, BLACK, (100, 400, 500, 500), 0)
	screen.blit(messageDisplay, dest=(100, 410))
	
def resetAll():
	screen.fill(BLACK)
	pygame.draw.line(screen, YELLOW, (200, 100), (200, 400), 8)
	pygame.draw.line(screen, YELLOW, (300, 100), (300, 400), 8)
	pygame.draw.line(screen, YELLOW, (100, 200), (400, 200), 8)
	pygame.draw.line(screen, YELLOW, (100, 300), (400, 300), 8)
	titleDisplay = font01.render(title, True, (255, 255, 255))
	screen.blit(titleDisplay, dest=(170,50))
	move01 = font02.render("Computer: X", True, GREEN)
	screen.blit(move01, dest=(393,20))
	move02= font02.render("You: O", True, GREEN)
	screen.blit(move02, dest=(440,40))
	inst01 = font02.render("Play: P", True, GREEN)
	screen.blit(inst01, dest=(20,20))
	inst02= font02.render("Retry: R", True, GREEN)
	screen.blit(inst02, dest=(20,40))
	inst03= font02.render("Exit: E", True, GREEN)
	screen.blit(inst03, dest=(20,60))
	message("Ready? Press 'p' to play!")
	pygame.display.update()
	
def check(cell1, cell2, cell3): # checks if 
	if cell1 % 3 == cell2 % 3 == cell3 % 3:
		return True
	elif cell1//3 == cell2//3 == cell3//3:
		return True
	elif cell1 % 2 == cell2 % 2 == cell3 % 2 == 0 and cell1 + cell2 + cell3 == 12:
		return True
	return False

def matchOver(moves): # checks if game over
	length = len(moves)
	if length > 2:
		for i in range(length):
			for j in range(i + 1, length):
				for k in range(i + j + 1, length):
					if check(moves[i], moves[j], moves[k]):
						if len(cells) % 2 == player:
							message("Sorry! Press 'r' to retry!")
							color = BLUE
						else:
							message("Congratulations! You Win")
							color = RED
						start = min(moves[i], moves[j], moves[k])
						end = max(moves[i], moves[j], moves[k])
						pygame.draw.line(screen, color, ((start % 3 + 1)*100 + 50, (start//3 + 1)*100 + 50), ((end % 3 + 1)*100 + 50, (end//3 + 1)*100 + 50), 10)
						return True
	return False

def matchTie(cells): # checks if match is tie
	if len(cells) == 0:
		message("Tie! Press 'R' to retry")
		return True
	return False

def matchCell(moves):
	length = len(moves)
	cell = 9
	if length > 1:
		for i in range(length):
			for j in range(i + 1, length):
				cell1 = moves[i]
				cell2 = moves[j]
				if cell1 % 3 == cell2 % 3:
					cell = (3 - (cell1//3) - (cell2//3))*3 + (cell1 % 3)
				elif cell1//3 == cell2//3:
					cell = (3 - (cell1 % 3) - (cell2 % 3)) + (cell1//3)*3
				elif cell1 % 2 == cell2 % 2 == 0 and (cell1 == 4 or cell2 == 4):
					cell = 12 - cell1 - cell2
	return cell

def drawCross(cells): # computer takes move
	if 4 in cells:
		cell = 4
	elif len(cells) == 8:
		cell = random.choice([0, 2, 6, 8])
	elif matchCell(cross) != 9 and matchCell(cross) in cells:
		cell = matchCell(cross)
	elif matchCell(circle) != 9 and matchCell(circle) in cells:
		cell = matchCell(circle)
	elif len(cells) == 6 and circle[0] % 2 == circle[1] % 2 == 0:
		cell = random.choice([i for i in cells if i % 2 == 0])
	else:
		cell = random.choice(cells)
	row, column = cell//3 + 1, cell%3 + 1
	pygame.draw.line(screen, BLUE, (column*100 + 10, row*100 + 10), (column*100 + 90, row*100 + 90), 10)
	pygame.draw.line(screen, BLUE, (column*100 + 10, row*100 + 90), (column*100 + 90, row*100 + 10), 10)
	cross.append((row - 1)*3 + (column - 1))
	cells.remove((row - 1)*3 + (column - 1))

def clickMouse(position): # User's move
	x, y = position
	if x > 400 or y > 400 or x < 100 or y < 100:
		message("You clicked out of Board!")
	elif x % 100 < 5 or x % 100 > 95 or y % 100 < 5 or y % 100 > 95:
		message("You clicked on the border!")
	else:
		row, column = (y - 100)//100 + 1, (x - 100)//100 + 1
		cell = (row - 1)*3 + (column - 1)
		if cell not in cells:
			message("The cell is preoccupied!")
		else:
			return True
	return False

def drawCirc(position): # draws user's move
	x, y = position
	row, column = (y - 100)//100 + 1, (x - 100)//100 + 1
	cell = (row - 1)*3 + (column - 1)
	cells.remove(cell)
	circle.append(cell)
	pygame.draw.circle(screen, RED, (column*100 + 50, row*100 + 50), 40, 10)
	message("Nice move! Carry On!")

# Beginning Game Loop
resetAll()
play = False
while True:
	pygame.display.update(100, 100, 400, 500)
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_p and start == False:
				play = True
				message("Want to go first? Y/N")
			elif event.key == pygame.K_y and start == False and play == True:
				player = 1
				start = True
				message("Click & take move!")
				if event.type == pygame.MOUSEBUTTONUP:
					pos = pygame.mouse.get_pos()
					if clickMouse(pos):
						drawCirc(pos)
						drawCross(cells)
			elif event.key == pygame.K_n and start == False and play == True:
				player = 0
				start = True
				drawCross(cells)
				message("Click & Take your move!")
			elif event.key == pygame.K_r:
				resetAll()
				cells = [0, 1, 2, 3, 4, 5, 6, 7, 8]
				cross = []
				circle = []
				start = False
			elif event.key == pygame.K_e:
				pygame.quit()
				sys.exit()
		if start:
			if event.type == pygame.MOUSEBUTTONUP:
				pos = pygame.mouse.get_pos()
				if clickMouse(pos):
					drawCirc(pos)
					if matchOver(circle):
						start = False
					elif matchTie(cells):
						start = False
					else:
						drawCross(cells)
						if matchOver(cross):
							start = False
						elif matchTie(cells):
							start = False		
				else:
					break
	FramePerSec.tick(FPS)
