from move_adapter import *
from piece import *


class Move:
    def __init__(self, start, end, piece, type, jumps=None):
        self.type = type
        self.piece = piece
        self.start = start
        self.jumps = jumps
        self.end = end

    def __repr__(self):
        final_str = self.type + ': ' + self.start + '->' + self.end
        if self.type == 'jump move':
            final_str += ', capturing ' + str(self.jumps)
        return final_str


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

    def available_moves_piece(self, piece, moves):
        pass
        # all available moves, not from a certain piece

    def available_moves_all(self, moves):
        final_moves = {}
        adapter = Move_Adapter()
        for i in range(0, len(self.board)):
            for j in range(0, len(self.board[i])):
                moves = []
                piece = self.board[i][j] # TO DO: make sure i and j are in bounds before trying to read from them
                if type(piece) == Piece and piece.color == self.cur_player.color:
                    if not piece.is_king:
                        spaces_to_check = []
                        if piece.color == 'black':
                            spaces_to_check.append([self.board[i+1][j-1], [i+1, j-1]])
                            spaces_to_check.append([self.board[i+1][j+1], [i+1, j+1]])
                        else: # if the piece is white
                            spaces_to_check.append([self.board[i - 1][j - 1], [i-1, j-1]])
                            spaces_to_check.append([self.board[i - 1][j + 1], [i-1], [j+1]])

                        for space in spaces_to_check:
                            if type(space[0]) == Piece and space[0].color != self.cur_player.color:
                                # check for how many jumps possible, add this to a move and save it
                                pass
                            elif space[0] == '◻':
                                moves.append(Move(adapter.convert_matrix_coord([i, j]), # position we start
                                                  adapter.convert_matrix_coord(space[1]), # position we end
                                                  space[0], #piece
                                                  'basic move')) #type of move
                    else:
                        # TO DO: implement king moves
                        pass
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
        nums = [str(x) for x in range(1, 9)]
        final_str = ''

        for i in range(0, 8):
            string = ''
            for j in range(0,8):
                string += self.board[i][j] + ' '
            final_str += (nums[i] + ' ' + string + '\n')
        final_str += '  a b c d e f g h'
        return final_str


class BoardStates:
    def __init__(self):
        pass
