from enum import Enum, unique, auto


@unique
class ServicesState(Enum):
    SCHEDULE = auto()
    UNSCHEDULED = auto()
