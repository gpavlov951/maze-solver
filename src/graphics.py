from tkinter import Tk, BOTH, Canvas, Frame, Label, Button, StringVar

class Window:
  def __init__(self, width, height) -> None:
    self.__root = Tk()
    self.__root.title("Maze Game")
    self.__root.geometry(f"{width}x{height}")
    self.__root.protocol("WM_DELETE_WINDOW", self.close)
    
    self.__width = width
    self.__height = height

    self.__canvas = Canvas(self.__root,
                            bg="white", 
                            width=width, 
                            height=height)
    self.__canvas.pack(fill=BOTH, expand=1)
    self.__is_running = False
    
    self.__popup_frame = None
    self.__restart_callback = None
  
  def redraw(self):
    self.__root.update_idletasks()
    self.__root.update()

  def wait_for_close(self):
    self.__is_running = True
    while self.__is_running:
      self.redraw()
  
  def draw_line(self, line, fill_color="black"):
    line.draw(self.__canvas, fill_color)

  def close(self):
    self.__is_running = False
    
  def clear_canvas(self):
    """Clear all items from the canvas"""
    self.__canvas.delete("all")
    
  def show_popup(self, message, restart_callback=None):
    """
    Display a popup with a message and a restart button without an overlay.
    
    Args:
        message: The message to display in the popup
        restart_callback: Function to call when the restart button is clicked
    """
    self.__restart_callback = restart_callback
    
    # Create popup frame with a slight shadow effect and more visible border
    self.__popup_frame = Frame(
        self.__root,
        bg="white",
        highlightbackground="#444444",
        highlightthickness=3,  # Thicker border for better visibility
        padx=20,
        pady=20
    )
    
    # Position popup in the center
    popup_width = 300
    popup_height = 150
    x_pos = (self.__width - popup_width) // 2
    y_pos = (self.__height - popup_height) // 2
    
    # Create message label with a contrasting text color
    message_label = Label(
        self.__popup_frame,
        text=message,
        font=("Arial", 14, "bold"),
        bg="white",
        fg="black",  # Explicitly set text color to black
        wraplength=260
    )
    message_label.pack(pady=(0, 20))
    
    # Create restart button with a distinctive style
    # Using a combination of parameters to ensure green color on all platforms
    restart_button = Button(
        self.__popup_frame,
        text="Restart",
        font=("Arial", 12, "bold"),
        background="green",      # Standard background parameter
        foreground="white",        # Text color
        activebackground="#45a049", # Color when clicked
        activeforeground="white",   # Text color when clicked
        command=self.__handle_restart,
        padx=15,
        pady=8,
        relief="raised",
        bd=2,
        highlightbackground="green", # For macOS
        highlightcolor="green",      # Additional color property
        bg="green",                  # Alternate bg parameter
        fg="white"                     # Alternate fg parameter
    )
    restart_button.pack()
    
    # Display the popup using canvas.create_window
    self.__canvas.create_window(
        x_pos + popup_width // 2,
        y_pos + popup_height // 2,
        window=self.__popup_frame,
        width=popup_width,
        height=popup_height,
        tags="popup"
    )
  
  def __handle_restart(self):
    """Handle the restart button click"""
    # Remove popup
    if self.__popup_frame:
        self.__popup_frame.destroy()
        self.__popup_frame = None
    
    # Call the restart callback if provided
    if self.__restart_callback:
        self.__restart_callback()


class Point:
  def __init__(self, x: int, y: int) -> None:
    self.x = x
    self.y = y


class Line:
  def __init__(self, p1: Point, p2: Point) -> None:
    self.p1 = p1
    self.p2 = p2

  def draw(self, canvas: Canvas, fill_color="black"):
    canvas.create_line(self.p1.x, 
                       self.p1.y, 
                       self.p2.x, 
                       self.p2.y, 
                       fill=fill_color,
                       width=2)
                       