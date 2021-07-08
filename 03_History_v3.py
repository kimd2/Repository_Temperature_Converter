"""
Component 3 - History
Diane Kim
05/07/21
Version 3 - Add export button and GUI
"""

# Copy main frame
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
        self.temperature_label = Label(self.converter_frame, text="", font=("Garamond", "14"), width=10, pady=5,
                                       bg="mistyrose")
        self.temperature_label.grid(row=4, column=2, padx=10)

        # Convert button (Row 5)
        self.convert_button = Button(self.converter_frame, text="Convert", font=("Garamond", "14", "bold"),
                                     command=self.convert)
        self.convert_button.grid(row=5, column=1, padx=10, pady=5)

        # Help Button (Row 6)
        self.help_button = Button(self.converter_frame, text="Help", font=("Garamond", "14"),
                                  command=self.help)
        self.help_button.grid(row=6, column=1, padx=10, pady=5)

        # History Button (Row 7)
        self.history_button = Button(self.converter_frame, text="History", font=("Garamond", "14"),
                                     command=self.history)
        self.history_button.grid(row=7, column=1, padx=10, pady=5)

    # Create command for help button
    def help(self):
        print("You asked for help")
        get_help = Help(self)
        get_help.help_text.configure(text="Help text goes here")

    # Create command for history button
    def history(self):
        global history_record
        print("History viewed")
        get_history = History(self)
        count = 0
        for item in conversions:
            if count != 10:
                if history_record:
                    history_record = history_record + "\n{}".format(item)
                else:
                    history_record = item
                count += 1
        if not conversions:
            history_record = "No conversions made"
        get_history.history_text.configure(text=history_record)

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
        global temperature_entry, check, from_variable
        temperature_entry_number = temperature_entry.get()
        print(temperature_entry_number)
        result = number_checker(temperature_entry_number)
        valid = False
        while not valid:
            if result or result == 0:
                if not check:
                    self.error_message.grid_remove()
                valid = True
                check = True
            else:
                if check:
                    self.error_message.grid(row=2, columnspan=3)
                    check = False
                self.conversion_label = Label(self.converter_frame, text="Invalid", font=("Garamond", "14"),
                                              bg="misty rose", pady=5, width=10)
                self.conversion_label.grid(row=4, column=2)
                break
        if valid:
            if from_variable == "Celsius":
                converted = result * (9 / 5) + 32
                converted = converted.__round__(2)
                conversions.insert(0, "{}°C ⇛ {}°F".format(result, converted))
            else:
                converted = (result - 32) * (5 / 9)
                converted = converted.__round__(2)
                conversions.append("{}°F ⇛ {}°C".format(result, converted))
            self.conversion_label = Label(self.converter_frame, text=converted, font=("Garamond", "14"),
                                          bg="misty rose", width=10, pady=5)
            self.conversion_label.grid(row=4, column=2)
            print(converted)


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
        self.help_frame = Frame(self.help_box, width=300, height=200, bg=background, pady=15)
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
                                     pady=5, command=partial(self.close_help, partner))
        self.dismiss_button.grid(row=2, pady=5)

    def close_help(self, partner):
        self.help_box.destroy()
        # Put Help button back to normal
        partner.help_button.config(state=NORMAL)


class History:
    def __init__(self, partner):
        # Format bg color
        background = "mistyrose"

        # Disable history button
        partner.history_button.config(state=DISABLED)

        # Sets up child window (IE, history box)
        self.history_box = Toplevel()

        # Enables history button if users press cross at top

        # Set up GUI frame
        self.history_frame = Frame(self.history_box, width=300, height=200, bg=background, pady=10)
        self.history_frame.grid()
        self.history_box.protocol("WM_DELETE_WINDOW", partial(self.close_history, partner))

        # Set up history Heading (row 0)
        self.history_heading = Label(self.history_frame, text="History", font=("Garamond", "16", "bold"), bg=background,
                                     padx=10,
                                     pady=10)
        self.history_heading.grid(row=0)

        # Set up history text (label, row 1)
        self.history_text = Label(self.history_frame, text="History2 text goes here", font=("Garamond", "14"),
                                  bg=background, padx=10, pady=10)
        self.history_text.grid(row=1)

        # Set up Dismiss button (button, row 3)
        self.dismiss_button = Button(self.history_frame,
                                     text="Dismiss",
                                     font=("Garamond", "14"),
                                     bg="salmon", padx=10,command=partial(self.close_history, partner))
        self.dismiss_button.grid(row=3, pady=5)

        # Set up export button (Row 2)
        self.export_button = Button(self.history_frame, text="Export", font=("Garamond", "14"), bg="salmon", padx=10, command=self.export)
        self.export_button.grid(row=2, pady=5)

    def export(self):
        print("Export window opened")
        get_export = Export(self)
        get_export.export_text.configure(text="The file will be exported into the same folder as the program.\nEnter file name:")

    def close_history(self, partner):
        self.history_box.destroy()
        # Put Help button back to normal
        partner.history_button.config(state=NORMAL)


class Export:
    def __init__(self, partner):
        # Format BG color
        background = "mistyrose"

        # Disable Export button
        partner.export_button.config(state=DISABLED)

        # Sets up child window (IE, Export box)
        self.export_box = Toplevel()

        # Enables Export button if users press cross at top
        self.export_box.protocol("WM_DELETE_WINDOW", partial(self.close_export, partner))

        # Set up GUI frame
        self.export_frame = Frame(self.export_box, width=300, height=200, bg=background, pady=10)
        self.export_frame.grid()

        # Set up Export Heading (row 0)
        self.export_heading = Label(self.export_frame,
                                    text="Export",
                                    font=("Garamond", "16", "bold"),
                                    bg=background,
                                    padx=10,
                                    pady=10)
        self.export_heading.grid(row=0,
                                 columnspan=2)

        # Set up Export text (label, row 1)
        self.export_text = Label(self.export_frame,
                                 text="Export text goes here",
                                 font=("Garamond", "14"),
                                 bg=background,
                                 padx=10,
                                 pady=10)
        self.export_text.grid(row=1,
                              columnspan=2)

        # Set up entry
        file_name_entry = Entry(self.export_frame, bd=2, width=40)
        file_name_entry.grid(row=2, columnspan=2, padx=10, pady=5)

        # Set up export option
        export_option_check = Checkbutton(self.export_frame, text="Export last 10 conversions only", bg=background)
        export_option_check.grid(row=3, columnspan=2)

        # Set up Dismiss and export button (button, row 4)
        self.dismiss_button = Button(self.export_frame, text="Dismiss", font=("Garamond", "14"), bg="salmon", padx=10,
                                     command=partial(self.close_export, partner))
        self.dismiss_button.grid(row=4, column=1, pady=5, sticky=W, padx=5)

        self.final_export_button = Button(self.export_frame, text="Export", font=("Garamond", "14"), bg="salmon", padx=10)
        self.final_export_button.grid(row=4, column=0, pady=5, sticky=E, padx=5)


    def close_export(self, partner):
        self.export_box.destroy()
        # Put Help button back to normal
        partner.export_button.config(state=NORMAL)



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
    # except TypeError:
    # print("Not float Type")
    # return None
    except ValueError:
        print("Not float Value")
        return None


# Main Routine
conversions = []
history_record = ""
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter()
    root.mainloop()
