class Move_Adapter:

    def convert_checker_coord(coord):
        col = coord[:1]
        row = coord[1:]
        col = ord(col) - 96
        row = int(row)
        return (row - 1, col - 1)

    def convert_matrix_coord(coord):
        row, col = coord
        return chr(col + 96 + 1) + str(row + 1)
