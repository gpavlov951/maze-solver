import unittest
from maze import Maze
from unittest.mock import MagicMock

class Tests(unittest.TestCase):
  def test_maze_create_cells(self):
    num_cols = 12
    num_rows = 10
    m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
    self.assertEqual(
        len(m1._cells),
        num_rows,
    )
    self.assertEqual(
        len(m1._cells[0]),
        num_cols,
    )

  def test_maze_cell_initialization_and_visited(self):
    num_cols = 5
    num_rows = 5
    m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
    
    # Test that all cells are properly initialized and marked as visited
    for i in range(num_rows):
        for j in range(num_cols):
            self.assertIsNotNone(m1._cells[i][j])
            self.assertTrue(m1._cells[i][j].visited, f"Cell at ({i}, {j}) was not visited")
            
    # Check entrance and exit specifically
    # Entrance cell (top-left) should have top wall removed
    self.assertFalse(m1._cells[0][0].has_top_wall)
    
    # Exit cell (bottom-right) should have bottom wall removed
    self.assertFalse(m1._cells[num_rows-1][num_cols-1].has_bottom_wall)

  def test_maze_without_window(self):
    num_cols = 3
    num_rows = 3
    m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
    
    # Test that cells are still created even without a window
    self.assertEqual(len(m1._cells), num_rows)
    self.assertEqual(len(m1._cells[0]), num_cols)
    
    # Test that _draw_cell and _animate don't raise errors when win is None
    m1._draw_cell(0, 0)
    m1._animate()

  def test_maze_cell_positions(self):
    num_cols = 2
    num_rows = 2
    cell_size_x = 20
    cell_size_y = 20
    x1, y1 = 10, 10
    
    # Create a mock window for this test
    mock_win = MagicMock()
    mock_win.redraw = MagicMock()
    
    m1 = Maze(x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, mock_win)
    
    # Calculate expected positions
    expected_positions = [
        # row 0, col 0
        (x1, y1, x1 + cell_size_x, y1 + cell_size_y),
        # row 0, col 1
        (x1 + cell_size_x, y1, x1 + 2*cell_size_x, y1 + cell_size_y),
        # row 1, col 0
        (x1, y1 + cell_size_y, x1 + cell_size_x, y1 + 2*cell_size_y),
        # row 1, col 1
        (x1 + cell_size_x, y1 + cell_size_y, x1 + 2*cell_size_x, y1 + 2*cell_size_y)
    ]
    
    # Verify cell positions
    self.assertEqual(m1._cells[0][0]._x1, expected_positions[0][0])
    self.assertEqual(m1._cells[0][0]._y1, expected_positions[0][1])
    self.assertEqual(m1._cells[0][0]._x2, expected_positions[0][2])
    self.assertEqual(m1._cells[0][0]._y2, expected_positions[0][3])
    
    self.assertEqual(m1._cells[0][1]._x1, expected_positions[1][0])
    self.assertEqual(m1._cells[0][1]._y1, expected_positions[1][1])
    self.assertEqual(m1._cells[0][1]._x2, expected_positions[1][2])
    self.assertEqual(m1._cells[0][1]._y2, expected_positions[1][3])
    
    self.assertEqual(m1._cells[1][0]._x1, expected_positions[2][0])
    self.assertEqual(m1._cells[1][0]._y1, expected_positions[2][1])
    self.assertEqual(m1._cells[1][0]._x2, expected_positions[2][2])
    self.assertEqual(m1._cells[1][0]._y2, expected_positions[2][3])
    
    self.assertEqual(m1._cells[1][1]._x1, expected_positions[3][0])
    self.assertEqual(m1._cells[1][1]._y1, expected_positions[3][1])
    self.assertEqual(m1._cells[1][1]._x2, expected_positions[3][2])
    self.assertEqual(m1._cells[1][1]._y2, expected_positions[3][3])

  def test_entrance_and_exit(self):
    num_cols = 5
    num_rows = 5
    
    # Create a maze with a fixed seed
    m1 = Maze(0, 0, num_rows, num_cols, 10, 10, seed=42)
    
    # Check that entrance (top-left cell) has its top wall removed
    self.assertFalse(m1._cells[0][0].has_top_wall)
    
    # Check that exit (bottom-right cell) has its bottom wall removed
    self.assertFalse(m1._cells[num_rows-1][num_cols-1].has_bottom_wall)

  def test_break_walls_all_cells_visited(self):
    num_cols = 5
    num_rows = 5
    
    # Create a maze with a fixed seed for predictable results
    m1 = Maze(0, 0, num_rows, num_cols, 10, 10, seed=42)
    
    # Check that all cells have been visited
    all_visited = True
    for i in range(num_rows):
        for j in range(num_cols):
            if not m1._cells[i][j].visited:
                all_visited = False
                break
    
    self.assertTrue(all_visited, "Not all cells were visited during maze generation")
    
  def test_break_walls_path_exists(self):
    # Create a small maze with a fixed seed
    m1 = Maze(0, 0, 3, 3, 10, 10, seed=42)
    
    # Check that there's a path from entrance to exit
    # For a valid path to exist, there must be broken walls connecting cells
    
    # Count the number of broken interior walls in the maze
    # Each wall between cells is counted only once
    broken_walls_count = 0
    for i in range(m1._num_rows):
        for j in range(m1._num_cols):
            # Only count right and bottom walls to avoid double counting
            if j < m1._num_cols - 1 and not m1._cells[i][j].has_right_wall:
                broken_walls_count += 1
            if i < m1._num_rows - 1 and not m1._cells[i][j].has_bottom_wall:
                broken_walls_count += 1
    
    # For a fully connected maze with n cells, we need exactly (n-1) broken interior walls
    # This doesn't count the entrance and exit openings
    expected_broken_walls = m1._num_rows * m1._num_cols - 1
    
    self.assertEqual(broken_walls_count, expected_broken_walls,
                    f"Expected {expected_broken_walls} broken walls but found {broken_walls_count}")

if __name__ == "__main__":
  unittest.main()