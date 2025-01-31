
"""
    Sedat Yıldız 01.02.2025

    Click the Space button to see a new solution

    The most important aspect of this code is in the range of 67...105
"""

import pygame


pygame.init()

#Game Variables
WIDTH, HEIGHT = 800, 800
running = True
WHITE = (255, 255, 255)
BROWN = (165, 42, 42)
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS

solutionindex = 0 # -> we will need that variable to see next solution each time we click Space

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('8 Queen Solution')

Image = pygame.image.load('Queen.png')
queen = pygame.transform.scale(Image, (SQUARE_SIZE, SQUARE_SIZE))

results = []   # -> we will put the solutions here

my_grid = [[None for _ in range(8)] for _ in range(8)]   # -> we will find the squares where we can put a queen

#  Screen Drawing functions

def draw_chessboard():
    for row in range(ROWS):
        for col in range(COLS):
            color = WHITE if (row + col) % 2 == 0 else BROWN
            pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

# put a single queen image to the given coordinates
def draw_Single_Queen(screen,row,col):
    screen.blit(queen, (col * SQUARE_SIZE, row * SQUARE_SIZE))

# this function gets a 2D grid and draw the solution
def draw_All_Queen(grid):
    draw_chessboard()
    for row in range(ROWS):
        for col in range(COLS):
            if grid[row][col] == "Q":
                draw_Single_Queen(screen,row,col)
    pygame.display.update()


# logic Functions
"""
    we need 2 functions to set the logic
    1- Check Queen's position after  we put a queen .it is valid or not
    2- a backtracking recursion algorithm to create solutions
    
    Note: we will put the queen logic base on rows so each time we only put one queen to one row so we dont need to check rows
    
"""

#Cols and diagonals Control
def check_queen(grid,row,col):

    # same col Control
    for i in range(row):
        if grid[i][col] == "Q":
            return False

    # left diagonal Control
    i,j = row,col
    while i >= 0 and j >= 0:
        if grid[i][j] == "Q":
            return False
        i -= 1
        j -= 1

    # right diagonal Control
    i, j = row, col
    while i >= 0 and j < 8:
        if grid[i][j] == "Q":
            return False
        i -= 1
        j += 1

    return True

def findSolutions(grid,row):
    if row == 8:
        # copy the rows of final grid and make it an 2D array then append it to results as solution
        results.append([r.copy() for r in grid])
        return

    for col in range(COLS):
        if check_queen(grid,row,col):
            grid[row][col] = "Q"
            #each time we increase the row so when row reach 8 we can find a solution and append it to the result
            findSolutions(grid,row+1) #Recursion
            #after the modification on grid sometimes we can not find a solution so we have to go back so we need to clear the grid
            grid[row][col] = None # backtracking

#call the findSolutions to create solutions
findSolutions(my_grid,0)
draw_All_Queen(results[solutionindex])

# GAME LOOP
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                draw_All_Queen(results[solutionindex])
                solutionindex += 1
                if solutionindex >= len(results):
                    solutionindex = 0
