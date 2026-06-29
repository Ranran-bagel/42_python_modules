from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    spellbook = dark_spell_allowed_ingredients()
    lower_ingredients = ingredients.lower()
    for item in spellbook:
        if item in lower_ingredients:
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
