class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age_days = age

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.age_days} days old")

    def age(self, time: int) -> None:
        self.age_days += time

    def grow(self, growth_rate: float) -> None:
        self.height += growth_rate


def main() -> None:
    rose = Plant("Rose", 25, 30)
    print("=== Garden Plant Growth ===")
    rose.show()
    growth_rate = 0.8
    start_height = rose.height
    for i in range(1, 8):
        print(f"=== Day {i} ===")
        rose.grow(growth_rate)
        rose.age(1)
        rose.show()
    final_height = rose.height
    print(f"Growth this week: {round(final_height - start_height, 1)}cm")


if __name__ == "__main__":
    main()
