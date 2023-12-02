"""
Advent of Code 2015 Day 7

Each line is an instruction for providing a signal output to a wire

Part 1
------
What signal is ultimately provided to wire a?

Part 2
------
Reset all wires, set wire b to now be the value of wire a from part 1,
and then recalculate all wires. What signal does wire a have now?
"""

def _route_wires(wires: dict[str, str], wire: str) -> None:
    """
    Recursively iterate through all wires until everything has a set value.

    For consistency between cases where a wire hasn't been fully resolved,
    and thus has some string value (either a command or a reference to another
    wire), I leave resolved numerical values as strings, but convert them
    to integers for computations.

    :param wires: The dict mapping wire inputs and outputs
    :param wire: The wire to set within wires
    """

    if wire.lstrip("-").isdigit():
        return

    signal = wires[wire]
    components = [component.strip() for component in signal.split()]

    # This should be a direct assignment, like 1 -> a or b -> a
    if len(components) == 1:
        source = components[0]
        _route_wires(wires, source)

        if source.lstrip("-").isdigit():
            wires[wire] = source
        elif wires[source].isdigit():
            wires[wire] = wires[source]
        return

    if len(components) == 2:
        if "NOT" not in components:
            raise ValueError(
                f"Found unsupported unary operation. "
                f"The input command is: {signal}."
            )
        source = components[1]
        _route_wires(wires, source)

        if source.lstrip("-").isdigit():
            value = int(source)
        else:
            value = int(wires[source])
        wires[wire] = str(~value)
        return

    if len(components) == 3:
        if not (
            "AND" in components
            or "OR" in components
            or "LSHIFT" in components
            or "RSHIFT" in components
        ):
            raise ValueError(
                f"Found unsupported binary operation. "
                f"The input command is: {signal}."
            )
        source_1 = components[0]
        _route_wires(wires, source_1)
        source_2 = components[2]
        _route_wires(wires, source_2)

        if source_1.lstrip("-").isdigit():
            value_1 = int(source_1)
        else:
            value_1 = int(wires[source_1])
        if source_2.lstrip("-").isdigit():
            value_2 = int(source_2)
        else:
            value_2 = int(wires[source_2])

        operator = components[1]
        match operator:
            case "AND":
                wires[wire] = str(value_1 & value_2)
            case "OR":
                wires[wire] = str(value_1 | value_2)
            case "LSHIFT":
                wires[wire] = str(value_1 << value_2)
            case "RSHIFT":
                wires[wire] = str(value_1 >> value_2)
            case _:
                raise ValueError(f"Received unsupported operator: {operator}.")
        return

    else:
        raise ValueError(
            f"Reached unexpected state. Please check the command format."
            f"The input command is: {signal}."
        )


def _to_uint16(integer: int|str) -> int:
    """
    Change the representation of an integer to be an unsigned 16-bit integer

    :param integer: The integer to change to uint16
    :returns: The uint16 representation of the input integer
    """

    if not isinstance(integer, int) and not isinstance(integer, str):
        raise ValueError(
            f"Cannot meaningfully cast data of type {type(integer)} "
            f"to uint16."
        )

    value = int(integer)
    if value < 0:
        value = 2**16 - value
    return value


def solve(puzzle: list[str], part: int | None = None) -> None:
    """
    Solve the 2015 Day 7 puzzle.

    :param puzzle: the contents of the puzzle file
    :param part: the part of the puzzle to solve. If None, solve both parts.
    """

    wires_1 = dict()
    wires_2 = dict()
    for line in puzzle:
        components = [component.strip() for component in line.split("->")]
        if len(components) != 2:
            raise ValueError(
                f"Found an unexpected instruction. The instruction is: {line}"
            )
        wires_1[components[1]] = components[0]
        wires_2[components[1]] = components[0]

    # Both parts require solving part 1
    _route_wires(wires_1, "a")
    value = _to_uint16(wires_1["a"])
    if part == 1 or part is None:
        print(f"Part 1: The value of wire 'a' is: {value}.")

    if part == 2 or part is None:
        wires_2["b"] = wires_1["a"]
        _route_wires(wires_2, "a")
        value = _to_uint16(wires_2["a"])
        print(f"Part 2: The value of wire 'a' is now: {value}.")
