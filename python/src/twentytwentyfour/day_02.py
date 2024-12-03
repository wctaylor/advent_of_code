"""
Advent of Code 2024 Day 2

The input contains a list of reports, where each report is a list of numbers

Part 1
------
How many reports are safe?

Part 2
------
How many reports are safe if one bad level can be removed?
"""


def _report_is_safe(report: list[int]) -> bool:
    """
    Determine whether a report is safe

    :param report: A list of numbers comprising a report
    :returns: Whether the report is safe
    """

    is_safe = True
    previous = None
    is_ascending = None
    for number in report:
        if previous is None:
            previous = number
            continue

        current = number
        difference = current - previous
        previous = current

        if not ((-3 <= difference <= -1) or (1 <= difference <= 3)):
            is_safe = False
            break

        if is_ascending is None:
            is_ascending = (difference > 0)
            continue

        if (
            (difference > 0 and not is_ascending)
            or (difference < 0 and is_ascending)
        ):
            is_safe = False
            break

    return is_safe


def solve(puzzle: list[str], part: int | None = None) -> None:
    """
    Solve the 2024 Day 2 puzzle.

    :param puzzle: the contents of the puzzle file
    :param part: the part of the puzzle to solve. If None, solve both parts.
    """

    safe_reports_1 = 0
    safe_reports_2 = 0
    for line in puzzle:
        report = [int(x) for x in line.strip().split()]
        is_safe = _report_is_safe(report)
        if is_safe:
            safe_reports_1 = safe_reports_1 + 1
            safe_reports_2 = safe_reports_2 + 1
        else:
            for i in range(0, len(report)):
                new_report = report[0:i] + report[i+1:]
                is_safe = _report_is_safe(new_report)
                if is_safe:
                    break
            if is_safe:
                safe_reports_2 = safe_reports_2 + 1

    if part == 1 or part is None:
        print(f"The number of safe reports is {safe_reports_1}")
    if part == 2 or part is None:
        print(f"The number of safe reports is {safe_reports_2}")
