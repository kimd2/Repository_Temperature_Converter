"""
Component 1 - Help GUI
Diane Kim
21/06/21
V2 - Create help button
"""

# Import
from tkinter import *


# Create converter class
class Converter:
    def __init__(self):
        print("Hello World")

        # Format variables
        background_color = "light pink"

        # Converter Main screen GUI
        self.converter_frame = Frame(width=300, height=300, bg=background_color, pady=10)
        self.converter_frame.grid()

        # Title
        self.temp_converter_label = Label(self.converter_frame, text="Temperature Converter", font=("Garamond", "16", "bold"), bg=background_color, padx=10, pady=10)
        self.temp_converter_label.grid(row=0)

        # Help Button (Row 1)
        self.help_button = Button(self.converter_frame, text="Help", font=("Garamond", "14"), padx=10, pady=10)
        self.help_button.grid(row=1)

    # Create command for button
    def help(self):
        print("You asked for help")
        get_help = Help()
        get_help.help_text.configure(text="Help text goes here")


# Main Routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter()
    root.mainloop()
