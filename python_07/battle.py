from ex0 import CreatureFactory, FlameFactory, AquaFactory


def test_factory(factory: CreatureFactory) -> None:
    base_creature = factory.create_base()
    evolved_creature = factory.create_evolved()
    print(base_creature.describe())
    print(base_creature.attack())
    print()
    print(evolved_creature.describe())
    print(evolved_creature.attack())


def test_battle(factory1: CreatureFactory, factory2: CreatureFactory) -> None:
    creature1 = factory1.create_base()
    creature2 = factory2.create_base()
    print(creature1.describe())
    print("vs.")
    print(creature2.describe())
    print(creature1.attack())
    print(creature2.attack())


def main() -> None:
    print("Testing factory")
    test_factory(FlameFactory())
    print()
    print("Testing factory")
    test_factory(AquaFactory())
    print()
    print("Testing battle")
    test_battle(FlameFactory(), AquaFactory())


if __name__ == "__main__":
    main()
