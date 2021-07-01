"""
Component 2 - Converter
Diane Kim
29/06/21
V3 - Added function to check input type
"""

# Import
from tkinter import *
from functools import partial  # to prevent opening unwanted windows


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
                                          font=("Garamond", "16", "bold"), bg=background_color)
        self.temp_converter_label.grid(row=0, columnspan=3, padx=10, pady=10)

        # Converter description (Row 1)
        self.converter_description_label = Label(self.converter_frame,
                                                 text="Convert from Fahrenheit to Centigrade or Centigrade to Fahrenheit",
                                                 font=("Garamond", "16", "bold"), bg=background_color)
        self.converter_description_label.grid(row=1, columnspan=3, padx=10, pady=10)

        # Variable identification (Row 3)
        self.error_message = Label(self.converter_frame, text="Please enter a number above -273.15ºC or -459.67ºF!",
                               font=("Garamond", "14"), bg="light pink", pady=5)
        global from_variable
        from_variable = "Celsius"
        self.from_variable_label = Label(self.converter_frame, text="Celsius", font=("Garamond", "14"),
                                         bg=background_color, pady=5)
        self.from_variable_label.grid(row=3, column=0)
        self.to_variable_label = Label(self.converter_frame, text="Fahrenheit", font=("Garamond", "14"),
                                       bg=background_color, pady=5)
        self.to_variable_label.grid(row=3, column=2)

        # Converter input box and change direction button (Row 4)
        global temperature_entry, check
        temperature_entry = Entry(self.converter_frame, bd=2)
        temperature_entry.grid(row=4, column=0, padx=10, pady=5)
        check = True
        self.change_temp_button = Button(self.converter_frame, text="Change Conversion Direction",
                                         font=("Garamond", "14"), command=self.change_direction)
        self.change_temp_button.grid(row=4, column=1, padx=10, pady=5)
        self.temperature_label = Label(self.converter_frame, text="Test", font=("Garamond", "14"), pady=5,
                                       bg="mistyrose")
        self.temperature_label.grid(row=4, column=2, padx=10)

        # Convert button (Row 5)
        self.convert_button = Button(self.converter_frame, text="Convert", font=("Garamond", "14", "bold"), command=self.convert)
        self.convert_button.grid(row=5, column=1, padx=10, pady=5)

        # Help Button (Row 6)
        self.help_button = Button(self.converter_frame, text="Help", font=("Garamond", "14"),
                                  command=self.help)
        self.help_button.grid(row=6, column=1, padx=10, pady=5)

    # Create command for help button
    def help(self):
        print("You asked for help")
        get_help = Help(self)
        get_help.help_text.configure(text="Help text goes here")

    # Create command for change direction button
    def change_direction(self):
        global from_variable
        if from_variable == "Celsius":
            from_variable = "Fahrenheit"
            to_variable = "Celsius"
        else:
            from_variable = "Celsius"
            to_variable = "Fahrenheit"
        print("Conversion direction changed")
        background_color = "light pink"
        self.from_variable_label = Label(self.converter_frame, text=from_variable, font=("Garamond", "14"),
                                         bg=background_color, pady=5, padx=20)
        self.from_variable_label.grid(row=3, column=0)
        self.to_variable_label = Label(self.converter_frame, text=to_variable, font=("Garamond", "14"),
                                       bg=background_color, pady=5, padx=20)
        self.to_variable_label.grid(row=3, column=2)

    # Create command for convert button
    def convert(self):
        # Number check
        global temperature_entry, check
        temperature_entry_number = temperature_entry.get()
        print(temperature_entry_number)
        result = number_checker(temperature_entry_number)
        valid = False
        while not valid:
            if result:
                if not check:
                    self.error_message.grid_remove()
                valid = True
                check = True
            else:
                if check:
                    self.error_message.grid(row=2, columnspan=3)
                    check = False
                self.conversion_label = Label(self.converter_frame, text="Invalid", font=("Garamond", "14"), bg="misty rose", pady=5)
                self.conversion_label.grid(row=4, column=2)
                break


# Create Help Class for GUI
class Help:
    def __init__(self, partner):
        # Format BG color
        background = "mistyrose"

        # Disable help button
        partner.help_button.config(state=DISABLED)

        # Sets up child window (IE, help box)
        self.help_box = Toplevel()

        # Enables help button if users press cross at top
        self.help_box.protocol("WM_DELETE_WINDOW", partial(self.close_help, partner))

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
                                     pady=10, command=partial(self.close_help, partner))
        self.dismiss_button.grid(row=2, pady=10)

    def close_help(self, partner):
        self.help_box.destroy()
        # Put Help button back to normal
        partner.help_button.config(state=NORMAL)


# Check number
def number_checker(number):
    global from_variable
    try:
        number = float(number)
        if from_variable == "Celsius":
            if number < -273.15:
                print("Invalid Celcius")
                return None
            else:
                print("Valid Celcius")
                return number
        else:
            if number < -459.67:
                print("Invalid Fahrenheit")
                return None
            else:
                print("Valid Fahrenheit")
                return number
    except ValueError:
        print("Not float Value")
        return None


# Main Routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter()
    root.mainloop()
