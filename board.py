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
        self.moves_since_last_capture = 0

    def available_moves_piece(self, move_piece, moves):
        pieces = moves.keys()
        if move_piece not in pieces or moves[move_piece] == []:
            return False
        else:
            for move in moves[move_piece]:
                if move.type == 'jump move':
                    return moves[move_piece]
            else:
                for piece in pieces:
                    for move in moves[piece]:
                        if move.type == 'jump move':
                            return False
                return moves[move_piece]

    def available_moves_all(self):
        final_moves = {}
        adapter = Move_Adapter()
        for i in range(0, len(self.board)):
            for j in range(0, len(self.board[i])):
                moves = []
                piece = self.board[i][j] # TO DO: make sure i and j are in bounds before trying to read from them
                if type(piece) == Piece and piece.color == self.cur_player.color:
                    spaces_to_check = piece.spaces_to_check(i, j, self.board)
                    for space in spaces_to_check:
                        if type(space[0]) == Piece and space[0].color != self.cur_player.color:
                            row_dir = space[1][0] - i
                            col_dir = space[1][1] - j
                            if self.board[i + row_dir][j + col_dir] == '◻':
                                jumped = [adapter.convert_matrix_coord([space[1][0], space[1][1]])]
                                end = adapter.convert_matrix_coord([i + row_dir, j + col_dir])
                                k = i + 2 * row_dir
                                l = j + 2 * col_dir
                                while k < len(self.board) and j < len(self.board[0]) and type(self.board[k][l]) == Piece \
                                        and self.board[k][l].color == space[0].color:
                                    if 0 <= k + row_dir <= len(self.board) and 0 <=l + col_dir <= \
                                            len(self.board[0]):
                                        if self.board[k + row_dir][l + col_dir] == '◻':
                                            jumped.append([adapter.convert_matrix_coord([k, l])])
                                            end = adapter.convert_matrix_coord([k + row_dir, l + col_dir])
                                        k = k + row_dir
                                        l = l + col_dir
                                moves.append(Move(adapter.convert_matrix_coord([i, j]),  # position we start
                                                  adapter.convert_matrix_coord(end),  # position we end
                                                  space[0],  # piece
                                                  'jump move',
                                                jumped))  # type of move
                        elif space[0] == '◻':
                            moves.append(Move(adapter.convert_matrix_coord([i, j]),  # position we start
                                              adapter.convert_matrix_coord((space[1][0], space[1][1])),  # position we end
                                              space[0],  # piece
                                              'basic move'))  # type of move

                        final_moves[adapter.convert_matrix_coord([i, j])] = moves
        return final_moves

    def check_winner(self, moves):
        if self.moves_since_last_capture == 50:
            return 'draw'
        if len(moves) == 0:
            if self.cur_player.color == 'white':
                return 'black has won'
            else:
                return 'white has won'
        for move in moves:
            if moves[move] is not None:
                return False
        return 'draw'


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
                string += str(self.board[i][j]) + ' '
            final_str += (nums[i] + ' ' + string + '\n')
        final_str += '  a b c d e f g h'
        return final_str


class BoardStates:
    def __init__(self):
        pass
