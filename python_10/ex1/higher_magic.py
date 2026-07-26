#!/usr/bin/env python3
from collections.abc import Callable


Spell = Callable[[str, int], str]
Condition = Callable[[str, int], bool]
CombinedSpell = Callable[[str, int], tuple[str, str]]
SequenceSpell = Callable[[str, int], list[str]]


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} HP"


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def spell_combiner(spell1: Spell, spell2: Spell) -> CombinedSpell:
    def combined(target: str, power: int) -> tuple[str, str]:
        res1 = spell1(target, power)
        res2 = spell2(target, power)
        return (res1, res2)
    return combined


def power_amplifier(base_spell: Spell, multiplier: int) -> Spell:
    def amplifier(target: str, power: int) -> str:
        new_spell = base_spell(target, power * multiplier)
        return new_spell
    return amplifier


def condition(_target: str, power: int) -> bool:
    if power > 15:
        return True
    return False


def conditional_caster(condition: Condition, spell: Spell) -> Spell:
    def conditional(target: str, power: int) -> str:
        if condition(target, power):
            res = spell(target, power)
            return res
        return "Spell fizzled"
    return conditional


def spell_sequence(spells: list[Spell]) -> SequenceSpell:
    def sequence(target: str, power: int) -> list[str]:
        res = list()
        for spell in spells:
            res.append(spell(target, power))
        return res
    return sequence


def spell_combiner_tester(target: str, power: int) -> None:
    combined = spell_combiner(fireball, heal)
    res = combined(target, power)
    print("Testing spell combiner...")
    print(f"Combined spell result: {res[0]}, {res[1]}")


def power_amplifier_tester(target: str, power: int) -> None:
    multiplier = 3
    amplifier = power_amplifier(fireball, multiplier)
    res_before = fireball(target, power)
    res_after = amplifier(target, power)
    print("Testing power amplifier...")
    print(f"Original: {power}, Amplified: {power * multiplier}")
    print(f"Original spell result: {res_before}")
    print(f"Amplified spell result: {res_after}")


def conditional_caster_tester() -> None:
    conditional = conditional_caster(condition, fireball)
    print("Testing conditional_caster...")
    print("if condition is True:")
    res1 = conditional("Dragon", 20)
    print(f"{res1}")
    print("if condition is False:")
    res2 = conditional("Dragon", 10)
    print(f"{res2}")


def spell_sequence_tester(
        spells: list[Spell],
        target: str,
        power: int) -> None:
    sequence = spell_sequence(spells)
    res = sequence(target, power)
    print("Testing spell_sequence...")
    for spell in res:
        print(spell)


def main() -> None:
    target = "Dragon"
    power = 10
    spell_combiner_tester(target, power)
    print()
    power_amplifier_tester(target, power)
    print()
    conditional_caster_tester()
    print()
    spell_sequence_tester([fireball, heal], target, power)


if __name__ == "__main__":
    main()
