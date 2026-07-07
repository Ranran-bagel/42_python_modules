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
    oak = Plant("Oak", 200, 365)
    cactus = Plant("Cactus", 5, 90)
    sunflower = Plant("Sunflower", 80, 45)
    fern = Plant("Fern", 15, 120)
    plant_list = [rose, oak, cactus, sunflower, fern]
    print("=== Plant Factory Output ===")
    for plant in plant_list:
        print("Created: ", end="")
        plant.show()


if __name__ == "__main__":
    main()
