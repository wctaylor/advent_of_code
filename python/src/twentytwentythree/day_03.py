"""
Advent of Code 2023 Day 3

The input represents an engine schematic and is essentially like a 2D grid.
Numbers appear on lines, and if a number is adjacent to any symbol character
(everything but other numbers and "." characters), it is a part number.

A gear is any * symbol that is adjacent to exactly two part numbers
(that's two part numbers, not just two numbers).
The gear ratio is the product of a gear's two part numbers.

Part 1
------
What is the sum of all the part numbers?

Part 2
------
What is the sum of all the gear ratios?
"""


def _find_gear_ratios(
    puzzle: list[str], index_row: int, part_numbers: list[dict]
) -> list[int]:
    """
    Generate the list of all gear ratios within the input window given the
    input part numbers

    :param window: The input region to search for part numbers
    :param index_window: The index of the window basis row
    :param part_numbers:
        The list of dicts containing part number values and positions
    :returns: The list of gear ratios found within the window
    """

    gear_ratios = list()
    row = puzzle[index_row]

    num_rows = len(puzzle)
    num_cols = len(row)
    for index_col, char in enumerate(row):
        if char == "*":
            neighboring_part_numbers = list()
            for part_number in part_numbers:
                part_found = False
                for i in range(-1, 2):
                    if index_row + i < 0 or index_row + i >= num_rows:
                        continue
                    for j in range(-1, 2):
                        if index_col + j < 0 or index_col + j >= num_cols:
                            continue

                        if (
                            not part_found
                            and part_number["row"] == index_row + i
                            and index_col + j in part_number["columns"]
                        ):
                            part_found = True
                            neighboring_part_numbers.append(part_number)

            if len(neighboring_part_numbers) == 2:
                gear_ratios.append(
                    neighboring_part_numbers[0]["value"]
                    * neighboring_part_numbers[1]["value"]
                )

    return gear_ratios


def _find_part_numbers(puzzle: list[str], index_row: int) -> list[dict]:
    """
    Generate the list of all part numbers within the input window

    :param puzzle: The input puzzle
    :param index_row: The row to search for part numbers
    :returns:
        A list of dictionaries, where each entry represents a part number.
        Example:
        {
            "value": 123,  # The part number
            "row": 1,  # The row index
            "columns": [1,2,3]  # The column indices within the row
        }
    """

    part_numbers = list()
    row = puzzle[index_row]

    num_rows = len(puzzle)
    num_cols = len(row)

    # Part 1: Used to build part numbers
    add_part_number = False
    part_number = ""
    # Part 2: Used to track part number locations as we go
    columns = list()
    for index_col, char in enumerate(row):
        # If we find a digit, we want to consider it for a part number
        if char.isdigit():
            # Part 1: We just need the number
            part_number = part_number + char
            # Part 2: We also need the location
            columns.append(index_col)
            for i in range(-1, 2):
                if index_row + i < 0 or index_row + i >= num_rows:
                    continue
                for j in range(-1, 2):
                    if index_col + j < 0 or index_col + j >= num_cols:
                        continue
                    neighbor = puzzle[index_row + i][index_col + j]
                    # A number is a part number if it has a neighbor
                    # that is not a digit and not a period
                    if not neighbor.isdigit() and neighbor != ".":
                        add_part_number = True

            # Handle cases where the row ends in a number
            if index_col == num_cols - 1 and add_part_number:
                # Part 1: "number" is needed
                # Part 2: "row" and "columns" are needed
                part_numbers.append(
                    {
                        "value": int(part_number),
                        "row": index_row,
                        "columns": columns,
                    }
                )

                add_part_number = False
                columns = list()
                part_number = ""

        # The character is not a digit, so we need to reset our part number
        else:
            if add_part_number:
                # Part 1: "number" is needed
                # Part 2: "row" and "columns" are needed
                part_numbers.append(
                    {
                        "value": int(part_number),
                        "row": index_row,
                        "columns": columns,
                    }
                )
            add_part_number = False
            columns = list()
            part_number = ""

    return part_numbers


def solve(puzzle: list[str], part: int | None = None) -> None:
    """
    Solve the 2023 Day 3 puzzle.

    :param puzzle: the contents of the puzzle file
    :param part: the part of the puzzle to solve. If None, solve both parts.
    """

    # Part 1
    part_numbers = []
    # Part 2
    gear_ratios = []
    for index_row, row in enumerate(puzzle):
        part_numbers.extend(_find_part_numbers(puzzle, index_row))
        gear_ratios.extend(
            _find_gear_ratios(puzzle, index_row - 1, part_numbers)
        )

    # Handle the last line for gear ratios
    gear_ratios.extend(_find_gear_ratios(puzzle, index_row, part_numbers))

    if part == 1 or part is None:
        sum_part_numbers = sum(
            part_number["value"] for part_number in part_numbers
        )
        print(f"The sum of the part numbers is {sum_part_numbers}.")
    if part == 2 or part is None:
        sum_gear_ratios = sum(gear_ratio for gear_ratio in gear_ratios)
        print(f"The sum of the gear ratios is {sum_gear_ratios}.")
