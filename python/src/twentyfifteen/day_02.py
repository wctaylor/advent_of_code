"""
Advent of Code 2015 Day 2
"""


def solve(puzzle: list[str]) -> None:
    """
    Solve the 2015 Day 2 puzzle.
    The input is a list of lines, where each line is of the form
    length x width x height, with no spaces.
    Example: 1x2x3

    Part 1
    ------
    How much total wrapping paper do the elves need?

    Part 2
    ------
    How much total ribbon do the elves need?

    :param puzzle: the contents of the puzzle file
    """

    total_paper_sqft = 0
    total_ribbon_ft = 0
    for dimensions in puzzle:
        dims = dimensions.split("x")
        if len(dims) != 3:
            raise ValueError(
                f"Found an unexpected line.\n"
                f"Expected a form of 'LxWxH', but found '{dimensions}'"
            )
        (length, width, height) = (int(x) for x in dims)
        volume = length * width * height

        # The elves need enough wrapping paper for the surface area of the
        # rectangular prism, plus the area of the smallest face
        areas_sqft = (
            length * width,
            length * height,
            width * height,
        )
        total_paper_sqft = (
            total_paper_sqft + min(areas_sqft) + 2 * sum(areas_sqft)
        )

        # The elves need enough ribbon to wrap the shortest perimeter of any
        # face, plus the volume of the prism for the bow
        perimeters_ft = (
            2 * (length + width),
            2 * (length + height),
            2 * (width + height),
        )
        total_ribbon_ft = total_ribbon_ft + min(perimeters_ft) + volume

    print(
        f"Part 1: The elves need a total of "
        f"{total_paper_sqft} square feet of wrapping paper."
    )
    print(
        f"Part 2: The elves need a total of {total_ribbon_ft} feet of ribbon."
    )
