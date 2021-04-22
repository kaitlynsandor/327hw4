from move_adapter import *


class Move:
    def __init__(self, type, piece, jumps=None):
        self.type = type
        self.piece = piece
        self.jumps = jumps


class Board:
    def __init__(self):
        self.board = [['⚈', '◼', '⚈', '◼', '⚈', '◼', '⚈', '◼'],
                      ['◼', '⚈', '◼', '⚈', '◼', '⚈', '◼', '⚈'],
                      ['⚈', '◼', '⚈', '◼', '⚈', '◼', '⚈', '◼'],
                      ['◼', '◻', '◼', '◻', '◼', '◻', '◼', '◻'],
                      ['◻', '◼', '◻', '◼', '◻', '◼', '◻', '◼'],
                      ['◼', '⚆', '◼', '⚆', '◼', '⚆', '◼', '⚆'],
                      ['⚆', '◼', '⚆', '◼', '⚆', '◼', '⚆', '◼'],
                      ['◼', '⚆', '◼', '⚆', '◼', '⚆', '◼', '⚆'],]

    def __repr__(self):
        nums = [str(x) for x in range(1,9)]
        final_str = ''

        for i in range(0,8):
            string = ''
            for j in range(0,8):
                string += self.board[i][j] + ' '
            final_str += (nums[i] + ' ' + string + '\n')
        final_str += ('  a b c d e f g h')
        return final_str



    def available_moves_all(self):
        pass
        # all available moves, not from a certain piece

    def available_moves_piece(self, piece, moves):
        moves = []
        # check if there is a move for this piece in all available moves and if so that it either is a jump or
        # there are no other jumps available
        pass

    def check_winner(self):
        pass

    def make_move(self, moves, choice=None,): # calls the player move function to get the best move
        adapter = Move_Adapter()
        pass # update the board to reflect the made move, return the new board for the undo function


class BoardStates:
    def __init__(self):
        pass
