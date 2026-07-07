class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = 0.0
        self._age_days = 0
        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
        else:
            self._height = height
        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
        else:
            self._age_days = age

    def show(self) -> None:
        print(f"{self._name}: {self._height:.1f}cm,"
              f" {self._age_days} days old")

    def age(self, time: int) -> None:
        self._age_days += time

    def grow(self, growth_rate: float, days: int) -> None:
        for _ in range(days):
            self._height += growth_rate
            self.age(1)

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age_days

    def set_height(self, height: float) -> None:
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
        print(f"Age updated: {self._age_days} days")


class Flower(Plant):
    def __init__(self, name: str,
                 height: float, age: int,
                 color: str, has_bloomed: bool) -> None:
        super().__init__(name, height, age)
        self._color = color
        self._has_bloomed = has_bloomed

    def bloom(self) -> None:
        self._has_bloomed = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self._color}")
        if self._has_bloomed:
            print(f"{self._name} is blooming beautifully!")
        else:
            print(f"{self._name} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name: str,
                 height: float, age: int, trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(f"Tree {self._name} now produces a shade of ", end="")
        print(f"{self._height:.1f}cm "
              f"long and {self._trunk_diameter:.1f}cm wide.")

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self._trunk_diameter:.1f}cm")


class Vegetable(Plant):
    def __init__(self, name: str,
                 height: float, age: int,
                 harvest_season: str, nutritional_value: int) -> None:
        super().__init__(name, height, age)
        self._harvest_season = harvest_season
        self._nutritional_value = nutritional_value

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self._harvest_season}")
        print(f"Nutritional value: {self._nutritional_value}")

    def age(self, days: int) -> None:
        super().age(days)
        self._nutritional_value += days


def main() -> None:
    rose = Flower("Rose", 15.0, 10, "red", False)
    oak = Tree("Oak", 200.0, 365, 5)
    tomato = Vegetable("Tomato", 5.0, 10, "April", 0)
    print("=== Garden Plant Types ===")
    print("=== Flower")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()
    print()
    print("=== Tree")
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print()
    print("=== Vegetable")
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    tomato.grow(2.1, 20)
    tomato.show()


if __name__ == "__main__":
    main()
