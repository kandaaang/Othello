#Kan Dang 54515091 Lab 4 Safir

import tkinter
import othello_greeting as og_gui
import othello_pointer

DEFAULT_FONT = ('Verdana', 12)
BOX_LENGTH = 75

class OthelloBoard:
    def __init__(self):
        
        self._root_window = tkinter.Tk()
        self._root_window.title('Kan\'s Othello Program FULL')

        self._canvas = tkinter.Canvas(
            master = self._root_window, background = 'green', width = og_gui.oth.BOARD_COLUMNS*BOX_LENGTH, height = og_gui.oth.BOARD_ROWS*BOX_LENGTH)

        self._canvas.grid(
            row = 1, column = 0, padx = 10, pady = 10,
            sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)

        self._canvas.bind('<Configure>', self._canvas_resize)
        self._canvas.bind('<Button-1>', self._on_canvas_click)

        self._root_window.rowconfigure(1, weight = 1)
        self._root_window.columnconfigure(0, weight = 1)

        self._counter_text = tkinter.StringVar()
        self._counter_text.set('Black: 0, White: 0')

        self.title_label = tkinter.Label(
            master = self._root_window, textvariable = self._counter_text,
            font = DEFAULT_FONT)

        self.title_label.grid(row = 0, column = 0, padx = 10, pady = 10,
                         sticky = tkinter.N)

        self._winner_text = tkinter.StringVar()
        self._winner_text.set('Winner: None')

        self.bottom_label = tkinter.Label(
            master = self._root_window, textvariable = self._winner_text,
            font = DEFAULT_FONT)

        self.bottom_label.grid(row = 4, column = 0, padx = 10, pady = 10,
                               sticky = tkinter.S)             

    def _on_canvas_click(self, event: tkinter.Event):
        'On click, attempts to make a move based on points, if valid' 
        
        width = self._canvas.winfo_width()
        height = self._canvas.winfo_height()

        click_point = othello_pointer.from_pixel(event.x, event.y, width, height)
        moves = self.check_coordinates(event.y, event.x)

        try:
            playthegame.place(moves[0], moves[1])
        except:
            pass

        self._redraw_squares()


    def canvas_and_fracts(self) -> list:
        'Updates the canvas width and height and fracs and returns as a list'
        canvas_width = self._canvas.winfo_width()
        canvas_height = self._canvas.winfo_height()

        xfract = canvas_width/(og_gui.oth.BOARD_COLUMNS*BOX_LENGTH)
        yfract = canvas_height/(og_gui.oth.BOARD_ROWS*BOX_LENGTH)

        return (canvas_width, canvas_height, xfract, yfract)
    
    def check_coordinates(self, a: 'eventx', b: 'eventby'):
        'Takes the coordinates of the click, and returns as a list'

        cvfract = self.canvas_and_fracts()

        x = int(a/(cvfract[3] * BOX_LENGTH))
        y = int(b/(cvfract[2] * BOX_LENGTH))
        
        return (x, y)

    def _canvas_resize(self, event: tkinter.Event):
        'Resizes the canvas and calls the redraw method'
        self._canvas.delete(tkinter.ALL)
        self._redraw_squares()

    def _redraw_squares(self) -> None:
        'Redraws the gameboard'
        
        self._canvas.delete(tkinter.ALL)

        cvfract = self.canvas_and_fracts()
        
        for i in range(og_gui.oth.BOARD_ROWS):
            for j in range(og_gui.oth.BOARD_COLUMNS):
                self._canvas.create_rectangle(1 + j * (BOX_LENGTH * cvfract[2]), 1 + i * (BOX_LENGTH * cvfract[3]),
                                              (BOX_LENGTH * cvfract[2]) + j * (BOX_LENGTH * cvfract[2]), (BOX_LENGTH * cvfract[3]) + i * (BOX_LENGTH * cvfract[3]), fill = 'green')


        for i in range(og_gui.oth.BOARD_ROWS):
            for j in range(og_gui.oth.BOARD_COLUMNS):
                if playthegame._board[j][i] == 1:
                    self._canvas.create_oval(1 + j * (BOX_LENGTH * cvfract[2]), 1 + i * (BOX_LENGTH * cvfract[3]),
                                             (BOX_LENGTH * cvfract[2]) + j * (BOX_LENGTH * cvfract[2]), (BOX_LENGTH * cvfract[3]) + i * (BOX_LENGTH *cvfract[3]), fill = 'white', outline = 'grey')
                elif playthegame._board[j][i] == 2:
                    self._canvas.create_oval(1 + j * (BOX_LENGTH * cvfract[2]), 1 + i * (BOX_LENGTH * cvfract[3]),
                                             (BOX_LENGTH * cvfract[2]) + j * (BOX_LENGTH * cvfract[2]), (BOX_LENGTH * cvfract[3]) + i * (BOX_LENGTH * cvfract[3]), fill = 'black', outline = 'grey')

        self._counter_text.set('Black: ' + str(playthegame._blackcount) + ' White: ' + str(playthegame._whitecount))
        
        
        self.check_winner()
        self.display_turn_player()

    def display_turn_player(self) -> None:
        'Changes the text of the label to display the player'

        if playthegame._winner == None:
            if playthegame._turn == og_gui.oth.BLACK:
                turnplayer = 'Turn: Black'
            elif playthegame._turn == og_gui.oth.WHITE:
                turnplayer = 'Turn: White'

            self._winner_text.set(turnplayer)

    def check_winner(self) -> None:
        'Checks for the winner and changes bottom text to display it'
        self.display_turn_player()
        
        if not playthegame.valid_moves_left():
            playthegame.opposite_turn()
            self.display_turn_player()
        
            playthegame.winner()
            if playthegame._winner != None:
                if playthegame._winner == og_gui.oth.WHITE:
                    self._winner_text.set('WINNER: WHITE')
                elif playthegame._winner == og_gui.oth.BLACK:
                    self._winner_text.set('WINNER: BLACK')
                elif playthegame._winner == 'NONE':
                    self._winner_text.set('WINNER: TIE')
                
    def run(self):
        'Runs the OthelloBoard'
        self._root_window.mainloop()

if __name__ == '__main__':
    
    settings = og_gui.GameSettings()
    settings.start()
    if settings.was_ok_clicked():
        playthegame = og_gui.oth.Gamestate((settings.FIRST_TURN, settings.STARTING_BOARD, settings.WIN_CONDITION))
        playthegame.starting_board()
        OthelloBoard().run()
