# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_analytics.py                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: wezhou <wezhou@student.42tokyo.jp>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/06/08 11:09:48 by wezhou            #+#    #+#              #
#    Updated: 2026/06/16 13:12:27 by wezhou           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Plant():
    class _Stats:
        def __init__(self) -> None:
            self._grow_count: int = 0
            self._age_count: int = 0
            self._show_count: int = 0

        def display(self) -> None:
            print(f"Stats: {self._grow_count} grow, "
                  f"{self._age_count} age, "
                  f"{self._show_count} show")

    @staticmethod
    def check_year_old(age: int) -> bool:
        return age > 365

    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = height
        self._age_days = age
        self._Stats = Plant._Stats()
    
    @classmethod
    def anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)

    def show(self) -> None:
        print(f"{self._name}: {self._height:.1f}cm, {self._age_days} days old")
        self._Stats._show_count += 1

    def age(self, days: int) -> None:
        self._age_days += days
        self._Stats._age_count += 1

    def grow(self, growth_height: float) -> None:
        self._height += growth_height
        self._Stats._grow_count += 1

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age_days

    def set_height(self, height: float):
        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
            return
        self._height = height
        print(f"Height updated: {self._height:.1f}cm")

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
            return
        self._age_days = age
        print(f"Age updated: {self._age_days}days")

    def get_stats(self) -> "Plant._Stats":
        return self._Stats


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str, has_bloomed: bool) -> None:
        super().__init__(name, height, age)
        self._color = color
        self._has_bloomed = has_bloomed
        self._Stats = Flower._Stats()

    def bloom(self) -> None:
        if self._has_bloomed is True:
            return
        else:
            self._has_bloomed = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self._color}")
        if self._has_bloomed is True:
            print(f"{self._name} is blooming beautifully!")
        else:
            print(f"{self._name} has not bloomed yet")


class Tree(Plant):
    class _Stats(Plant._Stats):
        def __init__(self) -> None:
            super().__init__()
            self._shade_count: int = 0

        def display(self) -> None:
            super().display()
            print(f"{self._shade_count} shade")

    def __init__(self, name: str, height: float, age: int, trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter = trunk_diameter
        self._Stats = Tree._Stats()

    def produce_shade(self) -> None:
        print(f"Tree {self._name} now produces a shade of ", end="")
        print(f"{self._height:.1f}cm long and {self._trunk_diameter:.1f}cm wide.")
        self._Stats._shade_count += 1

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self._trunk_diameter:.1f}cm")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int, harvest_season: str, nutritional_value: int) -> None:
        super().__init__(name, height, age)
        self._harvest_season = harvest_season
        self._nutritional_value = nutritional_value

    def show(self) -> None:
        super().show()
        print(f"Harvset season: {self._harvest_season}")
        print(f"Nuritional value: {self._nutritional_value}")

    def age(self, days: int) -> None:
        super().age(days)
        self._nutritional_value += 1 * days

class Seed(Flower):
    def __init__(self, name: str, height: float, age: int, color: str, has_bloomed: bool) -> None:
        super().__init__(name, height, age, color, has_bloomed)
        self._seeds: int = 0

    def bloom(self) -> None:
        super().bloom()
        self._seeds = 42

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self._seeds}")

def display_stats(plant: Plant) -> None:
    plant.get_stats().display()

if __name__ == "__main__":
    rose = Flower("Rose", 15, 10, "red", False)
    oak = Tree("Oak", 200.0, 365, 5.0)
    sunflower = Seed("Sunflower", 110.0, 65, "yellow", False)
    unknown_plant = Plant.anonymous()
    print("=== Garden statistics ===\n"
          "=== Check year-old\n"
          f"Is 30 days more than a year? -> {Plant.check_year_old(30)}\n"
          f"Is 400 days more than a year? -> {Plant.check_year_old(400)}\n")
    print()
    print("=== Flower")
    rose.show()
    print("[statistics for Rose]")
    display_stats(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow(8.0)
    rose.bloom()
    rose.show()
    print("[statistics for Rose]")
    display_stats(rose)
    print()
    print("=== Tree")
    oak.show()
    print("[statistics for Oak]")
    display_stats(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print("[statistics for Oak]")
    display_stats(oak)
    print()
    print("=== Seed")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.age(20)
    sunflower.grow(30.0)
    sunflower.bloom()
    sunflower.show()
    print("[statistics for Sunflower]")
    display_stats(sunflower)
    print()
    print("=== Anonymous")
    unknown_plant.show()
    print("[statistics for Unknown plant]")
    display_stats(unknown_plant)
