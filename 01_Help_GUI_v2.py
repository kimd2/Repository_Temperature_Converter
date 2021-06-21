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
        # Format variables
        background_color = "light pink"

        # Converter Main screen GUI
        self.converter_frame = Frame(width=300, height=300, bg=background_color, pady=10)
        self.converter_frame.grid()

        # Title
        self.temp_converter_label = Label(self.converter_frame, text="Temperature Converter",
                                          font=("Garamond", "16", "bold"), bg=background_color, padx=10, pady=10)
        self.temp_converter_label.grid(row=0)

        # Help Button (Row 1)
        self.help_button = Button(self.converter_frame, text="Help", font=("Garamond", "14"), padx=10, pady=10,
                                  command=self.help)
        self.help_button.grid(row=1)

    # Create command for button
    def help(self):
        print("You asked for help")
        get_help = Help()
        get_help.help_text.configure(text="Help text goes here")


# Create Help Class for GUI
class Help:
    def __init__(self):
        # Format BG color
        background = "mistyrose"

        # Sets up child window (IE, help box)
        self.help_box = Toplevel()

        # Set up GUI frame
        self.help_frame = Frame(self.help_box, width=300, height=200, bg=background, pady=10)
        self.help_frame.grid()

        # Set up Help Heading (row 0)
        self.help_heading = Label(self.help_frame, text="Help", font=("Garamond", "16", "bold"), bg=background, padx=10,
                                  pady=10)
        self.help_heading.grid(row=0)

        # Set up Help text (label, row 1)
        self.help_text = Label(self.help_frame, text="Help text goes here", font=("Garamond", "14"), bg=background,
                               padx=10, pady=10)
        self.help_text.grid(row=1)

        # Set up Dismiss button (button, row 2)
        self.dismiss_button = Button(self.help_frame, text="Dismiss", font=("Garamond", "14"), bg="salmon", padx=10,
                                     pady=10, command=self.close_help)
        self.dismiss_button.grid(row=2, pady=10)

    def close_help(self):
        self.help_box.destroy()


# Main Routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter()
    root.mainloop()
