from src.models.Cell import Cell


class Board:
    def __init__(self, dimension):
        self._size = dimension
        self._grid = []
        for row in range(dimension):
            rows = []
            for col in range(dimension):
                cell = Cell(row, col)
                rows.append(cell)
            self._grid.append(rows)

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = value

    @property
    def grid(self):
        return self._grid

    @grid.setter
    def grid(self, value):
        self._grid = value

    def print(self):
        for row in self.grid:
            print("|", end="")
            for cell in row:
                cell.print()
            print()

