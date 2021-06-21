"""
Component 1 - Help GUI
Diane Kim
21/06/21
Empty Frame
"""

# Import
from tkinter import *
import random


# Create converter class
class Converter:
    def __init__(self, parent):
        print("Hello World")


# Main Routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter(root)
    root.mainloop()
