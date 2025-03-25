from graphics import Window
from maze import Maze

def main():
    # Create a function to hold all maze creation and solving logic
    # so it can be restarted
    def create_and_solve_maze():
        nonlocal win
        
        num_rows = 12
        num_cols = 12
        margin = 50
        
        screen_x = 800
        screen_y = 600
        
        cell_size_x = (screen_x - 2 * margin) / num_cols
        cell_size_y = (screen_y - 2 * margin) / num_rows
        
        # Use seed=None for random maze every time
        # Use a specific value (e.g., seed=42) for consistent maze generation during debugging
        maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win, seed=None)
        
        # Solve the maze
        is_solved = maze.solve()
        
        # Instead of printing to console, show the result in a popup
        if is_solved:
            win.show_popup("🎉 Success! 🎉\nMaze solved successfully!\nClick Restart to generate a new maze.", restart_game)
        else:
            win.show_popup("❌ Oops! ❌\nCould not solve the maze.\nClick Restart to try a different maze.", restart_game)
    
    # Function to restart the game when the button is clicked
    def restart_game():
        # Clear the canvas before restarting
        win.clear_canvas()
        
        # Create and solve a new maze
        create_and_solve_maze()
    
    # Create the main window
    screen_x = 800
    screen_y = 600
    win = Window(screen_x, screen_y)
    
    # Create and solve the initial maze
    create_and_solve_maze()
    
    # Wait for the window to close
    win.wait_for_close()

if __name__ == "__main__":
    main()