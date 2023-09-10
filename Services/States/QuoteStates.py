from enum import Enum, unique, auto


@unique
class QuoteStates(Enum):
    # The client has pending upload the obligatory documents to plataform
    PENDING_DOCUMENTS = auto()
    # The quote has pending the review of documents by an operator
    PENDING_REVIEW = auto()
    # The client has pending make the pay for the first service schedule
    PENDING_PAY = auto()
    # The operator reject the documents upload by the client
    REJECT_BY_DOCUMENTS = auto()
    # The pay of first service schedule is made by the client
    PAY_ACCEPTED = auto()
