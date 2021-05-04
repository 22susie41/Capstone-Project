import os
import turtle
from tkinter import messagebox
import math
import time

WIDTH = 600
HEIGHT = 600

wn = turtle.Screen()
wn.title("Minesweepers")
wn.bgcolor("grey")
wn.tracer(0)

wn.setup(WIDTH, HEIGHT)

pen = turtle.Turtle()
pen.shape("square")
pen.hideturtle()
pen.penup()
pen.speed(0)

#timer pen
pen_2 = turtle.Turtle()
pen_2.shape("square")
pen_2.hideturtle()
pen_2.penup()
pen_2.speed(0)

#number of bombs
pen_3 = turtle.Turtle()
pen_3.shape("square")
pen_3.hideturtle()
pen_3.penup()
pen_3.speed(0)

#bombs text
pen_4 = turtle.Turtle()
pen_4.shape("square")
pen_4.hideturtle()
pen_4.penup()
pen_4.speed(0)


wn.register_shape("mine.gif")
wn.register_shape("flag.gif")
wn.register_shape("play.gif")
wn.register_shape("dead.gif")
wn.register_shape("win.gif")

smiley_state = "play"


FLAG = -2
UNKNOWN = -1
EMPTY = 0
MINE = 1


grid = [
    [0,0,1,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,1,0,0,0,0],
    [0,0,0,0,0,1,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,1,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,1],
    [0,0,0,0,1,0,0,0,0]
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




def is_winner():
    global smiley_state
    bomb_count = 0
    empty_count = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == MINE:
                bomb_count += 1
                
            if player_grid[row][col] > -1:
                empty_count += 1
    
    if empty_count == 81 - bomb_count:
        os.system("afplay win31.mp3&")
        smiley_state = "win"
        draw_smiley(pen)
        wn.update()
        time.sleep(5)
        exit()
    


def draw_numbers(grid, pen):
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            # Check conditions
            if grid[row][col] != UNKNOWN and grid[row][col] != FLAG:
                x = -80 + col * 20
                y = 80 - row * 20
                pen.goto(x, y-10)
                pen.color("white")
                num_of_bombs = count_bombs(row, col)
                pen.write(num_of_bombs, move=False, align="center", font=("Courier", 10, "normal")) 
                

def count_all_bombs(grid):
    num_of_bombs = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == MINE:
                num_of_bombs += 1
    return num_of_bombs
                
def count_all_flags(grid):
    num_of_flags = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == FLAG:
                num_of_flags += 1
    return num_of_flags

#clicking
def user_choice(row, col):
    global smiley_state
    
    # Check for bomb
    if(grid[row][col] == MINE):
        os.system("afplay dead.mp3&")
        smiley_state = "dead"
        draw_smiley(pen)
        pen.goto(0, -150)
        pen.color("black")
        pen.write(f"GAME OVER", align="center", font=("Courier", 40, "normal"))
        draw_mines(grid, pen)
        draw_all_numbers(grid, pen)
        time.sleep(5)
        exit()

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
                        
    is_winner()
    wn.update()
    
def set_flag(row, col):

    if player_grid[row][col] == FLAG:
        player_grid[row][col] = UNKNOWN

    elif player_grid[row][col] == UNKNOWN:
        player_grid[row][col] = FLAG
    
    bombs_left = count_all_bombs(grid)
    flags_left = count_all_flags(player_grid)
    
    pen_3.clear()
    pen_3.goto(200, 210)
    pen_3.color("black")
    pen_3.write(bombs_left-flags_left, align="center", font=("Courier", 32, "normal"))
    
    wn.update()



print_grid(grid)
print()
print_grid(player_grid)

is_winner()


#coordinates to row, col
def screen_to_grid(x, y):
    
    if(y < -200 ) and y:
        messagebox.showinfo("Help", """
        AVOID all the bombs.
        FLAG the bombs by right clicking.
        When you click a bomb, you die.
        The number tells how many bombs are around that tile.
        Click any tile to begin!
        *
        For more information,
        ask Google.
        """)
    else:
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



def screen_to_grid_flag(x, y):
    grid_width = 9
    grid_height = 9
    cell_size = 20
    
    center_to_left = cell_size * (grid_width / 2.0)
    center_to_top = cell_size * (grid_height / 2.0)

    max_row_value = grid_height - 1
        
    col = math.floor((x+center_to_left)/cell_size)
    row = max_row_value-math.floor((y+center_to_left)/cell_size)
    
    set_flag(row, col)
    draw_grid(player_grid, pen)

def draw_smiley(pen):
    if smiley_state == "play":
        pen.shape("play.gif")
    elif smiley_state == "dead":
        pen.shape("dead.gif")
    elif smiley_state == "win":
        pen.shape("win.gif")
    pen.goto(0, 225)
    pen.stamp()
    pen.shape("square")


def draw_grid(grid, pen):
    pen.clear()
    
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            x = -80 + col * 20
            y = 80 - row * 20
            pen.goto(x, y)
            pen.shapesize(0.9, 0.9)
            if grid[row][col] == UNKNOWN:
                pen.color("silver")
            elif grid[row][col] == FLAG:
                pen.color("red")
                pen.shape("flag.gif")
            else:
                pen.color("blue")
            pen.stamp()
            pen.shape("square")
            
    draw_numbers(grid, pen)
    draw_smiley(pen)
    wn.update()


def draw_mines(grid, pen):
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            x = -80 + col * 20
            y = 80 - row * 20
            pen.goto(x, y)
            pen.shapesize(0.9, 0.9)
            if grid[row][col] == MINE:
                pen.color("green")
                pen.shape("mine.gif")
                pen.stamp()
    wn.update()


def draw_all_numbers(grid, pen):
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            x = -80 + col * 20
            y = 80 - row * 20
            pen.goto(x, y-10)
            pen.color("black")
            num_of_bombs = count_bombs(row, col)
            pen.write(num_of_bombs, move=False, align="center", font=("Courier", 10, "normal"))  

    wn.update()


def right_click(x, y):
    print(x,y)

wn.onclick(screen_to_grid)
wn.onclick(screen_to_grid_flag, 2)

draw_grid(player_grid, pen)



elapsed_time = 0

def timer():
    global elapsed_time
    elapsed_time += 1
    pen_2.clear()
    pen_2.goto(-200, 210)
    pen_2.color("black")
    pen_2.write(elapsed_time, align="center", font=("Courier", 32, "normal"))
    wn.update()
    wn.ontimer(timer, 1000)

timer()




#bomb text
pen_4.clear()
pen_4.goto(200, 255)
pen_4.write(f"BOMBS", align="center", font=("Courier", 25, "normal"))
pen_4.goto(-200, 255)
pen_4.write(f"TIME", align="center", font=("Courier", 25, "normal"))
pen_4.goto(0, -230)
pen_4.write(f"HELP", align="center", font=("TmonMonsori", 40, "normal"))



turtle.mainloop()
