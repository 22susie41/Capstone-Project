
import tkinter
import random
import time



# easy = 6 bombs
# medium = 8 bombs
# hard = 


grid = [
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0]
]

for row in range(len(grid)):
    for col in range(len(grid[row])):
        print(grid[row][col], end="")
    print("")
