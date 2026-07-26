#!/usr/bin/env python3
from collections.abc import Callable


Counter = Callable[[], int]
Accumulator = Callable[[int], int]
Factory = Callable([str], str)
Store = Callable([])


def mage_counter() -> Counter:
    count = 0
    def counter() -> int:
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> Accumulator:
    total = initial_power
    def accumulator(amount: int) -> int:
        nonlocal total
        total += amount
        return total
    return accumulator


def enchantment_factory(enchantment_type: str) -> Factory:
    def factory(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"
    return factory


def memory_vault() -> dict[str, Callable]:
    storage = dict()
    def store(key: str, value: str) -> None:
        storage.update({key: value})
    def recall(key: str) -> str:
        return storage.get([key], "Memory not found")
    return {"store": store, "recall": recall}


def mage_counter_tester() -> None:
    counter_a = mage_counter()
    counter_b = mage_counter()
    print("Testing mage counter...")
    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    print(f"counter_b call 1: {counter_b()}")


def spell_accumulator_tester() -> None:
    base_power = 100
    accumulator = spell_accumulator(base_power)
    print("Testing spell accumulator...")
    amount1 = 20
    print(f"Base {base_power}, add {amount1}: {accumulator(amount1)}")
    amount2 = 30
    print(f"Base {base_power}, add {amount2}: {accumulator(amount2)}")


def enchantment_factory_tester() -> None:
    enchantment_types= ["Flaming", "Frozen"]
    item_names = ["Sword", "Shield"]
    print("Testing enchantment factory...")
    for enchantment_type in enchantment_types:
        factory = enchantment_factory(enchantment_type)
        for item_name in item_names:
            print(factory(item_name))


def memory_vault_tester() -> None:
    storage = memory_vault()
    print("Testing memory vault...")
    storage["store"]("secret", 42)
    print("Store 'secret' = 42")
    print(f"Recall 'secret': {storage["recall"]("secret")}")
    print(f"Recall 'unknown': {storage["recall"]("unknown")}")


def main() -> None:
    mage_counter_tester()
    print()
    spell_accumulator_tester()
    print()
    enchantment_factory_tester()
    print()
    memory_vault_tester()


if __name__ == "__main__":
    main()
