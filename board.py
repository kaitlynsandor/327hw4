from move_adapter import *
from piece import *


class Move:
    def __init__(self, value, piece, type, jumps=None):
        self.type = type
        self.piece = piece
        self.value = value
        self.jumps = jumps


class Board:
    def __init__(self):
        self.board = [[Piece('⚈'), '◼', Piece('⚈'), '◼', Piece('⚈'), '◼', Piece('⚈'), '◼'],
                      ['◼', Piece('⚈'), '◼', Piece('⚈'), '◼', Piece('⚈'), '◼', Piece('⚈')],
                      [Piece('⚈'), '◼', Piece('⚈'), '◼', Piece('⚈'), '◼', Piece('⚈'), '◼'],
                      ['◼', '◻', '◼', '◻', '◼', '◻', '◼', '◻'],
                      ['◻', '◼', '◻', '◼', '◻', '◼', '◻', '◼'],
                      ['◼', Piece('⚆'), '◼', Piece('⚆'), '◼', Piece('⚆'), '◼', Piece('⚆')],
                      [Piece('⚆'), '◼', Piece('⚆'), '◼', Piece('⚆'), '◼', Piece('⚆'), '◼'],
                      ['◼', Piece('⚆'), '◼', Piece('⚆'), '◼', Piece('⚆'), '◼', Piece('⚆')]]
        self.cur_player = None
        self.move = 1
        self.settings = None

    def available_moves_all(self):
        pass
        # all available moves, not from a certain piece

    def available_moves_piece(self, moves):
        final_moves = {}
        adapter = Move_Adapter()
        for i in range(0, len(self.board)):
            for j in range(0, len(self.board[i])):
                moves = []
                piece = self.board[i][j]
                if type(piece) == Piece and piece.color == self.cur_player.color:
                    # check if it has valid moves
                final_moves[adapter.convert_matrix_coord([i,j])] = moves
                pass

        return moves

    def check_winner(self):
        return False

    def make_move(self, moves, choice=None,): # calls the player move function to get the best move
        adapter = Move_Adapter()
        pass # update the board to reflect the made move, return the new board for the undo function

    def update_cur_player(self):
        self.cur_player = self.settings[(self.move + 1) % 2]

    def update_move(self):
        self.move += 1

    def __repr__(self):
        nums = [str(x) for x in range(1,9)]
        final_str = ''

        for i in range(0,8):
            string = ''
            for j in range(0,8):
                string += self.board[i][j] + ' '
            final_str += (nums[i] + ' ' + string + '\n')
        final_str += '  a b c d e f g h'
        return final_str

class BoardStates:
    def __init__(self):
        pass
