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

    total_paper = 0
    total_ribbon = 0
    for dimensions in puzzle:
        dims = dimensions.split("x")
        if len(dims) != 3:
            raise ValueError(
                f"Found an unexpected line.\n"
                f"Expected a form of 'LxWxH', but found '{dimensions}'"
            )

        length = int(dims[0])
        width = int(dims[1])
        height = int(dims[2])
        volume = length * width * height

        # The elves need enough wrapping paper for the surface area of the
        # rectangular prism, plus the area of the smallest face
        area_1 = 2 * length * width
        area_2 = 2 * length * height
        area_3 = 2 * width * height
        min_area = min([area_1, area_2, area_3])
        total_paper = total_paper + area_1 + area_2 + area_3 + min_area

        # The elves need enough ribbon to wrap the shortest perimeter of any
        # face, plus the volume of the prism for the bow
        perimeter_1 = 2 * (length + width)
        perimeter_2 = 2 * (length + height)
        perimeter_3 = 2 * (width + height)
        min_perimeter = min([perimeter_1, perimeter_2, perimeter_3])
        total_ribbon = total_ribbon + min_perimeter + volume

    print(
        f"Part 1: The elves need a total of "
        f"{total_paper} square feet of wrapping paper."
    )
    print(f"Part 2: The elves need a total of {total_ribbon} feet of ribbon.")
