from ..potions import strength_potion
from elements import create_fire
from ..elements import create_air


def lead_to_gold() -> str:
    return (f"Recipe transmuting Lead to Gold: brew '{create_air()}'"
            f"and 'Strength potion brewed with '{strength_potion()}' and"
            f"'Water element created'' mixed with '{create_fire()}'")
