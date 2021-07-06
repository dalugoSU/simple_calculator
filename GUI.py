# import tkinter as tk
import tkinter as tk
from GUI_CONSTANTS import WindowButtons, WindowDimensions, NumberButtons, OperationButtons, OutputScreen
import sympy
import logging

logging.basicConfig(level=logging.INFO)


class CalculatorApp:

    def __init__(self):  # Initializes factors of calculator that affects the GUI
        self._root = None
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
        self._result = None

    def __repr__(self):
        return f"Tkinter Calculator "

    def run(self):
        self._root = tk.Tk()
        self._main_screen()
        self._main_frame()
        logging.info("Loaded main frame no error")
        self._number_buttons()
        logging.info("Loaded Buttons no Error")
        self._operation_buttons()
        self._output = tk.Text(self._root_main_frame, bg="white", font=(None, 15))
        self._output.place(relx=OutputScreen.OUTPUT_REL_X, rely=OutputScreen.OUTPUT_REL_Y,
                           relwidth=OutputScreen.OUTPUT_REL_WIDTH, relheight=OutputScreen.OUTPUT_REL_HEIGHT)
        logging.info("Loaded output screen no Error")
        logging.info("Initialized Calculator No Error")
        self._root.mainloop()

    def _main_screen(self):  # Main Screen function. It gives the root window basic dimensions and title
        self._root.title(WindowDimensions.WINDOW_TITLE)
        self._root.minsize(WindowDimensions.MIN_X, WindowDimensions.MAX_Y)
        self._root.maxsize(WindowDimensions.MAX_X, WindowDimensions.MAX_Y)

    def _main_frame(self):  # Main Screen where everything will sit. It is on top of the root window
        self._root_main_frame = tk.Frame(self._root, bg="light grey")
        self._root_main_frame.pack(fill='both', expand=True)

    def _number_buttons(self):  # All number Buttons. Initialization and Placement. Each has command calling its designated function
        self._button0 = tk.Button(self._root_main_frame, text=0, bg="light gray",
                                  font=(None, 10), command=lambda: self._output_keypad_press(WindowButtons.ZERO))
        self._button0.place(relx=NumberButtons.ZERO_REL_X, rely=NumberButtons.ZERO_REL_Y,
                            relwidth=NumberButtons.ZERO_REL_WIDTH, relheight=NumberButtons.ZERO_REL_HEIGHT)

        self._dotButton = tk.Button(self._root_main_frame, text=".", bg="light gray",
                                    font=(None, 10), command=lambda: self._output_keypad_press(WindowButtons.DOT))
        self._dotButton.place(relx=NumberButtons.DOT_REL_X, rely=NumberButtons.DOT_REL_Y,
                              relwidth=NumberButtons.DOT_REL_WIDTH, relheight=NumberButtons.DOT_REL_HEIGHT)

        self._button1 = tk.Button(self._root_main_frame, text=1, font=(None, 15),
                                  command=lambda: self._output_keypad_press(WindowButtons.ONE))
        self._button1.place(relx=NumberButtons.ONE_REL_X, rely=NumberButtons.ONE_REL_Y,
                            relwidth=NumberButtons.ONE_REL_WIDTH, relheight=NumberButtons.ONE_REL_HEIGHT)

        self._button2 = tk.Button(self._root_main_frame, text=2, font=(None, 15),
                                  command=lambda: self._output_keypad_press(WindowButtons.TWO))
        self._button2.place(relx=NumberButtons.TWO_REL_X, rely=NumberButtons.TWO_REL_Y,
                            relwidth=NumberButtons.TWO_REL_WIDTH, relheight=NumberButtons.TWO_REL_HEIGHT)

        self._button3 = tk.Button(self._root_main_frame, text=3, font=(None, 15),
                                  command=lambda: self._output_keypad_press(WindowButtons.THREE))
        self._button3.place(relx=NumberButtons.THREE_REL_X, rely=NumberButtons.THREE_REL_Y,
                            relwidth=NumberButtons.THREE_REL_WIDTH, relheight=NumberButtons.THREE_REL_HEIGHT)

        self._button4 = tk.Button(self._root_main_frame, text=4, font=(None, 15),
                                  command=lambda: self._output_keypad_press(WindowButtons.FOUR))
        self._button4.place(relx=NumberButtons.FOUR_REL_X, rely=NumberButtons.FOUR_REL_Y,
                            relwidth=NumberButtons.FOUR_REL_WIDTH, relheight=NumberButtons.FOUR_REL_HEIGHT)

        self._button5 = tk.Button(self._root_main_frame, text=5, font=(None, 15),
                                  command=lambda: self._output_keypad_press(WindowButtons.FIVE))
        self._button5.place(relx=NumberButtons.FIVE_REL_X, rely=NumberButtons.FIVE_REL_Y,
                            relwidth=NumberButtons.FIVE_REL_WIDTH, relheight=NumberButtons.FIVE_REL_HEIGHT)

        self._button6 = tk.Button(self._root_main_frame, text=6, font=(None, 15),
                                  command=lambda: self._output_keypad_press(WindowButtons.SIX))
        self._button6.place(relx=NumberButtons.SIX_REL_X, rely=NumberButtons.SIX_REL_Y,
                            relwidth=NumberButtons.SIX_REL_WIDTH, relheight=NumberButtons.SIX_REL_HEIGHT)

        self._button7 = tk.Button(self._root_main_frame, text=7, font=(None, 15),
                                  command=lambda: self._output_keypad_press(WindowButtons.SEVEN))
        self._button7.place(relx=NumberButtons.SEVEN_REL_X, rely=NumberButtons.SEVEN_REL_Y,
                            relwidth=NumberButtons.SEVEN_REL_WIDTH, relheight=NumberButtons.SEVEN_REL_HEIGHT)

        self._button8 = tk.Button(self._root_main_frame, text=8, font=(None, 15),
                                  command=lambda: self._output_keypad_press(WindowButtons.EIGHT))
        self._button8.place(relx=NumberButtons.EIGHT_REL_X, rely=NumberButtons.EIGHT_REL_Y,
                            relwidth=NumberButtons.EIGHT_REL_WIDTH, relheight=NumberButtons.EIGHT_REL_HEIGHT)

        self._button9 = tk.Button(self._root_main_frame, text=9, font=(None, 15),
                                  command=lambda: self._output_keypad_press(WindowButtons.NINE))
        self._button9.place(relx=NumberButtons.NINE_REL_X, rely=NumberButtons.NINE_REL_Y,
                            relwidth=NumberButtons.NINE_REL_WIDTH, relheight=NumberButtons.NINE_REL_HEIGHT)

    def _operation_buttons(self):  # Operational buttons. Initialization and placement. Each has command calling its designated function
        self._multiply = tk.Button(self._root_main_frame, text="X", bg="light gray",
                                   font=(None, 10), command=lambda: self._output_keypad_press(WindowButtons.MULTIPLY))
        self._multiply.place(relx=OperationButtons.MULTIPLY_REL_X, rely=OperationButtons.MULTIPLY_REL_Y,
                             relwidth=OperationButtons.MULTIPLY_REL_WIDTH, relheight=OperationButtons.MULTIPLY_REL_HEIGHT)

        self._divide = tk.Button(self._root_main_frame, text="/", bg="light gray",
                                 font=(None, 10), command=lambda: self._output_keypad_press(WindowButtons.DIVIDE))
        self._divide.place(relx=OperationButtons.DIVIDE_REL_X, rely=OperationButtons.DIVIDE_REL_Y,
                           relwidth=OperationButtons.DIVIDE_REL_WIDTH, relheight=OperationButtons.DIVIDE_REL_HEIGHT)

        self._add = tk.Button(self._root_main_frame, text="+", bg="light gray",
                              font=(None, 15), command=lambda: self._output_keypad_press(WindowButtons.ADD))
        self._add.place(relx=OperationButtons.ADD_REL_X, rely=OperationButtons.ADD_REL_Y,
                        relwidth=OperationButtons.ADD_REL_WIDTH, relheight=OperationButtons.ADD_REL_HEIGHT)

        self._subtract = tk.Button(self._root_main_frame, text="-", bg="light gray",
                                   font=(None, 15), command=lambda: self._output_keypad_press(WindowButtons.SUBTRACT))
        self._subtract.place(relx=OperationButtons.SUBTRACT_REL_X, rely=OperationButtons.SUBTRACT_REL_Y,
                             relwidth=OperationButtons.SUBTRACT_REL_WIDTH, relheight=OperationButtons.SUBTRACT_REL_HEIGHT)

        self._equal = tk.Button(self._root_main_frame, text="=", bg="light green", font=(None, 15),
                                command=lambda: [self._get_input(), self._clear_screen(), self._calculate(self._operation)])
        self._equal.place(relx=OperationButtons.EQUAL_REL_X, rely=OperationButtons.EQUAL_REL_Y,
                          relwidth=OperationButtons.EQUAL_REL_WIDTH, relheight=OperationButtons.EQUAL_REL_HEIGHT)

        self._clear = tk.Button(self._root_main_frame, text="CLEAR", bg="light green",
                                font=(None, 10), command=lambda: self._clear_screen())
        self._clear.place(relx=OperationButtons.CLEAR_REL_X, rely=OperationButtons.CLEAR_REL_Y,
                          relwidth=OperationButtons.CLEAR_REL_WIDTH, relheight=OperationButtons.CLEAR_REL_HEIGHT)

    # Logic for all buttons & Performs Operation
    def _output_keypad_press(self, action):
        try:
            int(action)
            message = f"{action}"
        except ValueError:
            message = f" {action} "
        self._output.insert(tk.END, message)
        logging.info(f"Output on screen: {message}")

    def _get_input(self):  # This function gets the operation in the text box and sets global variable operation equals to that
        self._operation = self._output.get("1.0", tk.END)
        logging.info(f"Got Operation: {self._operation}")

    def _calculate(self, operation):  # Takes operation from text box. Splits numbers and Operands and performs operation based on those.

        if '/' in operation.rstrip().strip(" "):
            try:
                self._result = float(sympy.sympify(operation.rstrip()))
                self._output.insert(tk.END, self._result)
                logging.info(f"Output result: {self._result}")
            except TypeError:
                self._output.insert(tk.END, "ERROR - ZERO DIVISION")
                logging.info("Type error in _calculate; If zero division, ignore")
            except IndexError:  # If user left open ended operation
                self._output.insert(tk.END, "ERROR")
                logging.info("Index Error in _calculate; If open ended operation, ignore")
                pass
        else:
            result = sympy.sympify(operation.rstrip())
            self._output.insert(tk.END, result)

    def _clear_screen(self):  # Clears output text box
        self._output.delete("1.0", tk.END)
        logging.info("Cleared Screen")

    def _stop(self):
        self._root.destroy()

