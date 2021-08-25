#add button to remove val
import pygame
import random
import copy
 
pygame.font.init()
 
width = 500
height = 600
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
 
pygame.display.set_caption("Sudoku")
 
x = 0
y = 0
dif = width / 9
val = 0
grid = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]
prev_grid = copy.deepcopy(grid) 

board_font = pygame.font.SysFont("comicsans", 40)
text_font = pygame.font.SysFont("comicsans", 20)

def get_cord(pos):
    global x
    x = pos[0]//dif
    global y
    y = pos[1]//dif
 
def draw_box():
    for i in range(2):
        pygame.draw.line(screen, (255, 0, 0), (x * dif - 3, (y + i) * dif), (x * dif + dif + 3, (y + i) * dif), 7)
        pygame.draw.line(screen, (255, 0, 0), ( (x + i )* dif, y * dif ), ((x + i) * dif, y * dif + dif), 7)  
        
def draw():
    for i in range (9):
        for j in range (9):
            if grid[i][j]!= 0:

                pygame.draw.rect(screen, (144,238,144), (i * dif, j * dif, dif + 1, dif + 1))
 
                text1 = board_font.render(str(grid[i][j]), True, (0, 0, 0))
                screen.blit(text1, (i * dif + 15, j * dif + 15))    

    for i in range(10):
        if i % 3 == 0 :
            line_thick = 7
        else:
            if width > 800:
                line_thick = 2
            else:
                line_thick = 1
        pygame.draw.line(screen, (0, 0, 0), (0, i * dif), (width, i * dif), line_thick)
        pygame.draw.line(screen, (0, 0, 0), (i * dif, 0), (i * dif, width), line_thick)     

#==========================================================================

def valid(grid, i, j, val):
    for it in range(9):
        if grid[i][it]== val:
            return False
        if grid[it][j]== val:
            return False
    it = i//3
    jt = j//3

    for i in range(it * 3, it * 3 + 3):
        for j in range (jt * 3, jt * 3 + 3):
            if grid[i][j]== val:
                return False
    return True
 
def solve(grid, i, j):
    while grid[i][j]!= 0:
        if i < 8:
            i += 1
        elif i == 8 and j<8:
            i = 0
            j += 1
        elif i == 8 and j == 8:
            return True
    pygame.event.pump()   
    for it in range(1, 10):
        if valid(grid, i, j, it):
            grid[i][j]= it
            global x, y
            x = i
            y = j
            screen.fill((255, 255, 255))
            draw()
            draw_box()
            pygame.display.update()
            pygame.time.delay(10)
            if solve(grid, i, j):
                return True
            else:
                grid[i][j]= 0
            screen.fill((255, 255, 255))
         
            draw()
            draw_box()
            pygame.display.update()
            pygame.time.delay(30)   
    return False 

#==========================================================================

def generate_grid():
    new_grid =[
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    fill_diagonal(new_grid)
    fill_rest(new_grid, 0, 0)
    remove(new_grid, random.randint(50, 65))
    return new_grid

def valid_in_box(new_grid, i, j, val):
    it = i//3
    jt = j//3
    for i in range(it * 3, it * 3 + 3):
        for j in range (jt * 3, jt * 3 + 3):
            if new_grid[i][j]== val:
                return False
    return True

def fill_box(new_grid, i, j):
    it = i//3
    jt = j//3
    for i in range(it * 3, it * 3 + 3):
        for j in range (jt * 3, jt * 3 + 3):
            num = random.randint(1, 9)
            while(valid_in_box(new_grid, i, j, num) == False):
                num = random.randint(1, 9)
            new_grid[i][j] = num
            
def fill_diagonal(new_grid):
    for i in range(0,9,3):
        fill_box(new_grid, i,i)

def remove(new_grid, n):
    for i in range(n):
        tmp_x = random.randint(0, 8)
        tmp_y = random.randint(0, 8)
        if(new_grid[tmp_x][tmp_y] != 0):
            new_grid[tmp_x][tmp_y] =0
        else:
            i -= 1

def fill_rest(new_grid, i, j):
    while new_grid[i][j]!= 0:
        if i < 8:
            i += 1
        elif i == 8 and j<8:
            i = 0
            j += 1
        elif i == 8 and j == 8:
            return True 
    for it in range(1, 10):
        if valid(new_grid, i, j, it):
            new_grid[i][j]= it
            if fill_rest(new_grid, i, j):
                return True
            else:
                new_grid[i][j]= 0
    return False 
#==========================================================================

run = True
has_user_input = False
want_to_solve = False
has_solved = False
unsolvable = False
while run:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 
        if event.type == pygame.MOUSEBUTTONDOWN:
            has_user_input = True
            pos = pygame.mouse.get_pos()
            get_cord(pos)
        if event.type == pygame.VIDEORESIZE:
            width, height = event.size
            if width < 500:
                width = 500
            if height < 600:
                height = 600
            if height - 100 < width :
                height = 100+width

            board_font = pygame.font.SysFont("comicsans", int((40/500)*width))
            text_font = pygame.font.SysFont("comicsans", int((20/500)*width))
            dif = width/9

            screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
            pygame.display.update()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                val = 1
            if event.key == pygame.K_2:
                val = 2   
            if event.key == pygame.K_3:
                val = 3
            if event.key == pygame.K_4:
                val = 4
            if event.key == pygame.K_5:
                val = 5
            if event.key == pygame.K_6:
                val = 6
            if event.key == pygame.K_7:
                val = 7
            if event.key == pygame.K_8:
                val = 8
            if event.key == pygame.K_9:
                val = 9 

            if event.key == pygame.K_RETURN:
                want_to_solve = True

            if event.key == pygame.K_n:
                has_solved = False
                unsolvable = False
                want_to_solve = False
                grid = generate_grid()
                prev_grid = copy.deepcopy(grid) 

            if event.key == pygame.K_r:
                want_to_solve = False
                has_solved = False
                unsolvable = False
                grid = copy.deepcopy(prev_grid)

    if want_to_solve  == True:
        grid = copy.deepcopy(prev_grid) 
        if solve(grid, 0, 0) == False:
            unsolvable = True
        else:
            has_solved = True
        want_to_solve  = False   

    if val != 0:           
        text1 = board_font.render(str(val), True, (0, 0, 0))
        screen.blit(text1, (x * dif + 15, y * dif + 15)) 

        if valid(grid, int(x), int(y), val) and prev_grid[int(x)][int(y)] == 0:
            grid[int(x)][int(y)]= val
            has_user_input = False

        elif valid(grid, int(x), int(y), val) == False and prev_grid[int(x)][int(y)] == 0:
            grid[int(x)][int(y)]= 0

            text1 = text_font.render("Invalid input", True, (0, 0, 0))
            screen.blit(text1, (20, height-30))  
        val = 0   
    
    #if grid is generated correctly this message should never appear
    if unsolvable == True:
        text1 = text_font.render("Unsolvable", True, (0, 0, 0))
        screen.blit(text1, (20, height-30))

    if has_solved == True:
        text1 = text_font.render("Grid has been solved!", True, (0, 0, 0))
        screen.blit(text1, (20, height-30))    

    draw() 
    if has_user_input == True:
        draw_box()      

    text1 = text_font.render("Press N for new grid / R revert the grid", True, (0, 0, 0))
    text2 = text_font.render("Press Enter to auto solve / Click and type to enter numbers", True, (0, 0, 0))
    screen.blit(text1, (20, height-80))       
    screen.blit(text2, (20, height-60))  
 
    pygame.display.update() 
   
pygame.quit() 