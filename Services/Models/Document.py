from pydantic import BaseModel


class Document(BaseModel):
    Type: str
    MIME: str
    Base64: str
