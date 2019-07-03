#Kan Dang 54515091 Lab Section 4, Safir
#othello.py
#
#ICS 32 Spring 2016
#Project #4: Width of a Circle

'''
This module contains the game logic that underlies the Othello game.
Some examples of things to include are:
    Get the number of rows and/or columns on the board.
    Find out whose turn it is.
    Determine whether the game is over.
    Determine whether a disc is in some cell in the grid; if so, determine its color.
    Make a move.
All in the form of a class.
'''

# These constants specify the concepts of
# "no player", "white player", and "black player"

NONE = 0
WHITE = 1
BLACK = 2

# These constants will specify the size of the game board. It is possible to
# change these constants and re-run the program

BOARD_COLUMNS = 6
BOARD_ROWS = 6

# These are the exceptions that will be raised.

class InvalidMoveError(Exception):
    '''Raised whenever an invalid move is made'''
    pass

class AdjacencyError(Exception):
    '''Raised whenever there is no adjacent piece'''
    pass

class GameOverError(Exception):
    '''Raised whenever an attempt is made to make a move after the game
    is already over'''
    pass


# GameState class. This class will have attributes of an othello game including:
# board, turn, starting_board, blackcount, whitecount, winner, wincondition.

class Gamestate:
    
    def __init__(self, a):
        self.set_attributes(a)


    def set_attributes(self, a: list) -> None:
        'From a list sets the characteristics of the Gamestate'
        self._board = self._new_game_board() 
        self._turn = a[0]
        self._starting_board = a[1]
        self._blackcount = 0
        self._whitecount = 0
        self._winner = None
        self._wincondition = a[2]
        self._pieceatend = False
        self._fliplist = []
        
    def return_board(self) -> [[list]]:
        '''Returns the board as a list'''
        return self._board

    def return_turn(self) -> 'player':
        '''Returns the turn player'''
        return self._turn

    def return_starting_board(self) -> 'player':
        '''Returns starting board player'''
        return self._starting_board

    def return_blackcount(self) -> 'int':
        '''Returns the count of black pieces'''
        return self._blackcount

    def return_whitecount(self) -> 'int':
        '''Returns the count of white pieces'''
        return self._whitecount

    def return_winner(self) -> 'player':
        'Returns the winning player'
        return self._winner

    def return_win_condition(self) -> 'str':
        'Returns the win condition symbol'
        return self._wincondition

    def return_fliplist(self) -> 'list':
        'Returns the list of coordinates to be flipped'
        return self._fliplist

    def reset_fliplist(self) -> None:
        'Resets the fliplist to empty'
        self._fliplist = []

    def starting_board(self) -> list:
        '''Decides the starting board'''
        blankboard = self._new_game_board()
        blankboard[int(len(blankboard)/2)][int(len(blankboard[0])/2)] = self.return_starting_board()
        blankboard[int(len(blankboard)/2)-1][int(len(blankboard[0])/2)-1] = self.return_starting_board()
        self._opposite_starting_board()
        blankboard[int(len(blankboard)/2)][int(len(blankboard[0])/2)-1] = self.return_starting_board()
        blankboard[int(len(blankboard)/2)-1][int(len(blankboard[0])/2)] = self.return_starting_board()
        
        self._board = blankboard

    def place(self, row_number: int, column_number: int)  -> None:
        '''Given a column # and row #, changes teh gamestate based on the move
        if it is a valid move, else InvalidMoveError is raised.
        If the game is over, GameOverError is raised.'''

        self.reset_fliplist()
        self._require_valid_column_number(column_number)
        self._require_valid_row_number(row_number)
        self._require_game_not_over()
        self._require_valid_move(self.all_directions(row_number, column_number))

        if self.return_board()[column_number][row_number] != 0:
            raise InvalidMoveError()

        else:
            self._board[column_number][row_number] = self._turn
            self.flip(self.return_fliplist())
            self.opposite_turn()
            self.count_pieces()

    def piece_check(self, row: int, col: int, rowdelta: int, coldelta: int) -> bool:
        '''Checks if the piece is the same color, if it is not, it flips and continues
        if it is, it stops'''

        move_list = []
        valid = False
        while self._is_valid_column_number(col + coldelta) and self._is_valid_row_number(row + rowdelta):
            if self._board[col + coldelta][row + rowdelta] == 0:
                break
            elif self._board[col + coldelta][row + rowdelta] != self._turn:
                move_list.append((col + coldelta, row + rowdelta))
                valid = True
                row += rowdelta
                col += coldelta
            elif self._board[col + coldelta][row + rowdelta] == self._turn:
                if valid == False: 
                    break
                else:
                    self._fliplist.append(move_list)
                    return True
                    break
                
        return False

    def all_directions(self, row: int, col: int) -> list:
        '''Runs the piece_check function in all eight directions to check if valid move'''
        result = []
        result.append(self.piece_check(row, col, 0, 1))
        result.append(self.piece_check(row, col, 1, 1))
        result.append(self.piece_check(row, col, 1, 0))
        result.append(self.piece_check(row, col, 1, -1))
        result.append(self.piece_check(row, col, 0, -1))
        result.append(self.piece_check(row, col, -1, -1))
        result.append(self.piece_check(row, col, -1, 0))
        result.append(self.piece_check(row, col, -1, 1))

        return result

    def flip(self, a: list) -> None:
        '''Flips pieces that are not the same color'''
        for item in a:
            if type(item) == list:
                self.flip(item)
            else:
                self._board[item[0]][item[1]] = self.return_turn()

    def count_pieces(self):
        '''Counts the pieces for each color'''
        self._blackcount = 0
        self._whitecount = 0
        for item in self._board:
            for thing in item:
                if thing == BLACK:
                    self._blackcount += 1
                elif thing == WHITE:
                    self._whitecount += 1

    def winner(self) -> None:
        '''
        Determines if a player can make a move or not, if so, game continues, if not goes to check
        if the second player can in another function
        '''
        emptyspacesleft = self.empty_spaces_left()
        validmovesleft = self.valid_moves_left()          
                    
        if not emptyspacesleft:
            if self.return_win_condition() == '>':
                self.greater_piece_winner()
            else:
                self.lesser_piece_winner()
        else:
            if not validmovesleft:
                if self.return_win_condition() == '>':
                    self.greater_piece_winner()
                else:
                    self.lesser_piece_winner()

    def empty_spaces_left(self) -> bool:
        '''Determines if there are empty spaces left'''
        emptyspacesleft = False
        
        for i in range(BOARD_ROWS):
            for j in range(BOARD_COLUMNS):
                if self._board[j][i] == 0:
                    emptyspacesleft = True
                    
        return emptyspacesleft

    def valid_moves_left(self) -> bool:
        '''Determines if the player has valid moves left'''
        validmovesleft = False
        
        for i in range(BOARD_ROWS):
            for j in range(BOARD_COLUMNS):
                if self._board[j][i] == 0:
                    if True in self.all_directions(i, j):
                        validmovesleft = True
                    
        return validmovesleft

    def greater_piece_winner(self) -> None:
        '''Changes winner to the one with more pieces'''
        self.count_pieces()
        if self.return_blackcount() > self.return_whitecount():
            self._winner = BLACK
        elif self.return_blackcount() < self.return_whitecount():
            self._winner = WHITE
        else:
            self._winner = 'NONE'

    def lesser_piece_winner(self) -> None:
        '''Changes winner to the one with less pieces'''
        self.count_pieces()
        if self.return_blackcount() < self.return_whitecount():
            self._winner = BLACK
        elif self.return_blackcount() > self.return_whitecount():
            self._winner = WHITE
        else:
            self._winner = 'NONE'

    def _new_game_board(self) -> [[int]]:
        '''Creates a new game board'''
        board = []
        for col in range(BOARD_COLUMNS):
            board.append([])
            for row in range(BOARD_ROWS):
                board[-1].append(NONE)

        return board

    def opposite_turn(self) -> str:
        '''Given the current player turn, returns opposite player'''
        if self.return_turn() == WHITE:
            self._turn = BLACK
        else:
            self._turn = WHITE

    def _opposite_starting_board(self) -> str:
        '''Given the current player turn, returns opposite player'''
        if self.return_starting_board() == WHITE:
            self._starting_board = BLACK
        else:
            self._starting_board = WHITE
    
    def _require_valid_column_number(self, column_number: int) -> None:
        '''Raises a ValueError if its paremeter is not a valid column number'''
        if type(column_number) != int or not self._is_valid_column_number(column_number):
            raise ValueError('column_number must be int between 0 and {}'.format(BOARD_COLUMNS - 1))

    def _require_valid_row_number(self, row_number: int) -> None:
        '''Raises a ValueError if its paremeter is not a valid row number'''
        if type(row_number) != int or not self._is_valid_row_number(row_number):
            raise ValueError('column_number must be int between 0 and {}'.format(BOARD_ROWS - 1))

    def _require_valid_move(self, a: list) -> None:
        '''Raises an InvalidMoveError if it is not a legal move'''
        if True not in a:
            raise InvalidMoveError()

    def _require_game_not_over(self) -> None:
        '''Raises a GameOverError if the game is over'''
        if self.return_winner() != None:
            raise GameOverError()

    def _is_valid_column_number(self, column_number: int) -> bool:
        '''Returns True if the given column number is valid; return False otherwise'''
        return 0 <= column_number < BOARD_COLUMNS

    def _is_valid_row_number(self, row_number: int) -> bool:
        '''Returns True if the given row number is valid; returns False otherwise'''
        return 0 <= row_number < BOARD_ROWS


