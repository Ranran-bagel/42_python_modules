from .light_validator import validate_ingredients


def light_spell_allowed_ingredients() -> list[str]:
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    check_ingredients = validate_ingredients(ingredients)
    if "VALID" in check_ingredients:
        return (f"Spell recorded: {spell_name} {check_ingredients}")
    else:
        return (f"Spell rejected: {spell_name} {check_ingredients}")
