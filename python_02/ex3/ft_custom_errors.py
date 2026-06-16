# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_custom_errors.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: wezhou <wezhou@student.42tokyo.jp>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/06/16 15:33:53 by wezhou            #+#    #+#              #
#    Updated: 2026/06/16 16:29:53 by wezhou           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error") -> None:
        super().__init__(message)


def raise_plant_err(name: str) -> None:
    raise PlantError(f"The {name} plant is wilting！")


def raise_water_err() -> None:
    raise WaterError("Not enough water in the tank!")


def test_custom_errors() -> None:
    print("=== Custom Garden Errors Demo ===")
    print()
    print("Testing PlantError...")
    try:
        raise_plant_err("tomato")
    except PlantError as error:
        print(f"Caught PlantError: {error}")
    print()
    print("Testing WaterError...")
    try:
        raise_water_err()
    except WaterError as error:
        print(f"Caught WaterError: {error}")
    print()
    print("Testing catching all garden errors...")
    try:
        raise_plant_err("tomato")
    except GardenError as error:
        print(f"Caught GardenError: {error}")
    try:
        raise_water_err()
    except GardenError as error:
        print(f"Caught GardenError: {error}")
    print()
    print("All custom error types work correctly!")

if __name__ == "__main__":
    test_custom_errors()
