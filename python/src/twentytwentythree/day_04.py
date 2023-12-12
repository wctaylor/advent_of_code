"""
Advent of Code 2023 Day 4

The input represents a set of scratchcards.
Each line contains the winning numbers for a card
and the numbers obtained on the card, separated by a | character.

Part 1
------
The first winning number on a card is worth one point,
and every subsequent winning number on the card doubles the points.

What is the total number of points from all cards?

Part 2
------
If a card has N winning numbers, then the next N cards are copied.
Each of those copied cards can subsequently generate additional copies.

What is the total number of cards?
"""


def solve(puzzle: list[str], part: int | None = None) -> None:
    """
    Solve the 2023 Day 4 puzzle.

    :param puzzle: the contents of the puzzle file
    :param part: the part of the puzzle to solve. If None, solve both parts.
    """

    # Part 1
    total_score = 0
    # Part 2
    scratchcards = dict()
    for card in puzzle:
        components = card.split(":")

        # Part 1
        number_groups = components[1].split("|")
        winning_numbers = number_groups[0].strip().split()
        found_numbers = number_groups[1].strip().split()

        num_found = 0
        for number in found_numbers:
            if number in winning_numbers:
                num_found = num_found + 1
        if num_found == 0:
            score = 0
        else:
            score = 2 ** (num_found - 1)
        total_score = total_score + score

        # Part 2
        card_id = int(components[0].split()[1])

        # Add the originals
        if card_id in scratchcards:
            scratchcards[card_id] = scratchcards[card_id] + 1
        else:
            scratchcards[card_id] = 1

        # Add the copies
        for i in range(num_found):
            copy_id = card_id + i + 1
            # Each copy of the card_id card adds a copy of the copy_id card
            if copy_id in scratchcards:
                scratchcards[copy_id] = (
                    scratchcards[copy_id] + scratchcards[card_id]
                )
            else:
                scratchcards[copy_id] = scratchcards[card_id]

    if part == 1 or part is None:
        print(f"The total score of the cards is {total_score}.")
    if part == 2 or part is None:
        print(
            f"The total number cards is "
            f"{sum(value for value in scratchcards.values())}."
        )
