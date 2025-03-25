import time
import random
from cell import Cell

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
            seed=None
        ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        
        if seed is not None:
            random.seed(seed)
        
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls()
        self._reset_cells_visited()
    
    def solve(self):
        """
        Solve the maze using a depth-first algorithm.
        Returns True if the maze was solved, False otherwise.
        """
        # Reset visited flags before solving
        self._reset_cells_visited()
        # Start solving from the entrance cell (top-left)
        return self._solve_r(0, 0)
    
    def _solve_r(self, i, j):
        """
        Recursive helper method for solving the maze.
        Returns True if the current cell is the end cell or leads to it.
        Returns False if the current cell is a dead end.
        """
        # Animate the solving process
        self._animate()
        
        # Mark the current cell as visited
        self._cells[i][j].visited = True
        
        # If we reached the end cell (bottom-right), we solved the maze
        if i == self._num_rows - 1 and j == self._num_cols - 1:
            return True
        
        # Try each direction: up, right, down, left
        
        # Up
        if i > 0 and not self._cells[i][j].has_top_wall and not self._cells[i-1][j].visited:
            # Draw a move to the cell above
            self._cells[i][j].draw_move(self._cells[i-1][j])
            
            # If the path through the cell above leads to the end, we're done
            if self._solve_r(i-1, j):
                return True
            
            # Otherwise, undo the move (it's a dead end)
            self._cells[i][j].draw_move(self._cells[i-1][j], True)
        
        # Right
        if j < self._num_cols - 1 and not self._cells[i][j].has_right_wall and not self._cells[i][j+1].visited:
            # Draw a move to the cell to the right
            self._cells[i][j].draw_move(self._cells[i][j+1])
            
            # If the path through the cell to the right leads to the end, we're done
            if self._solve_r(i, j+1):
                return True
            
            # Otherwise, undo the move (it's a dead end)
            self._cells[i][j].draw_move(self._cells[i][j+1], True)
        
        # Down
        if i < self._num_rows - 1 and not self._cells[i][j].has_bottom_wall and not self._cells[i+1][j].visited:
            # Draw a move to the cell below
            self._cells[i][j].draw_move(self._cells[i+1][j])
            
            # If the path through the cell below leads to the end, we're done
            if self._solve_r(i+1, j):
                return True
            
            # Otherwise, undo the move (it's a dead end)
            self._cells[i][j].draw_move(self._cells[i+1][j], True)
        
        # Left
        if j > 0 and not self._cells[i][j].has_left_wall and not self._cells[i][j-1].visited:
            # Draw a move to the cell to the left
            self._cells[i][j].draw_move(self._cells[i][j-1])
            
            # If the path through the cell to the left leads to the end, we're done
            if self._solve_r(i, j-1):
                return True
            
            # Otherwise, undo the move (it's a dead end)
            self._cells[i][j].draw_move(self._cells[i][j-1], True)
        
        # If none of the directions worked out, this cell is a dead end
        return False
    
    def _create_cells(self):
        # Initialize the cells as a 2D grid (list of lists)
        self._cells = [[Cell(self._win) for _ in range(self._num_cols)] for _ in range(self._num_rows)]
        
        # Draw each cell
        for i in range(self._num_rows):
            for j in range(self._num_cols):
                self._draw_cell(i, j)
    
    def _break_entrance_and_exit(self):
        # Break the top wall of the entrance cell (top-left)
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        
        # Break the bottom wall of the exit cell (bottom-right)
        self._cells[self._num_rows-1][self._num_cols-1].has_bottom_wall = False
        self._draw_cell(self._num_rows-1, self._num_cols-1)
    
    def _break_walls(self):
        # Start the recursive wall-breaking process from the entrance cell
        self._break_walls_r(0, 0)
    
    def _reset_cells_visited(self):
        # Reset the visited property of all cells to False
        for i in range(self._num_rows):
            for j in range(self._num_cols):
                self._cells[i][j].visited = False
    
    def _break_walls_r(self, i, j):
        # Mark the current cell as visited
        self._cells[i][j].visited = True
        
        # Loop until we can't go any further
        while True:
            # Create a list to hold possible directions
            possible_directions = []
            
            # Check adjacent cells (up, right, down, left)
            # Up
            if i > 0 and not self._cells[i-1][j].visited:
                possible_directions.append((i-1, j, "up"))
            # Right
            if j < self._num_cols-1 and not self._cells[i][j+1].visited:
                possible_directions.append((i, j+1, "right"))
            # Down
            if i < self._num_rows-1 and not self._cells[i+1][j].visited:
                possible_directions.append((i+1, j, "down"))
            # Left
            if j > 0 and not self._cells[i][j-1].visited:
                possible_directions.append((i, j-1, "left"))
            
            # If there are no possible directions, break out of the loop
            if len(possible_directions) == 0:
                self._draw_cell(i, j)
                return
            
            # Choose a random direction
            direction_index = random.randrange(len(possible_directions))
            next_i, next_j, direction = possible_directions[direction_index]
            
            # Break down the walls between the current cell and the chosen cell
            if direction == "up":
                self._cells[i][j].has_top_wall = False
                self._cells[next_i][next_j].has_bottom_wall = False
            elif direction == "right":
                self._cells[i][j].has_right_wall = False
                self._cells[next_i][next_j].has_left_wall = False
            elif direction == "down":
                self._cells[i][j].has_bottom_wall = False
                self._cells[next_i][next_j].has_top_wall = False
            elif direction == "left":
                self._cells[i][j].has_left_wall = False
                self._cells[next_i][next_j].has_right_wall = False
            
            # Redraw the current cell to show the wall removal
            self._draw_cell(i, j)
            
            # Recursively visit the chosen cell
            self._break_walls_r(next_i, next_j)
    
    def _draw_cell(self, i, j):
        # Check if win exists
        if self._win is None:
            return 

        # Calculate the position of the cell based on its indices, cell size and maze position
        x1 = self._x1 + j * self._cell_size_x
        y1 = self._y1 + i * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        
        # Draw the cell
        self._cells[i][j].draw(x1, y1, x2, y2)
        
        # Animate the drawing
        self._animate()
    
    def _animate(self):
        # Check if win exists
        if self._win is None:
            return 

        # Redraw the window and pause briefly to visualize the maze creation
        self._win.redraw()
        time.sleep(0.05) 