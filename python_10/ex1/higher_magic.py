from collections.abc import Callable


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} HP"


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"

def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(target: str, power: int) -> tuple(str, str):
        return (spell1(target, power), spell2(target, power))
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def new_spell(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return new_spell

def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def condition(target: str, power: int) -> str:
        if condition:
            return spell(target, power)
        return "Spell fizzled"
    return condition

def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence(target: str, power: int) -> list[str]:
        res = list()
        for spell in spells:
            res.append(spell(target, power))
        return res
    return sequence

