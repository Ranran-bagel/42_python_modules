import typing
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex1 import HealCapability, TransformCapability


def test_healing_creatures() -> None:
    healing_factory = HealingCreatureFactory()
    healing_base = healing_factory.create_base()
    healing_evolved = healing_factory.create_evolved()
    base_healer = typing.cast(HealCapability, healing_base)
    evolved_healer = typing.cast(HealCapability, healing_evolved)
    print("Testing Creature with healing capability")
    print("base:")
    print(healing_base.describe())
    print(healing_base.attack())
    print(base_healer.heal())
    print("evolved:")
    print(healing_evolved.describe())
    print(healing_evolved.attack())
    print(evolved_healer.heal("itself and others"))


def test_transform_creatures() -> None:
    transform_factory = TransformCreatureFactory()
    transform_base = transform_factory.create_base()
    transform_evolved = transform_factory.create_evolved()
    base_transformer = typing.cast(TransformCapability, transform_base)
    evolved_transformer = typing.cast(TransformCapability, transform_evolved)
    print("Testing Creature with transform capability")
    print("base:")
    print(transform_base.describe())
    print(transform_base.attack())
    print(base_transformer.transform())
    print(transform_base.attack())
    print(base_transformer.revert())
    print("evolved:")
    print(transform_evolved.describe())
    print(transform_evolved.attack())
    print(evolved_transformer.transform())
    print(transform_evolved.attack())
    print(evolved_transformer.revert())


def main() -> None:
    test_healing_creatures()
    print()
    test_transform_creatures()


if __name__ == "__main__":
    main()
