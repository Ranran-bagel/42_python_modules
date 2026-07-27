#!/usr/bin/env python3
from collections.abc import Callable
from typing import Any
from functools import partial, lru_cache, reduce, singledispatch
import operator


Enchant = Callable[[int, str, str], str]


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0

    elif operation == "add":
        return reduce(operator.add, spells)

    elif operation == "multiply":
        return reduce(operator.mul, spells)

    elif operation == "max":
        return reduce(max, spells)

    elif operation == "min":
        return reduce(min, spells)

    else:
        raise ValueError(f"Unknown operation: {operation}")


def enchant(power: int, element: str, target: str) -> str:
    return f"{element} enchantment on {target} with {power} power"


def partial_enchanter(base_enchantment: Enchant) -> dict[str, partial[str]]:
    enchanters = dict()
    fire_enchanter = partial(base_enchantment, 20, "fire")
    ice_enchanter = partial(base_enchantment, 20, "ice")
    lighting_enchanter = partial(base_enchantment, 20, "lighting")
    enchanters["fire"] = fire_enchanter
    enchanters["ice"] = ice_enchanter
    enchanters["lighting"] = lighting_enchanter
    return enchanters


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n-1) + memoized_fibonacci(n-2)


def spell_dispatcher() -> Callable[[Any], str]:

    @singledispatch
    def dispatch(value: object) -> str:
        return "Unknown spell type"

    @dispatch.register
    def _(value: int) -> str:
        return f"Damage spell: {value} damage"

    @dispatch.register
    def _(value: str) -> str:
        return f"Enchantment: {value}"

    @dispatch.register
    def _(value: list[Any]) -> str:
        return f"Multi-cast: {len(value)} spells"
    return dispatch


def spell_reducer_tester() -> None:
    spells = [10, 20, 30, 40]
    print("Testing spell reducer...")
    print(f"Sum: {spell_reducer(spells, 'add')}")
    print(f"Product: {spell_reducer(spells, 'multiply')}")
    print(f"Max: {spell_reducer(spells, 'max')}")


def partial_enchanter_tester() -> None:
    enchanters = partial_enchanter(enchant)
    target = "Dragon"
    print("Testing partial enchanter...")
    print(f"Fire: {enchanters["fire"](target)}")
    print(f"Ice: {enchanters["ice"](target)}")
    print(f"Lighting: {enchanters["lighting"](target)}")


def memoized_fibonacci_tester() -> None:
    print("Testing memoized fibonacci...")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")


def spell_dispatcher_tester() -> None:
    dispatcher = spell_dispatcher()
    print("Testing spell dispatcher...")
    print(dispatcher(42))
    print(dispatcher("fireball"))
    print(dispatcher([1, 2, 3]))
    print(dispatcher(1.0))


def main() -> None:
    spell_reducer_tester()
    print()
    partial_enchanter_tester()
    print()
    memoized_fibonacci_tester()
    print()
    spell_dispatcher_tester()


if __name__ == "__main__":
    main()
