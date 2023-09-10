from enum import Enum, unique, auto


@unique
class QuoteStates(Enum):
    PENDING_REVIEW = auto()
    PENDING_PAY = auto()
    REJECT_BY_DOCUMENTS = auto()
    PAY_ACCEPTED = auto()
