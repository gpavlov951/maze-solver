import time
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
        ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        
        self._create_cells()
    
    def _create_cells(self):
        # Initialize the cells as a 2D grid (list of lists)
        self._cells = [[Cell(self._win) for _ in range(self._num_cols)] for _ in range(self._num_rows)]
        
        # Draw each cell
        for i in range(self._num_rows):
            for j in range(self._num_cols):
                self._draw_cell(i, j)
    
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