from abc import ABC, abstractmethod
from ex0.creatures import Creature
from ex1.capabilities import HealCapability, TransformCapability
from .exceptions import InvalidStrategyError
import typing


class BattleStrategy(ABC):
    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass

    @abstractmethod
    def act(self, creature: Creature) -> list[str]:
        pass


class NormalStrategy(BattleStrategy):
    def is_valid(self, _creature: Creature) -> bool:
        return True

    def act(self, creature: Creature) -> list[str]:
        return [creature.attack()]


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> list[str]:
        if self.is_valid(creature):
            tranformer = typing.cast(TransformCapability, creature)
            return [tranformer.transform(), creature.attack(),
                    tranformer.revert()]
        else:
            raise InvalidStrategyError("Invalid Creature "
                                       f"'{creature.get_name()}'"
                                       " for this aggressive strategy"
                                       )


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> list[str]:
        if self.is_valid(creature):
            healer = typing.cast(HealCapability, creature)
            return [creature.attack(), healer.heal()]
        else:
            raise InvalidStrategyError("Invalid Creature "
                                       f"'{creature.get_name()}'"
                                       " for this aggressive strategy"
                                       )
