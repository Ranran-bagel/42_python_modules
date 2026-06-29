def validate_ingredients(ingredients: str) -> str:
    from .light_spellbook import light_spell_allowed_ingredients
    spellbook = light_spell_allowed_ingredients()
    lower_ingredients = ingredients.lower()
    for item in spellbook:
        if item in lower_ingredients:
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
