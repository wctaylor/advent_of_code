"""
Advent of Code 2023 Day 5

The input contains various maps of source, destination, and range.
In part 1, there is a list of seed numbers that ultimately must be mapped to
location numbers.
In part 2, the interpretation of the seed numbers is updated to generate
even more seed numbers to consider.

Part 1
------
There is a fixed list of seed numbers provided.

Part 2
------
The seed number input generates ranges of seed numbers,
so there are more seed numbers to check.

In both parts,what is the lowest location number
that corresponds to any of the initial seed numbers?
"""


def _get_destination(maps: dict, source: int, reverse=False) -> int:
    """
    Trace the source value to its final destination.

    :param maps:
        A dict containing all the mapping information for each type of map
    :param source: The starting value of the first map to check
    :param reverse:
        If true, work backwards through the maps,
        e.g. location to seed instead of seed to location.
    :returns: The final destination value for the input source
    """

    ordered_maps = [
        "seed-to-soil",
        "soil-to-fertilizer",
        "fertilizer-to-water",
        "water-to-light",
        "light-to-temperature",
        "temperature-to-humidity",
        "humidity-to-location",
    ]

    if reverse:
        ordered_maps = reversed(ordered_maps)
        source_key = "destination"
        destination_key = "source"
    else:
        source_key = "source"
        destination_key = "destination"
    for map_ in ordered_maps:
        for mini_map in maps[map_]:
            if (
                source >= mini_map[source_key]
                and source <= mini_map[source_key] + mini_map["range"]
            ):
                source = (
                    mini_map[destination_key] + source - mini_map[source_key]
                )
                break

    return source


def solve(puzzle: list[str], part: int | None = None) -> None:
    """
    Solve the 2023 Day 5 puzzle.

    :param puzzle: the contents of the puzzle file
    :param part: the part of the puzzle to solve. If None, solve both parts.
    """

    # Pull in the input data
    map_ = ""
    maps = dict()
    seeds = list()
    for line in puzzle:
        # skip blank lines
        if not line.strip():
            continue
        if line.startswith("seeds"):
            seeds = [int(seed) for seed in line.split() if seed.isdigit()]
        else:
            # We've encountered a new map region, so we add it to our maps
            if "map" in line:
                map_ = line.split()[0]
                maps[map_] = list()
            else:
                components = line.split()
                if len(components) != 3:
                    raise ValueError(
                        f"Each line should consist of "
                        f"a destination, a source, and a range.\n"
                        f"Found: {components}"
                    )
                maps[map_].append(
                    {
                        "destination": int(components[0]),
                        "source": int(components[1]),
                        "range": int(components[2]),
                    }
                )

    # Part 1: The seed values are as provided
    if part == 1 or part is None:
        location = None
        for seed in seeds:
            result = _get_destination(maps, seed)
            if location is None or location > result:
                location = result
        print(f"The smallest location value is {location}.")
    # Part 2: The seeds values actually describe ranges,
    # so have to do some extra looping.
    # It is a bit faster to just iterate through the locations and then stop
    # when we find the first one, rather than check all seed numbers.
    if part == 2 or part is None:
        if len(seeds) % 2 != 0:
            raise ValueError(
                f"The number of seed values must be even, "
                f"but found {len(seeds)}"
            )
        location = 0
        seed_found = False
        while not seed_found:
            check_seed = _get_destination(maps, location, reverse=True)
            for i in range(0, len(seeds), 2):
                seed = seeds[i]
                offset = seeds[i + 1]
                if check_seed >= seed and check_seed <= seed + offset:
                    seed_found = True
            if not seed_found:
                location = location + 1
        print(f"The smallest location value is {location}.")
