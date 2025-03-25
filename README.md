# Maze Solver

A Python-based maze generator and solver with visual representation.

## Overview

This project creates a random maze and solves it using a depth-first search algorithm. The entire process is visualized in real-time, showing both the maze generation and the solving path.

## Features

- Automatic random maze generation
- Visual representation of the maze with Tkinter
- Depth-first search algorithm for maze creation
- Depth-first search algorithm for maze solving
- Visual path finding with successful and unsuccessful attempt tracking
- Configurable maze dimensions and cell sizes
- Optional seed parameter for reproducible mazes

## Requirements

- Python 3.x
- Tkinter (usually comes with Python)

## Running the Application

You can run the maze solver using the provided shell script:

```bash
./main.sh
```

This will generate a random maze and then solve it, displaying the result in a GUI window.

## Running the Tests

Unit tests are provided to verify the functionality of the maze generation and solving. Run them using:

```bash
./test.sh
```

This uses Python's unittest discovery to run all tests in the src directory.

## Project Structure

- `src/main.py`: Entry point for the application
- `src/maze.py`: Contains the Maze class that handles maze generation and solving
- `src/cell.py`: Contains the Cell class representing individual maze cells
- `src/graphics.py`: Contains graphics utilities for visualization
- `src/tests.py`: Unit tests for the maze functionality
- `main.sh`: Shell script to run the main program
- `test.sh`: Shell script to run all tests

## How It Works

### Maze Generation

The maze is generated using a depth-first search with backtracking (recursive backtracker) algorithm:

1. Start with a grid of cells, all with walls between them
2. Begin at the entrance (top-left cell)
3. Randomly choose an unvisited adjacent cell
4. Break down the wall between the current cell and the chosen cell
5. Recursively repeat from the new cell until all cells are visited

### Maze Solving

The maze is solved using another depth-first search algorithm:

1. Start at the entrance (top-left cell)
2. Try each possible direction (up, right, down, left)
3. If a path leads to the exit, return success
4. If a path leads to a dead end, backtrack and try another direction
5. Visually show the path with red lines, and gray lines for dead ends

## Customization

You can customize the maze by modifying parameters in `main.py`:

- `num_rows` and `num_cols`: Change the size of the maze
- `margin`: Adjust the margin around the maze
- `seed`: Set a specific seed for reproducible maze generation

## License

This project is licensed under the MIT License - see the LICENSE file for details.
