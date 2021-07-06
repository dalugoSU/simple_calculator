# import tkinter as tk
from tkinter import *
import GUI_CONSTANTS as gc  # Imports constants from GUI_CONSTANTS file, these are not meant to be changed
import sympy


class CalculatorApp:

    def __init__(self, root):  # Initializes each function/method that affects the GUI
        self._root = root
        self._main_screen()
        self._main_frame()
        self._root_main_frame = None
        self._output = None
        self._button0 = None
        self._dotButton = None
        self._button1 = None
        self._button2 = None
        self._button3 = None
        self._button4 = None
        self._button5 = None
        self._button6 = None
        self._button7 = None
        self._button8 = None
        self._button9 = None
        self._multiply = None
        self._divide = None
        self._add = None
        self._subtract = None
        self._equal = None
        self._clear = None
        self._operation = None
        self._number_buttons()
        self._operation_buttons()
        self._output = Text(self._main_frame, bg="white", font=(None, 15))
        self._output.place(relx=0.05, rely=0.05, relwidth=0.67, relheight=0.2)
        self._OPTIONS = {
            'add': self._output.insert(END, gc.ADD),
            'subtract': self._output.insert(END, gc.SUBTRACT),
            'divide': self._output.insert(END, gc.DIVIDE),
            'multiply': self._output.insert(END, gc.MULTIPLY),
            'zero': self._output.insert(END, gc.ZERO),
            'one': self._output.insert(END, gc.ONE),
            'two': self._output.insert(END, gc.TWO),
            'three': self._output.insert(END, gc.THREE),
            'four': self._output.insert(END, gc.FOUR),
            'five': self._output.insert(END, gc.FIVE),
            'six': self._output.insert(END, gc.SIX),
            'seven': self._output.insert(END, gc.SEVEN),
            'eight': self._output.insert(END, gc.EIGHT),
            'nine': self._output.insert(END, gc.NINE),
            'dot': self._output.insert(END, gc.DOT)
        }

    def _main_screen(self):  # Main Screen function. It gives the root window basic dimensions and title
        self._root.title(gc.WINDOW_TITLE)
        self._root.minsize(gc.MINX, gc.MINY)
        self._root.maxsize(gc.MAXX, gc.MAXY)

    def _main_frame(self):  # Main Screen where everything will sit. It is on top of the root window
        self._root_main_frame = Frame(self._root, bg="light grey")
        self._root_main_frame.pack(fill='both', expand=True)

    def _number_buttons(self):  # All number Buttons. Initialization and Placement. Each has command calling its designated function
        self._button0 = Button(self._main_frame, text=0, bg="light gray", font=(None, 10), command=lambda: self._output_keypad_press(gc.ZERO))
        self._button0.place(relx=0.75, rely=0.75, relwidth=0.2, relheight=0.09)

        self._dotButton = Button(self._main_frame, text=".", bg="light gray", font=(None, 10), command=lambda: self._output_keypad_press(gc.DOT))
        self._dotButton.place(relx=0.75, rely=0.86, relwidth=0.2, relheight=0.09)

        self._button1 = Button(self._main_frame, text=1, font=(None, 15), command=lambda: self._output_keypad_press(gc.ONE))
        self._button1.place(relx=0.05, rely=0.75, relwidth=0.2, relheight=0.2)

        self._button2 = Button(self._main_frame, text=2, font=(None, 15), command=lambda: self._output_keypad_press(gc.TWO))
        self._button2.place(relx=0.28, rely=0.75, relwidth=0.2, relheight=0.2)

        self._button3 = Button(self._main_frame, text=3, font=(None, 15), command=lambda: self._output_keypad_press(gc.THREE))
        self._button3.place(relx=0.51, rely=0.75, relwidth=0.2, relheight=0.2)

        self._button4 = Button(self._main_frame, text=4, font=(None, 15), command=lambda: self._output_keypad_press(gc.FOUR))
        self._button4.place(relx=0.05, rely=0.52, relwidth=0.2, relheight=0.2)

        self._button5 = Button(self._main_frame, text=5, font=(None, 15), command=lambda: self._output_keypad_press(gc.FIVE))
        self._button5.place(relx=0.28, rely=0.52, relwidth=0.2, relheight=0.2)

        self._button6 = Button(self._main_frame, text=6, font=(None, 15), command=lambda: self._output_keypad_press(gc.SIX))
        self._button6.place(relx=0.51, rely=0.52, relwidth=0.2, relheight=0.2)

        self._button7 = Button(self._main_frame, text=7, font=(None, 15), command=lambda: self._output_keypad_press(gc.SEVEN))
        self._button7.place(relx=0.05, rely=0.3, relwidth=0.2, relheight=0.2)

        self._button8 = Button(self._main_frame, text=8, font=(None, 15), command=lambda: self._output_keypad_press(gc.EIGHT))
        self._button8.place(relx=0.28, rely=0.3, relwidth=0.2, relheight=0.2)

        self._button9 = Button(self._main_frame, text=9, font=(None, 15), command=lambda: self._output_keypad_press(gc.NINE))
        self._button9.place(relx=0.51, rely=0.3, relwidth=0.2, relheight=0.2)

    def _operation_buttons(self):  # Operational buttons. Initialization and placement. Each has command calling its designated function
        self._multiply = Button(self._main_frame, text="X", bg="light gray", font=(None, 10), command=lambda: self._output_keypad_press(gc.MULTIPLY))
        self._multiply.place(relx=0.75, rely=0.63, relwidth=0.2, relheight=0.09)

        self._divide = Button(self._main_frame, text="/", bg="light gray", font=(None, 10), command=lambda: self._output_keypad_press(gc.DIVIDE))
        self._divide.place(relx=0.75, rely=0.53, relwidth=0.2, relheight=0.09)

        self._add = Button(self._main_frame, text="+", bg="light gray", font=(None, 15), command=lambda: self._output_keypad_press(gc.ADD))
        self._add.place(relx=0.75, rely=0.4, relwidth=0.2, relheight=0.09)

        self._subtract = Button(self._main_frame, text="-", bg="light gray", font=(None, 15), command=lambda: self._output_keypad_press(gc.SUBTRACT))
        self._subtract.place(relx=0.75, rely=0.3, relwidth=0.2, relheight=0.09)

        self._equal = Button(self._main_frame, text="=", bg="light green", font=(None, 15), command=lambda: [self._get_input(), self._clear_screen(), self._calculate(self._operation)])
        self._equal.place(relx=0.75, rely=0.15, relwidth=0.2, relheight=0.09)

        self._clear = Button(self._main_frame, text="CLEAR", bg="light green", font=(None, 10), command=lambda: self._clear_screen())
        self._clear.place(relx=0.75, rely=0.05, relwidth=0.2, relheight=0.09)

    # Logic for all buttons & Performs Operation
    def _output_keypad_press(self, action):
        return self._OPTIONS[action]

    def _get_input(self):  # This function gets the operation in the text box and sets global variable operation equals to that
        self._operation = self._output.get("1.0", END)

    def _calculate(self, operation):  # Takes operation from text box. Splits numbers and Operands and performs operation based on those.

        if '/' in operation.rstrip().strip(" "):
            try:
                result = float(sympy.sympify(operation.rstrip()))
                self._output.insert(END, result)
            except TypeError:
                self._output.insert(END, "ERROR - ZERO DIVISION")
            except IndexError:  # If user left open ended operation
                self._output.insert(END, "ERROR")
                pass
        else:
            result = sympy.sympify(operation.rstrip())
            self._output.insert(END, result)

    def _clear_screen(self):  # Clears output text box

        self._output.delete("1.0", END)


def start():
    root = Tk()
    CalculatorApp(root)
    root.mainloop()