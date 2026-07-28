#!/usr/bin/env python3
from collections.abc import Callable
from functools import wraps
import time
from typing import ParamSpec, TypeVar


P = ParamSpec("P")
R = TypeVar("R")


def spell_timer(func: Callable[P, R]) -> Callable[P, R]:
    @wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        print(f"Casting {func.__name__}...")
        time_before = time.time()
        result = func(*args, **kwargs)
        cost_time = time.time() - time_before
        print(f"Spell completed in {cost_time:.3f} seconds")

        return result

    return wrapper


@spell_timer
def fireball() -> str:
    time.sleep(0.1)
    return "Fireball cast!"


def power_validator(
    min_power: int
    ) -> Callable[
        [Callable[P, str]],
        Callable[P, str]
        ]:
    def decorator(func: Callable[P, str]) -> Callable[P, str]:
        @wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> str:
            power: object | None = kwargs.get("power")
            if power is None:
                if not args:
                    raise TypeError("Power argument is missing")
                power = args[-1]
            if not isinstance(power, int):
                raise TypeError("Power must be int")
            if power < min_power:
                return "Insufficient power for this spell"

            return func(*args, **kwargs)

        return wrapper

    return decorator


def retry_spell(max_attempts: int,) -> Callable[
                                        [Callable[P, str]],
                                        Callable[P, str],
                                        ]:
    def decorator(func: Callable[P, str]) -> Callable[P, str]:
        @wraps(func)
        def wrapper(
            *args: P.args,
            **kwargs: P.kwargs,
        ) -> str:
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)

                except Exception:
                    if attempt < max_attempts:
                        print(
                            "Spell failed, retrying... "
                            f"(attempt {attempt}/{max_attempts})"
                        )

            return (
                "Spell casting failed after "
                f"{max_attempts} attempts"
            )

        return wrapper

    return decorator


@retry_spell(1)
def retry_func_success() -> str:
    return "Waaaaaaagh spelled!"


def retry_func_failure() -> Callable[[], str]:
    times = 1

    @retry_spell(3)
    def func() -> str:
        nonlocal times
        if times <= 3:
            times += 1
            raise RuntimeError("Spell casting failed")

        return "Waaaaaaagh spelled!"

    return func


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return bool(
            name
            and len(name) >= 3
            and all(
                    character.isalpha() or character == " "
                    for character in name
                    )
                )

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return (
            f"Successfully cast {spell_name} "
            f"with {power} power"
        )


def spell_timer_tester() -> None:
    print("Testing spell timer...")
    print(f"Result: {fireball()}")


def retry_spell_tester() -> None:
    print("Testing retrying spell...")

    runner = retry_func_failure()
    print(runner())
    print(retry_func_success())


def mage_guild_tester() -> None:
    print("Testing MageGuild...")

    mage_guild = MageGuild()

    print(mage_guild.validate_mage_name("Alice"))
    print(mage_guild.validate_mage_name("al"))
    print(mage_guild.cast_spell("Alice", 15))
    print(mage_guild.cast_spell("Alice", 5))


def main() -> None:
    spell_timer_tester()
    print()
    retry_spell_tester()
    print()
    mage_guild_tester()


if __name__ == "__main__":
    main()
