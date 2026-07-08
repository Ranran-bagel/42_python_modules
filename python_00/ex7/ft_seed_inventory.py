def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if unit not in {"packets", "grams", "area"}:
        print("Unknown unit type")
        return
    if unit == "packets":
        print(f"{seed_type.capitalize()} seeds: {quantity} {unit} available")
    elif unit == "grams":
        print(f"{seed_type.capitalize()} seeds: {quantity} {unit} total")
    else:
        print(f"{seed_type.capitalize()} seeds: "
              f"covers {quantity} square meters")
