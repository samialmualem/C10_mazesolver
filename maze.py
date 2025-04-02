import time
from graphics import *
from tkinter import Tk, Canvas, BOTH
from random import seed, randint

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
        seed_value=None
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win

        if seed_value is not None:
            seed(seed_value) 


        self._create_cells()
    
    def _create_cells(self):
        self._cells = []
        for j in range(self._num_cols):
            col = []
            for i in range(self._num_rows):
                x1 = self._x1 + j * self._cell_size_x
                y1 = self._y1 + i * self._cell_size_y
                x2 = x1 + self._cell_size_x
                y2 = y1 + self._cell_size_y
                cell = Cell(x1, y1, x2, y2, self._win)
                
                col.append(cell)
            self._cells.append(col)

        for j in range(self._num_cols):
            for i in range(self._num_rows):
                self._draw_cell(j, i)

    def _draw_cell(self, j, i, fill_color='white'):
        self._cells[j][i].x1 = self._x1 + j * self._cell_size_x
        self._cells[j][i].y1 = self._y1 + i * self._cell_size_y
        self._cells[j][i].x2 = self._cells[j][i].x1 + self._cell_size_x
        self._cells[j][i].y2 = self._cells[j][i].y1 + self._cell_size_y

        self._cells[j][i].draw(self._win, fill_color)

    def _animate(self):
        for i in range(self._num_rows):
            for j in range(self._num_cols):
                self._draw_cell(j, i, 'gray')
                self._win.redraw()
                time.sleep(0.005)

    def _break_entrance_and_exit(self):
        # Remove the walls of the (0,0) cell (entrance) and the (num_rows-1,num_cols-1) cell (exit)
        self._cells[0][0].has_top_wall = False
        self._cells[0][0].draw(self._win, 'white')
        self._cells[self._num_cols -1][self._num_rows -1].has_bottom_wall = False
        self._cells[self._num_cols -1][self._num_rows -1].draw(self._win, 'white')

    def _break_walls_r(self, j, i):
        # Mark the current cell as visited
        self._cells[j][i].visited = True

        # In an infinite loop:
        while True:
            # Create a new empty list to hold the j and i values you will need to visit.
            to_visit = []

            # Check the cells that are directly adjacent to the current cell. 
            # Keep track of any that have not been visited as "possible directions" to move to.
            # Check the cell to the left
            if j > 0 and not self._cells[j - 1][i].visited:
                to_visit.append('left')
            # Check the cell to the right 
            if j < self._num_cols - 1 and not self._cells[j + 1][i].visited:
                to_visit.append('right')
            # Check the cell above
            if i > 0 and not self._cells[j][i - 1].visited:
                to_visit.append('up')
            # Check the cell below
            if i < self._num_rows - 1 and not self._cells[j][i + 1].visited:
                to_visit.append('down')
            # If there are no unvisited cells, draw the current cell and return to break out of the loop.
            if not to_visit:
                self._draw_cell(j, i)
                return
            

            # Choose a random direction from the list of possible directions. Use the random module to do this, and
            # use the seed value to ensure that the random choice is reproducible.
            

            direction = randint(0, len(to_visit) - 1)

            # Knock down the walls between the current cell and the chosen cell.
            # Move to the chosen cell by recursively calling _break_walls_r
            if to_visit[direction] == 'left':
                self._cells[j][i].has_left_wall = False
                self._cells[j - 1][i].has_right_wall = False
                self._draw_cell(j, i)
                self._draw_cell(j - 1, i)
                self._break_walls_r(j - 1, i)
            elif to_visit[direction] == 'right':
                self._cells[j][i].has_right_wall = False
                self._cells[j + 1][i].has_left_wall = False
                self._draw_cell(j, i)
                self._draw_cell(j + 1, i)
                self._break_walls_r(j + 1, i)
            elif to_visit[direction] == 'up':
                self._cells[j][i].has_top_wall = False
                self._cells[j][i - 1].has_bottom_wall = False
                self._draw_cell(j, i)
                self._draw_cell(j, i - 1)
                self._break_walls_r(j, i - 1)
            elif to_visit[direction] == 'down':
                self._cells[j][i].has_bottom_wall = False
                self._cells[j][i + 1].has_top_wall = False
                self._draw_cell(j, i)
                self._draw_cell(j, i + 1)
                self._break_walls_r(j, i + 1)


    def _reset_cells_visited(self):
        for j in range(self._num_cols):
            for i in range(self._num_rows):
                self._cells[j][i].visited = False
                self._draw_cell(j, i, 'white')


    def solve(self):
        # Call _solve_r with the current cell
        result = self._solve_r(0, 0)
        if not result:
            return False # No solution found
        return True # All cells have been solved
    

    def _solve_r(self, j, i):
        # The _solve_r method returns True if the current cell is an end cell, OR if it leads to the end cell. 
        # It returns False if the current cell is a loser cell.

        # Call the _animate method.
        self._animate()

        # Mark the current cell as visited.
        self._cells[j][i].visited = True

        # If you are at the "end" cell (the goal) then return True.
        if j == self._num_cols - 1 and i == self._num_rows - 1:
            return True
        
        # For each direction, 
        # if there is a cell in that direction, there is no wall blocking you, and that cell hasn't been visited:
        # 1. Draw a move between the current cell and that cell.
        # 2. Call _solve_r recursively to move to that cell. 
        # 3. If that cell returns True, then just return True and don't worry about the other directions.
        #    Otherwise, draw an "undo" move between the current cell and the next cell

        # 4. If none of the cells return True, then return False.
        # Check the cell to the left
        if j > 0 and not self._cells[j - 1][i].visited and not self._cells[j][i].has_left_wall:
            self._cells[j][i].draw_move(self._cells[j - 1][i])
            if self._solve_r(j - 1, i):
                return True
            else:
                self._cells[j][i].draw_move(self._cells[j - 1][i], undo=True)
        # Check the cell to the right
        if j < self._num_cols - 1 and not self._cells[j + 1][i].visited and not self._cells[j][i].has_right_wall:
            self._cells[j][i].draw_move(self._cells[j + 1][i])
            if self._solve_r(j + 1, i):
                return True
            else:
                self._cells[j][i].draw_move(self._cells[j + 1][i], undo=True)
        # Check the cell above
        if i > 0 and not self._cells[j][i - 1].visited and not self._cells[j][i].has_top_wall:
            self._cells[j][i].draw_move(self._cells[j][i - 1])
            if self._solve_r(j, i - 1):
                return True
            else:
                self._cells[j][i].draw_move(self._cells[j][i - 1], undo=True)
        # Check the cell below
        if i < self._num_rows - 1 and not self._cells[j][i + 1].visited and not self._cells[j][i].has_bottom_wall:
            self._cells[j][i].draw_move(self._cells[j][i + 1])
            if self._solve_r(j, i + 1):
                return True
            else:
                self._cells[j][i].draw_move(self._cells[j][i + 1], undo=True)
        # If none of the cells return True, then return False.
        return False
