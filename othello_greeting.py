#Kan Dang 54515091 Lab 4 Safir

import othello as oth
import tkinter

DEFAULT_FONT = ('Verdana', 12)

class GameSettings:
    def __init__(self):
        self._dialog_window = tkinter.Tk()

        self._dialog_window.title('Kan\'s Othello Program')

        settings_label = tkinter.Label(
            master = self._dialog_window, text = 'Please enter the game settings',
            font = DEFAULT_FONT)

        settings_label.grid(
            row = 0, column = 0, columnspan = 2, padx = 10, pady = 10,
            sticky = tkinter.N)

        col_number_label = tkinter.Label(
            master = self._dialog_window, text = '# of Columns:',
            font = DEFAULT_FONT)

        col_number_label.grid(
            row = 1, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)

        self._col_number_entry = tkinter.Entry(
            master = self._dialog_window, width = 20, font = DEFAULT_FONT)

        self._col_number_entry.grid(
            row = 1, column = 1, padx = 10, pady = 1,
            sticky = tkinter.W + tkinter.E)

        col_dir_label = tkinter.Label(
            master = self._dialog_window, text = '(Even integer 4-16)',
            font = DEFAULT_FONT)

        col_dir_label.grid(
            row = 1, column = 2, padx = 10, pady = 10,
            sticky = tkinter.E)

        row_number_label = tkinter.Label(
            master = self._dialog_window, text = '# of Rows:',
            font = DEFAULT_FONT)

        row_number_label.grid(
            row = 2, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)

        self._row_number_entry = tkinter.Entry(
            master = self._dialog_window, width = 20, font = DEFAULT_FONT)

        self._row_number_entry.grid(
            row = 2, column = 1, padx = 10, pady = 10,
            sticky = tkinter.W + tkinter.E)

        row_dir_label = tkinter.Label(
            master = self._dialog_window, text = '(Even integer 4-16)',
            font = DEFAULT_FONT)

        row_dir_label.grid(
            row = 2, column = 2, padx = 10, pady = 10,
            sticky = tkinter.E)

        first_turn_label = tkinter.Label(
            master = self._dialog_window, text = 'First Turn:',
            font = DEFAULT_FONT)

        first_turn_label.grid(
            row = 3, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)

        self._first_turn_entry = tkinter.Entry(
            master = self._dialog_window, width = 20, font = DEFAULT_FONT)

        self._first_turn_entry.grid(
            row = 3, column = 1, padx = 10, pady = 10,
            sticky = tkinter.W + tkinter.E)

        first_turn_dir_label = tkinter.Label(
            master = self._dialog_window, text = 'BLACK or WHITE',
            font = DEFAULT_FONT)

        first_turn_dir_label.grid(
            row = 3, column = 2, padx = 10, pady = 10,
            sticky = tkinter.E)

        starting_position_label = tkinter.Label(
            master = self._dialog_window, text = 'Starting Board:',
            font = DEFAULT_FONT)

        starting_position_label.grid(
            row = 4, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)

        self._starting_position_entry = tkinter.Entry(
            master = self._dialog_window, width = 20, font = DEFAULT_FONT)

        self._starting_position_entry.grid(
            row = 4, column = 1, padx = 10, pady = 10,
            sticky = tkinter.W + tkinter.E)

        starting_position_dir_label = tkinter.Label(
            master = self._dialog_window, text = 'BLACK or WHITE',
            font = DEFAULT_FONT)

        starting_position_dir_label.grid(
            row = 4, column = 2, padx = 10, pady = 10,
            sticky = tkinter.E)

        win_condition_label = tkinter.Label(
            master = self._dialog_window, text = 'Win Condition:',
            font = DEFAULT_FONT)

        win_condition_label.grid(
            row = 5, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)

        self._win_condition_entry = tkinter.Entry(
            master = self._dialog_window, width = 20, font = DEFAULT_FONT)

        self._win_condition_entry.grid(
            row = 5, column = 1, padx = 10, pady = 10,
            sticky = tkinter.W + tkinter.E)

        win_condition_dir_label = tkinter.Label(
            master = self._dialog_window, text = '> or <',
            font = DEFAULT_FONT)

        win_condition_dir_label.grid(
            row = 5, column = 2, padx = 10, pady = 10,
            sticky = tkinter.E)

        button_frame = tkinter.Frame(master = self._dialog_window)

        button_frame.grid(
            row = 6, column = 0, columnspan = 2, padx = 10, pady = 10,
            sticky = tkinter.E + tkinter.S)

        ok_button = tkinter.Button(
            master = button_frame, text = 'OK', font = DEFAULT_FONT,
            command = self._on_ok_button)

        ok_button.grid(row = 0, column = 0, padx = 10, pady = 10)

        cancel_button = tkinter.Button(
            master = button_frame, text = 'Cancel', font = DEFAULT_FONT,
            command = self._on_cancel_button)

        cancel_button.grid(row = 0, column = 1, padx = 10, pady = 10)

        self._dialog_window.rowconfigure(5, weight = 1)
        self._dialog_window.columnconfigure(1, weight = 1)

        self._ok_clicked = False
        self._col_number = ''
        self._row_number = ''
        self._first_turn = ''
        self._starting_position = ''
        self._win_condition = ''

    def show(self) -> None:
        'Gives control over to dialog box'
        self._dialog_window.grab_set()
        self._dialog_window.wait_window()

    def was_ok_clicked(self) -> bool:
        'Returns of ok is clicked'
        return self._ok_clicked

    def get_col_number(self) -> str:
        'Returns value for col number entry'
        return self._col_number

    def get_row_number(self) -> str:
        'Returns value for row number entry'
        return self._row_number

    def get_first_turn(self) -> str:
        'Returns the first turn entry'
        return self._first_turn

    def get_starting_position(self) -> str:
        'Returns the starting position entry'
        return self._starting_position

    def get_win_condition(self) -> str:
        'Returns the win condition entry'
        return self._win_condition

    def _on_ok_button(self) -> None:
        'On clicking ok button, gets the information in entry forms'
        self._ok_clicked = True
        self._col_number = self._col_number_entry.get()
        self._row_number = self._row_number_entry.get()
        self._first_turn = self._first_turn_entry.get()
        self._starting_position = self._starting_position_entry.get()
        self._win_condition = self._win_condition_entry.get()

        self._apply_settings()
        self._dialog_window.destroy()

    def _on_cancel_button(self) -> None:
        'On clicking cancel button, closes window'
        CANCELED = True
        self._dialog_window.destroy()

    def _decide_first_turn(self, a: str) -> None:
        'Decides the first turn player'
        if 'B' in a or 'b' in a:
            self.FIRST_TURN = oth.BLACK
        else:
            self.FIRST_TURN = oth.WHITE

    def _decide_win_condition(self, a: str) -> None:
        'Decides the win condition'
        if a == '>':
            self.WIN_CONDITION = '>'
        else:
            self.WIN_CONDITION = '<'

    def _decide_starting_board(self, a: str) -> None:
        'Decides the starting board'
        if 'B' in a or 'b' in a:
            self.STARTING_BOARD = oth.BLACK
        else:
            self.STARTING_BOARD = oth.WHITE

    def start(self) -> None:
        'Begins prompts'
        self._dialog_window.mainloop()

    def _apply_settings(self) -> None:
        'Sets the settings according to input if OK was clicked'
        
        if self.was_ok_clicked():
            oth.BOARD_COLUMNS = int(self.get_col_number())
            oth.BOARD_ROWS = int(self.get_row_number())
            self._decide_first_turn(self.get_first_turn())
            self._decide_starting_board(self.get_starting_position())
            self._decide_win_condition(self.get_win_condition())
                        


        
    

    
