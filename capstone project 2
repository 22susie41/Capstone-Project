# Capstone-Project
import turtle
import math

WIDTH = 600
HEIGHT = 600

wn = turtle.Screen()
wn.title("Minesweepers")

wn.setup(WIDTH, HEIGHT)

pen = turtle.Turtle()
pen.shape("square")
pen.hideturtle()
pen.penup()
pen.speed(0)

# easy = 6 bombs
# medium = 8 bombs
# hard = 12


FLAG = -2
UNKNOWN = -1
EMPTY = 0
MINE = 1
NUMBER = 2


grid = [
    [0,0,1,1,0,0,1,0,0],
    [0,0,1,0,0,1,0,1,0],
    [1,1,0,1,0,0,0,0,0],
    [0,1,1,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,1,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,1,0,0,0,0,0,0,0]
]


player_grid = [
    [-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1]
]


def print_grid(grid):
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            symbol = grid[row][col]
            if symbol == UNKNOWN:
                symbol = "."
            if symbol == FLAG:
                symbol = "F"
            print(symbol, end="")
        print("")


def count_bombs(row, col):
    # Count bombs
    count = 0
    
    offsets = ((-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1))
    
    for offset in offsets:
        new_row = row + offset[0]
        new_col = col + offset[1]
        
        if new_row >= 0 and new_row <=8 and new_col >=0 and new_col <=8:
            if grid[new_row][new_col] == MINE:
                count+=1
            
    return count

def user_choice(row, col):
    
    # Check for bomb
    if(grid[row][col] == MINE):
        print("BOOM")

    # Check number of bombs in the cell
    # If it is greater than zero stop
    if count_bombs(row, col) > 0:
        player_grid[row][col] = count_bombs(row, col)
        
    else:
        # Search
        cells = [(row,col)]
        
        offsets = ((-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1))
        
        while len(cells) > 0:
            cell = cells.pop()
            for offset in offsets:
                row = offset[0] + cell[0]
                col = offset[1] + cell[1]
                if((row>=0 and row<=8) and (col>=0 and col<=8)):
                    if((player_grid[row][col]==UNKNOWN) and (grid[row][col]==EMPTY)):
                        player_grid[row][col] = count_bombs(row,col)

                        if count_bombs(row,col) == EMPTY and (row,col) not in cells:
                            cells.append((row,col))
                        else:
                            player_grid[row][col] = count_bombs(row,col)
                
            

def set_flag(row, col):
    if player_grid[row][col] == FLAG:
        player_grid[row][col] = UNKNOWN
    elif player_grid[row][col] == UNKNOWN:
        player_grid[row][col] = FLAG

def reset():
    pass

user_choice(0,0)
set_flag(4, 4)


print_grid(grid)
print()
print_grid(player_grid)

def screen_to_grid(x, y):
    grid_width = 9
    grid_height = 9
    cell_size = 20
    
    center_to_left = cell_size * (grid_width / 2.0)
    center_to_top = cell_size * (grid_height / 2.0)

    max_row_value = grid_height - 1
        
    col = math.floor((x+center_to_left)/cell_size)
    row = max_row_value-math.floor((y+center_to_left)/cell_size)
    
    user_choice(row, col)
    draw_grid(player_grid, pen)




def draw_grid(grid, pen):
    pen.clear()
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            x = -80 + col * 20
            y = 80 - row * 20
            pen.goto(x, y)
            pen.shapesize(0.9, 0.9)
            if grid[row][col] == UNKNOWN:
                pen.color("grey")
            elif grid[row][col] == FLAG:
                pen.color("red")
            else:
                pen.color("blue")
            pen.stamp()



wn.onclick(screen_to_grid)



draw_grid(player_grid, pen)

turtle.mainloop()
