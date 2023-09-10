from enum import Enum, unique, auto


@unique
class ScheduleState(Enum):
    PENDING_SERVICE = auto()
