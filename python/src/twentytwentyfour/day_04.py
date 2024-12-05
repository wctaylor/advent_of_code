"""
Advent of Code 2024 Day 4

The input contains a word search (a 2D grid of characters)

Part 1
------
How many times does "XMAS" appear?

Part 2
------
How many times does "MAS" appear in an "X" shape?
"""


from collections.abc import Iterable


class Find:
    """
    A class representing a found word in the word search
    """

    def __init__(
        self,
        word: str,
        position: tuple[int, int],
        direction: tuple[int, int],
    ) -> None:
        self.word = word
        self.position = position
        self.direction = direction


def _find_words(
    puzzle: list[str],
    word: str,
    directions: Iterable[Find],
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
            position = (row, col)
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
                    finds.append(Find(word, position, direction))

    return finds


def _get_character_point(find: Find, character: str) -> tuple[int, int]:
    """
    Get the point within the original puzzle of the specified character
    within the Find

    :param find: The Find to use
    :param character: The character of interest
    :returns:
        A (row, col) position to use within the context of the original
        puzzle
    """

    row = (
        find.position[0]
        + (find.word.index(character) * find.direction[0])
    )

    col = (
        find.position[1]
        + (find.word.index(character) * find.direction[1])
    )

    return (row, col)


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
        cross_character = "A"
        finds = _find_words(puzzle, word, directions)

        count_cross = 0
        for i in range(len(finds)):
            cross_point_1 = _get_character_point(finds[i], cross_character)
            for j in range(i+1, len(finds)):
                cross_point_2 = _get_character_point(finds[j], cross_character)
                if cross_point_1 == cross_point_2:
                    count_cross += 1

        print(f"The number of times X-{word} appears is {count_cross}")
