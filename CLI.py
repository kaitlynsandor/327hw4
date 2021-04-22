from board import *
from move_adapter import *
from player import *
import sys

class CLI:

    def __init__(self):
        self.board = Board()
        self.commands = {}
        self.move = 1
        self.settings = None
        self.colors = ['black', 'white']
        self.cur_player = None

    def get_players(self, inputs):
            output = []
            for input in inputs:
                if input == 'human':
                    output.append(HumanPlayer())
                elif input == 'random':
                    output.append(RandomPlayer())
                elif input == 'computer':
                    output.append(ComputerPlayer())
                elif input == 'on':
                    output.append('on')
                elif input == 'off':
                    output.append('off')
            return output

    def _display_menu(self):
        print(self.board)
        print(f"Turn: {self.move}, {self.colors[self.move%2]}")

    def run(self):

        while True:
            self._display_menu()
            if self.board.check_winner():
                print('yay end of game')
            moves = self.board.available_moves_all()
            if type(self.cur_player) == HumanPlayer:
                print('Select a piece to move')
                choice = input()
                result = self.board.available_moves_piece(choice, moves)
                print('Select a move by entering the corresponding index')
                choice = input()
                self.board.make_move(choice, result)
            else:
                self.board.make_move(moves)


            self.move += 1
            self.cur_player = self.settings[(self.move+1) % 2] # update current player to switch


if __name__ == "__main__":
    inputs = list(sys.argv)
    cli = CLI()
    settings = [HumanPlayer(), HumanPlayer(), 'off']
    inputs = cli.get_players(inputs[1:])
    if len(inputs) < len(settings):
        settings = inputs + settings[len(inputs):]
    else:
        settings = inputs
    cli.settings = settings
    print(settings)
    cli.cur_player = settings[0]
    cli.run()
