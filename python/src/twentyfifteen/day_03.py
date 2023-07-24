"""
Advent of Code 2015 Day 3
"""


def update_coordinates(char: str, coords: tuple[int, int]) -> int:
    """
    Update the provided coordinate based on the input character
    
    :param char: The instruction character
    :param coord: The coordinates to update
    :returns: The updated coordinate
    """
    
    valid_chars = {"<", ">", "v", "^"}
    if char not in valid_chars:
        raise ValueError(
            f"Received a character that is not a valid instruction."
            f"The character should be one of {valid_chars}, not {char}")

    if len(coords) != 2:
        raise ValueError(
            f"Received unexpected coordinates.\n"
            f"The coordinates should be a tuple of (x, y), "
            f"but received {coords}"
        )
    if char == "<":
        return (coords[0] - 1, coords[1])
    elif char == ">":
        return (coords[0] + 1, coords[1])
    elif char == "v":
        return (coords[0], coords[1] - 1)
    elif char == "^":
        return (coords[0], coords[1] + 1)


def part_1(chars: str) -> int:
    """
    Solve part 1, where the full instructions are read by Santa alone
    
    :param chars: The input string of instruction characters
    :returns: The number of houses which receive at least one gift
    """
    
    coord = (0, 0)
    # The starting house receives a gift
    houses = 1
    coordinates = [coord]
    for char in chars:
        coord = update_coordinates(char, coord)
        if coord not in coordinates:
            houses = houses + 1
            coordinates.append(coord)
    
    return houses


def part_2(chars: str) -> int:
    """
    Solve part 2, where the instructions are shared by Santa and Robo-Santa,
    each taking turns reading the movement instruction
    
    :param chars: The input string of instruction characters
    :returns: The number of houses which receive at least one gift
    """
    
    coord_santa = (0, 0)
    coord_robo = (0, 0)
    # The starting house receives a gift
    houses = 1
    coordinates = [(0, 0)]
    for char_num, char in enumerate(chars):
        if char_num % 2:
            coord_robo = update_coordinates(char, coord_robo)
            if coord_robo not in coordinates:
                houses = houses + 1
                coordinates.append(coord_robo)
        else:
            coord_santa = update_coordinates(char, coord_santa)
            if coord_santa not in coordinates:
                houses = houses + 1
                coordinates.append(coord_santa)

    return houses

def solve(puzzle: list[str]) -> None:
    """
    Solve the 2015 Day 3 puzzle.
    The input is a list of characters, where each character is one of
    "<", ">", "v", or "^", and each corresponds to the direction Santa
    (or Robo-Santa) moves in a 2D grid.

    Part 1
    ------
    How many houses receive at least one present?

    Part 2
    ------
    How many houses receive at least one present, when the instructions are
    split among Santa and Robo-Santa?

    :param puzzle: the contents of the puzzle file
    """
    
    if len(puzzle) > 1:
        raise ValueError(
            f"Unexpected puzzle length: expected a length of 1, "
            f"but found {len(puzzle)}."
        )
        
    chars = puzzle[0]
    houses_solo = part_1(chars)
    houses_team = part_2(chars)
                
    print(f"Part 1: Santa delivers gifts to a total of {houses_solo} houses.")
    print(
        f"Part 2: Santa and Robo-Santa deliver gifts "
        f"to a total of {houses_team} houses."
    )
