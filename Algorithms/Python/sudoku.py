"""
A sudoku generator that returns a valid solved board and a
sudoku challenge with a certain number of numbers removed.

Created: 21/02/2022
"""

from random import choice, randint

class SudokuUtils:
    """
    Represents the soduku utils that will be required
    when doing the brute force aspect of the algorithm
    """
    rows: list[list[int]]

    def set_xy(self, xy: list[int, int], value: int) -> None:
        """Sets the x and y value to value.
        :param xy: The xy coordinates.
        :param vlaue: The value to set.
        """
        y, x = xy
        self.rows[x][y] = value

    def get_xy(self, xy: list[int, int]) -> list[int]:
        """Gets the value from the square in x and y.
        :param xy: The xy coordinates to get
            the value from.
        :return: The value in the square.
        """
        y, x = xy
        return self.rows[x][y]

    def get_box(self, index: int | list[list[int]]) -> list[int]:
        """Gets the box with index `index` or from coordinates.
        :return: The box squares in list form.
        """
        board = sum(self.rows, start=[])
        boxes = {
            0: [board[i : i + 3] for i in range(0, 27, 9)],
            1: [board[i + 3 : i + 6] for i in range(0, 27, 9)],
            2: [board[i + 6 : i + 9] for i in range(0, 27, 9)],
            3: [board[i : i + 3] for i in range(27, 54, 9)],
            4: [board[i + 3 : i + 6] for i in range(27, 54, 9)],
            5: [board[i + 6 : i + 9] for i in range(27, 54, 9)],
            6: [board[i : i + 3] for i in range(54, 81, 9)],
            7: [board[i + 3 : i + 6] for i in range(54, 81, 9)],
            8: [board[i + 6 : i + 9] for i in range(54, 81, 9)],
        }

        try:
            return boxes[index]
        except TypeError:
            pass

        y, x = index

        if x in [0, 1, 2] and y in [0, 1, 2]:
            return boxes[0]
        elif x in [3, 4, 5] and y in [0, 1, 2]:
            return boxes[1]
        elif x in [6, 7, 8] and y in [0, 1, 2]:
            return boxes[2]

        if x in [0, 1, 2] and y in [3, 4, 5]:
            return boxes[3]
        elif x in [3, 4, 5] and y in [3, 4, 5]:
            return boxes[4]
        elif x in [6, 7, 8] and y in [3, 4, 5]:
            return boxes[5]

        if x in [0, 1, 2] and y in [6, 7, 8]:
            return boxes[6]
        elif x in [3, 4, 5] and y in [6, 7, 8]:
            return boxes[7]
        elif x in [6, 7, 8] and y in [6, 7, 8]:
            return boxes[8]

    def get_column(self, index: int | list[list[int]]) -> list[int]:
        """Gets the column with index `index` or from coordinates.
        :return: The columns squares in list form.
        """
        board = sum(self.rows, start=[])
        columns = [board[i::9] for i in range(9)]

        try:
            return columns[index]
        except TypeError:
            pass

        _, x = index
        return columns[x]

    def get_row(self, index: int | list[list[int]]) -> list[int]:
        """Gets the row with index `index` or from coordinates.
        :return: The rows squares in list form.
        """
        try:
            return self.rows[index]
        except TypeError:
            pass

        y, _ = index
        return self.rows[y]

    def get_possible_numbers(self, xy: list[int, int], _number_bag: list[int]) -> list[int] | None:
        """
        Gets all the possible numbers around the
        coordinates xy as to not create conflicts.
        :return: The possible number combinations or `None`
        """
        column = self.get_column(xy)
        row = self.get_row(xy)

        number_bag = _number_bag.copy()
        number_bag = self.subtract_list(number_bag, column)
        number_bag = self.subtract_list(number_bag, row)
        return number_bag

    def subtract_list(self, operand_one: list[int], operand_two: list[int]) -> list[int]:
        """Subtracts two lists.
        :param operand_one: The first list.
        :param operand_two: The second list.
        :return: The subtracted list.
        """
        for index in operand_one.copy():
            if index in operand_two:
                operand_one.remove(index)
        return operand_one
    

class SudokuGenerator(SudokuUtils):
    """
    Represents the generator class to create, solve
    and generate soduku boards.
    """

    rows: list[list[int]] = [[0 for _ in range(9)] for _ in range(9)]

    def generate_puzzle(self, difficulty: str) -> list[list[int]]:
        """Generates the puzzle.
        :param difficulty: How many numbers to remove.
        :return: The board instance that was
            created. Sorted into each box.
        """
        difficulty_ratio = {"easy": 30, "medium": 25, "hard": 20, "insane": 17}

        while True:
            board = self.build_board()
            if board:
                board_boxes = [sum(self.get_box(i), start=[]) for i in range(9)]
                numbers = difficulty_ratio[difficulty]

                for _ in range(82 - numbers):
                    x = randint(0, 8)
                    y = randint(0, 8)
                    self.set_xy([y, x], 0)
                return (board_boxes, [sum(self.get_box(i), start=[]) for i in range(9)])

    def build_box(self, index: int) -> None:
        """Builds a box.
        Sets the value of the 9 squares in a box
        while making sure there are no conflicts.
        :param index: The box index to build.
        """
        unused_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        used_numbers = []
        box_coords = {
            0: [[0, 3], [0, 3]],
            1: [[0, 3], [3, 6]],
            2: [[0, 3], [6, 9]],
            3: [[3, 6], [0, 3]],
            4: [[3, 6], [3, 6]],
            5: [[3, 6], [6, 9]],
            6: [[6, 9], [0, 3]],
            7: [[6, 9], [3, 6]],
            8: [[6, 9], [6, 9]],
        }

        for row in range(*box_coords[index][0]):
            for column in range(*box_coords[index][1]):
                xy = [row, column]

                possible_numbers = self.get_possible_numbers(xy, unused_numbers)
                if not possible_numbers:
                    return False

                number = choice(possible_numbers)
                unused_numbers.remove(number)
                used_numbers.append([[column, row], number])

        for index in used_numbers:
            self.set_xy(index[0], index[1])
        return True

    def build_board(self) -> bool:
        """Attempts to build a board.
        :return:
            `True` indiciating the build was successful.
            `False` indicating the build was unsuccessful.
        """

        for i in range(9):
            for _ in range(9):
                built = self.build_box(i)
                if built:
                    break

            if not built:
                self.rows: list[list[int]] = [[0 for _ in range(9)] for __ in range(9)]
                return False
        return True

    def print_board(self, raw: bool = False) -> None:
        """Visually prints the current board.
        Used for debugging purposes.
        :param raw: Whether or not to format the board.
        """

        if raw:
            print("\n".join([str(s) for s in self.rows]))
            return

        visual_board = ""
        for row in range(9):
            for column in range(9):
                visual_board += str(self.rows[row][column])
                if (column + 1) % 3 == 0 and 7 > column:
                    visual_board += "|"

            visual_board += "\n"
            if (row + 1) % 3 == 0 and 7 > row:
                visual_board += "-----------\n"
        print(visual_board)


if __name__ == "__main__":
    puzzle = SudokuGenerator()
    puzzle.generate_puzzle("medium")
    puzzle.print_board()

    import timeit

    print(timeit.timeit("SudokuGenerator().generate_puzzle('medium')", number=1000, globals=globals()))