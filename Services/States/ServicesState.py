from enum import Enum, unique, auto


@unique
class ServicesState(Enum):
    # The service has been schedule for apply the service
    SCHEDULE = auto()
    # The service is pending of schedule for apply the service
    UNSCHEDULED = auto()
    # The client cancel the applying of recurring service
    INACTIVE = auto()
    # The service is pending of pay by the client
    PENDING_PAY = auto()
