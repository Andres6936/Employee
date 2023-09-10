from enum import Enum, unique, auto


@unique
class PlanType(Enum):
    DAILY = auto()
    WEEKLY = auto()
    MONTHLY = auto()
    ONCE = auto()
    PRIORITY = auto()
