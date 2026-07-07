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
        print(f"{self._name}: {self.get_height():.1f}cm,"
              f" {self.get_age()} days old")

    def age(self, time: int) -> None:
        self._age_days += time

    def grow(self, growth_rate: float) -> None:
        self._height += growth_rate

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


def main() -> None:
    print("=== Garden Security System ===")
    print("Plant created: ", end="")
    rose = Plant("Rose", 15, 10)
    rose.show()
    print()
    rose.set_height(25)
    rose.set_age(30)
    print()
    rose.set_height(-1)
    rose.set_age(-10)
    print()
    print("Current state: ", end="")
    rose.show()


if __name__ == "__main__":
    main()
