from board import *
from move_adapter import *
from player import *
import sys
from board_version_manager import *
import copy


class CLI:

    def __init__(self):
        self.board = Board() # create a board object
        self.settings = None
        self.board_version_manager = Board_Version_Manager() # this is for history which will be implemented later

    def get_players(self, inputs): # looking at the command line inputs, return the settings that we have found
            output = []
            for input in inputs:
                if input == 'human':
                    output.append(HumanPlayer())
                elif input == 'random':
                    output.append(RandomPlayer())
                elif input == 'greedy':
                    output.append(ComputerPlayer())
                elif input == 'on':
                    output.append('on')
                elif input == 'off':
                    output.append('off')
            return output

    def _display_menu(self): # the thing that needs to be displayed every time regardless of the player
        print(self.board)
        print(f"Turn: {self.board.move}, {self.board.cur_player.color}")

    def run(self):
        if self.settings[2] == 'on': # if we are saving board came history, save the initial board state
            self.board_version_manager.append_state(copy.deepcopy(self.board))
        while True: # enter the game
            self._display_menu()
            moves = self.board.available_moves_all() # get all of the available moves for the current player, all pieces
            if self.board.check_winner(moves) is not False: # check if there is a winner on the board, if there is exit the game
                print(self.board.check_winner(moves))
                break
            if type(self.board.cur_player) == HumanPlayer: # if we have a human player we need to get more data from them
                result = False
                while result is False: # while the human selects a piece that cannot move
                    message = 'Select a piece to move'
                    if self.settings[2] == 'on':
                        message += ', undo, redo, or next.'
                    print(message)
                    user_in = input()
                    if self.settings[2] == 'on' and user_in == 'undo':
                        self.board = self.board_version_manager.undo()
                        self._display_menu()
                    elif self.settings[2] == 'on' and user_in == 'redo':
                        self.board = self.board_version_manager.re_do()
                        self._display_menu()
                    elif self.settings[2] == 'on' and user_in == 'next':
                        self.board_version_manager.next()
                        self._display_menu()
                    else:
                        piece = user_in
                        result = self.board.available_moves_piece(piece, moves) # see if there are available moves in our "all moves" list for our current piece
                        if result == 'no move': # if there is no available moves, try again
                            print('That piece cannot move')
                            result = False
                        elif result == 'no piece':
                            print('No piece at that location')
                            result = False
                        elif result == 'wrong piece':
                            print('That is not your piece')
                            result = False
                for i in range(0, len(result)): # once they select a piece that can move, print out all the moves for that piece
                    print(str(i) + ': '+ str(result[i]))
                print('Select a move by entering the corresponding index')
                choice = input()
                self.board.make_move(moves, choice, piece) # update the board to reflect the move the player specified
            else:
                self.board.make_move(moves) # if not a human player, go right into make move with the AI
            self.board.update_move() # increments our current turn by one
            self.board.update_cur_player() # flips what palyer is current player

            if self.settings[2] == 'on': # if we are saving the history, save the curernt board state
                self.board_version_manager.append_state(copy.deepcopy(self.board))


if __name__ == "__main__":
    inputs = list(sys.argv) # get the command line arguments for history and type of player
    cli = CLI() # create a command line manager object
    settings = [HumanPlayer(), HumanPlayer(), 'off'] # set the default settings
    inputs = cli.get_players(inputs[1:]) # get the actual settings from the command line arguments
    if len(inputs) < len(settings): # if not all of the settings specified, get the remaining from the defaults
        settings = inputs + settings[len(inputs):]
    else:
        settings = inputs
    settings[0].color = 'white' #set the first player to white and the second player to black
    settings[1].color = 'black'
    cli.settings = settings # update the settings in our CLU manager
    cli.board.cur_player = settings[0] # set the first player
    cli.board.settings = settings # set the settings in our board
    cli.run() # start running the command line
