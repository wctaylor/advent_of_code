"""
Advent of Code 2024 Day 5

The input contains one section for page ordering rules followed by a section
of updates with sequences of page numbers.

Part 1
------
What is the sum of the middle number in every correctly ordered update?

Part 2
------
What is the sum of the middle number of every incorrectly ordered update
after it has been correctly ordered?
"""


def solve(puzzle: list[str], part: int | None = None) -> None:
    """
    Solve the 2024 Day 5 puzzle.

    :param puzzle: the contents of the puzzle file
    :param part: the part of the puzzle to solve. If None, solve both parts.
    """

    break_ = puzzle.index("")
    rules = puzzle[0:break_]
    updates = puzzle[break_ + 1:]

    followers_by_page = {}
    for rule in rules:
        pair = rule.split("|")
        first, second = pair[0], pair[1]
        if first in followers_by_page:
            followers_by_page[first].add(second)
        else:
            followers_by_page[first] = {second}
        if second not in followers_by_page:
            followers_by_page[second] = set()

    total_1 = 0
    total_2 = 0
    for update in updates:
        pages = update.split(",")
        valid = True
        for i in range(len(pages)):
            for j in range(i + 1, len(pages)):
                if pages[j] not in followers_by_page[pages[i]]:
                    valid = False
                    break
            if not valid:
                break

        if valid:
            total_1 = total_1 + int(pages[len(pages) // 2])
        else:
            corrected = {}
            for page in pages:
                corrected[page] = []
                for follower in followers_by_page[page]:
                    if follower in pages:
                        corrected[page].append(follower)

            corrected = sorted(
                corrected.keys(),
                key=lambda page: len(corrected[page]),
                reverse=True
            )
            total_2 = total_2 + int(corrected[len(corrected) // 2])

    if part == 1 or part is None:
        print(
            f"The sum of all the middle page numbers "
            f"of correct updates is {total_1}"
        )

    if part == 2 or part is None:
        print(
            f"The sum of all the middle page numbers "
            f"of incorrect updates is {total_2}"
        )
