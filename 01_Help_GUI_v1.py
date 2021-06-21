"""
Component 1 - Help GUI
Diane Kim
21/06/21
Basic formatting of GUI
"""

# Import
from tkinter import *
import random


# Create converter class
class Converter:
    def __init__(self):
        print("Hello World")

        # Format variables
        background_color = "light pink"

        # Converter Main screen GUI
        self.converter_frame = Frame(width=300, height=300, bg=background_color)
        self.converter_frame.grid()


# Main Routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter()
    root.mainloop()
