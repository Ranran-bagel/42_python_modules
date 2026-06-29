import alchemy.grimoire


def main() -> None:
    print("=== Kaboom 0 ===")
    print("Using grimoire module directly")
    para1 = "Fantasy"
    para2 = "Earth, wind and fire"
    testing = alchemy.grimoire.light_spell_record(para1, para2)
    print("Testing record light spell: "
          f"{testing}")


if __name__ == "__main__":
    main()
