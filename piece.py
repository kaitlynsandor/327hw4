class Piece:
    def __init__(self, symbol, color='white',  is_king=False, position=False,):
        self.symbol = symbol # this is the actual board sympol
        if self.symbol == '⚈' or self.symbol == '⚉':  # set the color
            self.color = 'black'
        else:
            self.color = color
        self.is_king = is_king

    def update_king(self, boolean):
        self.is_king = boolean
        if self.color == 'white':
            self.symbol = '⚇'
        else:
            self.symbol = '⚉'

    def spaces_to_check(self, i, j, board): # spaces to check to see if there is an available move, if black checking down the board, if white up the board, if king in both directions
        spaces_to_check = []
        print(self.is_king, i, j, self.color)
        if self.color == 'black' or self.is_king:
            if i < len(board) - 1:
                if j > 0:
                    spaces_to_check.append([board[i + 1][j - 1], [i + 1, j - 1]])
                if j < len(board[0]) - 1:
                    spaces_to_check.append([board[i + 1][j + 1], [i + 1, j + 1]])
        if self.color == 'white' or self.is_king:  # if the piece is white
            if i > 0:
                if j > 0:
                    spaces_to_check.append([board[i - 1][j - 1], [i - 1, j - 1]])
                if j < len(board[0]) - 1:
                    spaces_to_check.append([board[i - 1][j + 1], [i - 1, j + 1]])
        return spaces_to_check

    def __repr__(self):
        return self.symbol # print out the symbol associated with this piece

