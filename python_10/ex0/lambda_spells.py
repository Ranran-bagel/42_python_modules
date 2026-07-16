#!/usr/bin/env python3
def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda item: item["power"], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    res = list(filter(lambda mage: mage["power"] >= min_power, mages))
    return res


def spell_transformer(spells: list[str]) -> list[str]:
    transformer = map(lambda n: f"* {n} *", spells)
    return list(transformer)


def mage_stats(mages: list[dict]) -> dict:
    powers = list(map(lambda m: m["power"], mages))
    return {
        "max_power": max(powers),
        "min_power": min(powers),
        "avg_power": round(sum(powers) / len(powers), 2),
    }


def main() -> None:
    artifacts = [{'name': 'Fire Staff', 'power': 101, 'type': 'focus'},
                 {'name': 'Fire Staff', 'power': 62, 'type': 'relic'},
                 {'name': 'Fire Staff', 'power': 116, 'type': 'armor'},
                 {'name': 'Water Chalice', 'power': 86, 'type': 'focus'}]
    mages = [{'name': 'Kai', 'power': 99, 'element': 'lightning'},
             {'name': 'Casey', 'power': 66, 'element': 'shadow'},
             {'name': 'Nova', 'power': 97, 'element': 'shadow'},
             {'name': 'Riley', 'power': 71, 'element': 'wind'},
             {'name': 'Ash', 'power': 95, 'element': 'earth'}]
    spells = ['earthquake', 'heal', 'meteor', 'lightning']
    print("Testing artifact sorter...")
    sorted_artifacts = artifact_sorter(artifacts)
    print(f"{sorted_artifacts[0]['name']} "
          f"({sorted_artifacts[0]['power']} power) "
          f"comes before {sorted_artifacts[1]['name']}"
          f" ({sorted_artifacts[1]['power']} power)")
    print()
    print("Testing spell transformer...")
    print(" ".join(spell_transformer(spells)))
    filtered = power_filter(mages, 50)
    print("Testing power filter...")
    print(f"Mages with power >= 50: {[m['name'] for m in filtered]}")
    print()
    print("Testing mage stats...")
    stats = mage_stats(mages)
    print(stats)


if __name__ == "__main__":
    main()
