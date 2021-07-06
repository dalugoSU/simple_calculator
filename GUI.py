import tkinter as ttk
import GUI_CONSTANTS as gc  # Imports constants from GUI_CONSTANTS file, these are not meant to be changed


class CalculatorApp:

    def __init__(self, root):  # Initializes each function/method that affects the GUI
        self.root = root
        self.main_screen()
        self.main_frame()
        self.output_screen()
        self.number_buttons()
        self.operation_buttons()

    def main_screen(self):  # Main Screen function. It gives the root window basic dimensions and title
        self.root.title(gc.WINDOW_TITLE)
        self.root.minsize(gc.MINX, gc.MINY)
        self.root.maxsize(gc.MAXX, gc.MAXY)

    def main_frame(self):  # Main Screen where everything will sit. It is on top of the root window
        global main_frame

        main_frame = ttk.Frame(self.root, bg="light grey")
        main_frame.pack(fill='both', expand=True)

    def output_screen(self):  # Text Box that will show output
        global output

        output = ttk.Text(main_frame, bg="white", font=(None, 15))
        output.place(relx=0.05, rely=0.05, relwidth=0.67, relheight=0.2)

    def number_buttons(self):  # All number Buttons. Initialization and Placement. Each has command calling its designated function
        global button0, dotButton, button1, button2, button3, button4, button5, button6, button7, button8, button9

        button0 = ttk.Button(main_frame, text=0, bg="light gray", font=(None, 10), command=lambda: self.get_zero())
        button0.place(relx=0.75, rely=0.75, relwidth=0.2, relheight=0.09)

        dotButton = ttk.Button(main_frame, text=".", bg="light gray", font=(None, 10), command=lambda: self.get_dot())
        dotButton.place(relx=0.75, rely=0.86, relwidth=0.2, relheight=0.09)

        button1 = ttk.Button(main_frame, text=1, font=(None, 15), command=lambda: self.get_one())
        button1.place(relx=0.05, rely=0.75, relwidth=0.2, relheight=0.2)

        button2 = ttk.Button(main_frame, text=2, font=(None, 15), command=lambda: self.get_two())
        button2.place(relx=0.28, rely=0.75, relwidth=0.2, relheight=0.2)

        button3 = ttk.Button(main_frame, text=3, font=(None, 15), command=lambda: self.get_three())
        button3.place(relx=0.51, rely=0.75, relwidth=0.2, relheight=0.2)

        button4 = ttk.Button(main_frame, text=4, font=(None, 15), command=lambda: self.get_four())
        button4.place(relx=0.05, rely=0.52, relwidth=0.2, relheight=0.2)

        button5 = ttk.Button(main_frame, text=5, font=(None, 15), command=lambda: self.get_five())
        button5.place(relx=0.28, rely=0.52, relwidth=0.2, relheight=0.2)

        button6 = ttk.Button(main_frame, text=6, font=(None, 15), command=lambda: self.get_six())
        button6.place(relx=0.51, rely=0.52, relwidth=0.2, relheight=0.2)

        button7 = ttk.Button(main_frame, text=7, font=(None, 15), command=lambda: self.get_seven())
        button7.place(relx=0.05, rely=0.3, relwidth=0.2, relheight=0.2)

        button8 = ttk.Button(main_frame, text=8, font=(None, 15), command=lambda: self.get_eight())
        button8.place(relx=0.28, rely=0.3, relwidth=0.2, relheight=0.2)

        button9 = ttk.Button(main_frame, text=9, font=(None, 15), command=lambda: self.get_nine())
        button9.place(relx=0.51, rely=0.3, relwidth=0.2, relheight=0.2)

    def operation_buttons(self):  # Operational buttons. Initialization and placement. Each has command calling its designated function
        global multiply, divide, add, subtract, equal, clear

        multiply = ttk.Button(main_frame, text="X", bg="light gray", font=(None, 10), command=lambda: self.get_multiply())
        multiply.place(relx=0.75, rely=0.63, relwidth=0.2, relheight=0.09)

        divide = ttk.Button(main_frame, text="/", bg="light gray", font=(None, 10), command=lambda: self.get_divide())
        divide.place(relx=0.75, rely=0.53, relwidth=0.2, relheight=0.09)

        add = ttk.Button(main_frame, text="+", bg="light gray", font=(None, 15), command=lambda: self.get_add())
        add.place(relx=0.75, rely=0.4, relwidth=0.2, relheight=0.09)

        subtract = ttk.Button(main_frame, text="-", bg="light gray", font=(None, 15),command=lambda: self.get_subtract())
        subtract.place(relx=0.75, rely=0.3, relwidth=0.2, relheight=0.09)

        equal = ttk.Button(main_frame, text="=", bg="light green", font=(None, 15), command=lambda: [self.get_input(), self.clear_screen(), self.calculate(operation)])
        equal.place(relx=0.75, rely=0.15, relwidth=0.2, relheight=0.09)

        clear = ttk.Button(main_frame, text="CLEAR", bg="light green", font=(None, 10), command=lambda: self.clear_screen())
        clear.place(relx=0.75, rely=0.05, relwidth=0.2, relheight=0.09)

    # Logic for all buttons & Performs Operation

    def get_multiply(self):

        output.insert(ttk.END, gc.MULTIPLY)

    def get_divide(self):

        output.insert(ttk.END, gc.DIVIDE)

    def get_add(self):

        output.insert(ttk.END, gc.ADD)

    def get_subtract(self):

        output.insert(ttk.END, gc.SUBTRACT)

    def get_zero(self):

        output.insert(ttk.END, gc.ZERO)

    def get_dot(self):

        output.insert(ttk.END, gc.DOT)

    def get_one(self):

        output.insert(ttk.END, gc.ONE)

    def get_two(self):

        output.insert(ttk.END, gc.TWO)

    def get_three(self):

        output.insert(ttk.END, gc.THREE)

    def get_four(self):

        output.insert(ttk.END, gc.FOUR)

    def get_five(self):

        output.insert(ttk.END, gc.FIVE)

    def get_six(self):

        output.insert(ttk.END, gc.SIX)

    def get_seven(self):

        output.insert(ttk.END, gc.SEVEN)

    def get_eight(self):

        output.insert(ttk.END, gc.EIGHT)

    def get_nine(self):

        output.insert(ttk.END, gc.NINE)

    def get_input(self):  # This function gets the operation outputed in the text box and sets global variable operation equals to that
        global operation

        operation = output.get("1.0", ttk.END)

    def calculate(self, operation):  # Takes operation from text box. Splits numbers and Operands and performs operation based on those.

        result = int()
        print(operation)

        try:
            do = f'result = {operation}'
            exec(do)
        except IndexError:  # If user left open ended operation
            output.insert(ttk.END, "ERROR")
            pass
        except ZeroDivisionError:  # If user attempts to divide by zero
            output.insert(ttk.END, "ERROR - ZERO DIVISION")

        output.insert(ttk.END, result)

    def clear_screen(self):  # Clears output text box

        output.delete("1.0", ttk.END)


        
        
def start_calculator():  # This function is called by main to run calculator
    root = ttk.Tk()
    CalculatorApp(root)
    root.mainloop()
