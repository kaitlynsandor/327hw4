from board import *
from move_adapter import *
from player import *
import sys

class CLI:

    def __init__(self):
        self.board = Board()
        self.commands = {}

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
        print(f"Current Board: {self.board}")
        options = ", ".join(self.commands.keys())
        print('Enter command')
        print(options)

    def run(self):

        while True:
            self._display_menu()
            choice = input()
            action = self.commands.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))


if __name__ == "__main__":
    inputs = str(sys.argv)
    settings = [HumanPlayer(), HumanPlayer(), 'off']
    cli = CLI()
    inputs = cli.get_players(inputs)
    if len(inputs) < len(settings):
        settings = inputs + settings[len(inputs)+1:]
    else:
        settings = inputs

    cli.run()
