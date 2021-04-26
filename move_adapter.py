class Move_Adapter: # copied straight from his assignment descriptoins, to convert between like b6 and the coordinates (1,5)

    def convert_checker_coord(self, coord):
        col = coord[:1]
        row = coord[1:]
        col = ord(col) - 96
        row = int(row)
        return (row - 1, col - 1)

    def convert_matrix_coord(self, coord):
        row, col = coord
        return chr(col + 96 + 1) + str(row + 1)
