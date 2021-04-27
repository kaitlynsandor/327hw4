from move_adapter import *
from piece import *
from player import *

class Move:

    def __init__(self, start, end, piece, type, jumps=None):
        self.type = type # is this a jump move or a basic move?
        self.piece = piece # the piece object associated with this move
        self.start = start # starting position
        self.jumps = jumps # pieces that are jumped in this move
        self.end = end # ending location of this move

    def __repr__(self): # basic print out of the move
        final_str = self.type + ': ' + self.start + '->' + self.end
        if self.type == 'jump move':
            jumps = '['
            for jump in self.jumps:
                jumps+=(jump+', ')
            jumps = jumps[:-2]
            jumps += ']'
            final_str += ', capturing ' + jumps
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


    def available_moves_piece(self, move_piece, moves): # this checks all of the moves available from available_moves_all to see if the piece can be moved
        pieces = moves.keys()
        adapter = Move_Adapter()
        coordinates_of_piece = adapter.convert_checker_coord(move_piece)
        board_item = self.board[int(coordinates_of_piece[0])][int(coordinates_of_piece[1])]
        if type(board_item) != Piece:
            return 'no piece'
        elif board_item.color != self.cur_player.color:
            return 'wrong piece'
        elif move_piece not in pieces or moves[move_piece] == []: # if there are no moves associated with this piece, cant move it
            return 'no move'
        else:
            for move in moves[move_piece]: # if the piece is a jump piece we can automatically use it
                if move.type == 'jump move':
                    return moves[move_piece]
            else:
                for piece in pieces: # if piece is not a jump move, we can only use it if there are no other jump moves
                    for move in moves[piece]:
                        if move.type == 'jump move':
                            return 'no move'
                return moves[move_piece]

    def available_moves_all(self): # this function does not yet support kings jumping in all directions
        final_moves = {}
        adapter = Move_Adapter()
        for i in range(0, len(self.board)): # for every space on the board
            for j in range(0, len(self.board[i])):
                moves = []
                piece = self.board[i][j] # get the piece at the current space
                if type(piece) == Piece and piece.color == self.cur_player.color: #if the piece is a moveable piece that belongs to the current player
                    spaces_to_check = piece.spaces_to_check(i, j, self.board) # get all of the spaces we want to check
                    for space in spaces_to_check: # for each space to check
                        if type(space[0]) == Piece and space[0].color != self.cur_player.color: # if we can jump this piece
                            row_dir = space[1][0] - i # get the direction our space is in (ex. up and to the left)
                            col_dir = space[1][1] - j
                            if str(self.board[i + 2*row_dir][j + 2*col_dir]) == '◻': # check for double jumps
                                jumped = [adapter.convert_matrix_coord([space[1][0], space[1][1]])]
                                end = [i + 2*row_dir, j + 2*col_dir]

                                # k = i + 3 * row_dir
                                # l = j + 3 * col_dir
                                # while k < len(self.board) and j < len(self.board[0]) and type(self.board[k][l]) == Piece \
                                #         and self.board[k][l].color == space[0].color: # while we have empty spaces, just keep appending them
                                #     if 0 <= k + row_dir <= len(self.board) and 0 <= l + col_dir <= \
                                #             len(self.board[0]):
                                #         if self.board[k + row_dir][l + col_dir] == '◻':
                                #             jumped.append([adapter.convert_matrix_coord([k, l])])
                                #             end = adapter.convert_matrix_coord([k + row_dir, l + col_dir])
                                #         k = k + row_dir
                                #         l = l + col_dir # at the end (nexct line) append all of the spaces we jumped, the start and end point

                                moves.append(Move(adapter.convert_matrix_coord([i, j]),  # position we start
                                                  adapter.convert_matrix_coord(end),  # position we end
                                                  piece,  # piece
                                                  'jump move',
                                                jumped))  # type of move
                        elif space[0] == '◻': # otherwise if there is not a jump but the space to check is empty, we can move to that space so add that move
                            moves.append(Move(adapter.convert_matrix_coord([i, j]),  # position we start
                                              adapter.convert_matrix_coord((space[1][0], space[1][1])),  # position we end
                                              piece,  # piece
                                              'basic move'))  # type of move

                        final_moves[adapter.convert_matrix_coord([i, j])] = moves # moves at each location we checked is equal to all the moves we found
        return final_moves # return all of the possible moves we found

    def check_winner(self, moves):
        if self.moves_since_last_capture == 50: # if there have been more than 50 turns without a caputure, its a draw
            return 'draw'
        if len(moves) == 0: # if the current player cannot move, the other player wins
            if self.cur_player.color == 'white':
                return 'black has won'
            else:
                return 'white has won'
        for move in moves: # if we have moves in our moves list but each of them is empty, we have a draw
            if moves[move] is not None: # if the move isnt empty, there is a move we can make and we return false
                return False
        return 'draw'

    def make_move(self, moves, choice=None, piece=None): # calls the player move function to get the best move
        adapter = Move_Adapter()
        if type(self.cur_player) != HumanPlayer:
            move = self.cur_player.next_move(moves) # just get the move from the AI
        else:
            move = moves[piece][int(choice)] # otherwise read it from the all moves array at their specified choice, choice is the move associated with the piece
        end_pos = adapter.convert_checker_coord(move.end) # get the end position in coordinates
        start_pos = adapter.convert_checker_coord(move.start) # get the start position in coordinates
        if end_pos[1] == '1' and move.piece.color == 'white':
            move.piece.update_king(True)
        elif end_pos[1] == '8' and move.piece.color == 'black':
            move.piece.update_king(True)

        self.board[int(end_pos[0])][int(end_pos[1])] = (move.piece) # move the piece
        self.board[int(start_pos[0])][int(start_pos[1])] = '◻' # set the beginning space to be empty

        if move.type == 'jump move': # if there is a jump move, remove all of the pieces we "jumped"
            for jump in move.jumps:
                coord = adapter.convert_checker_coord(jump)
                self.board[int(coord[0])][int(coord[1])] = '◻' # set the piece to be empty if we jumped it
            self.moves_since_last_capture = 0 # update moves since last capture to show that we have captured
        else:
            self.moves_since_last_capture += 1 # but if there were no jumps update to reflect that
        return self.board # return the new board

    def update_cur_player(self):
        self.cur_player = self.settings[(self.move + 1) % 2] # flop between the two platers

    def update_move(self):
        self.move += 1 # this is the number of turns we have been through so far

    def __repr__(self): # print out the board
        nums = [str(x) for x in range(1, 9)]
        final_str = ''

        for i in range(0, 8):
            string = ''
            for j in range(0,8):
                string += str(self.board[i][j]) + ' '
            final_str += (nums[i] + ' ' + string + '\n')
        final_str += '  a b c d e f g h'
        return final_str

