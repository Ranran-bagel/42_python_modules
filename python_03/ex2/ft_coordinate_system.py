import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        text = input("Enter new coordinates as floats in format 'x,y,z': ")

        try:
            x_text, y_text, z_text = text.split(",")
        except ValueError:
            print("Invalid syntax")
            continue
        try:
            x = float(x_text)
        except ValueError as error:
            print(f"Error on parameter '{x_text}': {error}")
            continue
        try:
            y = float(y_text)
        except ValueError as error:
            print(f"Error on parameter '{y_text}': {error}")
            continue
        try:
            z = float(z_text)
        except ValueError as error:
            print(f"Error on parameter '{z_text}': {error}")
            continue
        return (x, y, z)


def main() -> None:
    print("=== Game Coordinate System ===")
    print()
    print("Get a first set of coordinates")
    first = get_player_pos()
    x1, y1, z1 = first
    print(f"Got a first tuple: {first}")
    print(f"It includes: X={x1}, Y={y1}, Z={z1}")
    distance = math.sqrt(x1 ** 2 + y1 ** 2 + z1 ** 2)
    print(f"Distance to center: {round(distance, 4)}")
    print()
    print("Get a second set of coordinates")
    second = get_player_pos()
    x2, y2, z2 = second
    distance = math.sqrt(
        (x2 - x1) ** 2
        + (y2 - y1) ** 2
        + (z2 - z1) ** 2
    )
    print(f"Distance between the 2 sets of coordinates: {round(distance, 4)}")


if __name__ == "__main__":
    main()
