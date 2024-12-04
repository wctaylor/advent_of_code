"""
Advent of Code 2024 Day 4

The input contains a word search (a 2D grid of characters)

Part 1
------
How many times does "XMAS" appear?

Part 2
------
"""


from collections.abc import Iterable


def _find_words(
    puzzle: list[str],
    word: str,
    directions: Iterable[tuple[tuple[int], tuple[int]]],
) -> list[tuple[int]]:
    """
    Find all occurrences of the given word,
    returning a list of the starting positions and the directions of the word

    :param puzzle: The puzzle to search
    :param word: The word to search within the puzzle
    :param directions: The set of valid directions to search in
    :returns:
        A list of tuples, where each tuple in the list contains
        one tuple for the starting postion (row, col)
        and one tuple for the direction (x, y) of the word
    """

    finds = []
    length_word = len(word)
    height = len(puzzle)
    for row, line in enumerate(puzzle):
        width = len(line)
        for col, char in enumerate(line):
            for direction in directions:
                if not (
                    (0 <= row + (length_word - 1) * direction[0] < height)
                    and (0 <= col + (length_word - 1) * direction[1] < width)
                ):
                    continue

                matched = True
                for i in range(length_word):
                    index_row = row + i * direction[0]
                    index_col = col + i * direction[1]
                    if puzzle[index_row][index_col] != word[i]:
                        matched = False
                        break
                if matched:
                    finds.append(((row, col), direction))

    return finds


def solve(puzzle: list[str], part: int | None = None) -> None:
    """
    Solve the 2024 Day 4 puzzle.

    :param puzzle: the contents of the puzzle file
    :param part: the part of the puzzle to solve. If None, solve both parts.
    """

    if part == 1 or part is None:
        directions = {
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        }
        word = "XMAS"
        finds = _find_words(puzzle, word, directions)
        print(f"The number of times {word} appears is {len(finds)}")

    if part == 2 or part is None:
        directions = {
            (-1, -1),
            (-1, 1),
            (1, -1),
            (1, 1),
        }
        word = "MAS"
        intersection = "A"
        finds = _find_words(puzzle, word, directions)

        count_cross = 0
        for i in range(len(finds)):
            intersection_row_1 = (
                finds[i][0][0] + (word.index(intersection) * finds[i][1][0])
            )
            intersection_col_1 = (
                finds[i][0][1] + (word.index(intersection) * finds[i][1][1])
            )

            for j in range(i+1, len(finds)):
                intersection_row_2 = (
                    finds[j][0][0] + (word.index(intersection) * finds[j][1][0])
                )
                intersection_col_2 = (
                    finds[j][0][1] + (word.index(intersection) * finds[j][1][1])
                )
                if (
                    intersection_row_1 == intersection_row_2
                    and intersection_col_1 == intersection_col_2
                ):
                    count_cross += 1

        print(f"The number of times X-{word} appears is {count_cross}")

