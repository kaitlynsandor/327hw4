from board import *
from move_adapter import *
from player import *
import sys
from board_version_manager import *
import copy


class CLI:

    def __init__(self):
        self.board = Board()
        self.settings = None
        self.board_version_manager = Board_Version_Manager()

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
        print(f"Turn: {self.board.move}, {self.board.cur_player.color}")

    def run(self):
        if self.settings[2] == 'on':
            self.board_version_manager.append_state(copy.deepcopy(self.board))
        while True:
            self._display_menu()
            moves = self.board.available_moves_all()
            if self.board.check_winner(moves) is not False:
                print(self.board.check_winner(moves))
            if type(self.board.cur_player) == HumanPlayer:
                result = False
                while result is False:
                    print('Select a piece to move')
                    piece = input()
                    result = self.board.available_moves_piece(piece, moves)
                    if not result:
                        print('That piece cannot move')
                for i in range(0, len(result)):
                    print(str(i) + ': '+ str(result[i]))
                print('Select a move by entering the corresponding index')
                choice = input()
                self.board.make_move(moves, choice, piece)
            else:
                self.board.make_move(moves)
            self.board.update_move()
            self.board.update_cur_player()

            if self.settings[2] == 'on':
                self.board_version_manager.append_state(copy.deepcopy(self.board))


if __name__ == "__main__":
    inputs = list(sys.argv)
    cli = CLI()
    settings = [HumanPlayer(), HumanPlayer(), 'off']
    inputs = cli.get_players(inputs[1:])
    if len(inputs) < len(settings):
        settings = inputs + settings[len(inputs):]
    else:
        settings = inputs
    settings[0].color = 'white'
    settings[1].color = 'black'
    cli.settings = settings
    cli.board.cur_player = settings[0]
    cli.board.settings = settings
    cli.run()
