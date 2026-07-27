#!/usr/bin/env python3
from collections.abc import Callable
from functools import wraps
import time


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper() -> None:
        print(f"Casting {func.__name__}...")
        time_before = time.time()
        func()
        cost_time = time.time() - time_before
        print(f"Spell completed in {cost_time:.3f} seconds")

    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: object, **kwargs: object) -> None:
            power = kwargs.get("power")
            if power is None:
                power = args[-1]
            if power > min_power:
                func()
            else:
                return "Insufficient power for this spell"
        return wrapper

    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: object, **kwargs: object) -> object:
            last_error: Exception | None = None
            for _ in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as exc:
                    last_error = exc
            if last_error is not None:
                raise last_error
            return None

        return wrapper

    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return bool(name and name.isalpha() and name[0].isupper())

    def cast_spell(self, spell_name: str, power: int) -> str:
        if not self.validate_mage_name(spell_name):
            raise ValueError("Invalid spell name")
        return f"{spell_name} cast with power {power}"
