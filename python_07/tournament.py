from ex0 import AquaFactory, FlameFactory
from ex0 import CreatureFactory
from ex2 import AggressiveStrategy, DefensiveStrategy, NormalStrategy
from ex2 import BattleStrategy, InvalidStrategyError
from ex1 import HealingCreatureFactory, TransformCreatureFactory


def run_action(strategy: BattleStrategy, creature) -> None:
    for line in strategy.act(creature):
        print(line)


def run_tournament(
    opponents: list[tuple[CreatureFactory, BattleStrategy]],
) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")
    print()
    creatures = []
    for factory, strategy in opponents:
        creatures.append((factory.create_base(), strategy))
    for i in range(len(creatures)):
        for j in range(i + 1, len(creatures)):
            creature1, strategy1 = creatures[i]
            creature2, strategy2 = creatures[j]
            print("* Battle *")
            print(creature1.describe())
            print("vs.")
            print(creature2.describe())
            print("now fight!")
            try:
                run_action(strategy1, creature1)
                run_action(strategy2, creature2)
            except InvalidStrategyError as error:
                print(f"Battle error, aborting tournament: {error}")
                return
            print()


def main() -> None:
    print("Tournament 0 (basic)")
    print("[ (Flameling+Normal), (Healing+Defensive) ]")
    run_tournament([
        (FlameFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
    ])
    print("Tournament 1 (error)")
    print("[ (Flameling+Aggressive), (Healing+Defensive) ]")
    run_tournament([
        (FlameFactory(), AggressiveStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
    ])
    print("Tournament 2 (multiple)")
    print("[ (Aquabub+Normal), (Healing+Defensive), "
          "(Transform+Aggressive) ]")
    run_tournament([
        (AquaFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
        (TransformCreatureFactory(), AggressiveStrategy()),
    ])


if __name__ == "__main__":
    main()
