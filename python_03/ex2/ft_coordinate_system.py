import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        text = input("Enter new coordinates as floats in format 'x,y,z': ")
        result = text.split(",")
        if len(result) != 3:
            print("Invalid syntax")
            continue
        try:
            x = float(result[0])
        except ValueError as error:
            print(f"Error on parameter '{result[0]}': {error}")
            continue
        try:
            y = float(result[1])
        except ValueError as error:
            print(f"Error on parameter '{result[1]}': {error}")
            continue
        try:
            z = float(result[2])
        except ValueError as error:
            print(f"Error on parameter '{result[2]}': {error}")
            continue
        return (x, y, z)


def  main() -> None:
    print("=== Game Coordinate System ===")
    print()
    print("Get a first set of coordinates")
    first = get_player_pos()
    x1 = first[0]
    y1 = first[1]
    z1 = first[2]
    print(f"Got a first tuple: {first}")
    print(f"It includes: X={x1}, Y={y1}, Z={z1}")
    distance = math.sqrt(x1 ** 2 + y1 ** 2 + z1 ** 2)
    print(f"Distance to center: {round(distance, 4)}")
    print()
    print("Get a second set of coordinates")
    second = get_player_pos()
    x2 = second[0]
    y2 = second[1]
    z2 = second[2]
    print(f"Got a second tuple: {second}")
    print(f"It includes: X={x2}, Y={y2}, Z={z2}")
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)
    print(f"Distance between the 2 sets of coordinates: {round(distance, 4)}")


if __name__ == "__main__":
    main()
