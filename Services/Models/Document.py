from pydantic import BaseModel


class Document(BaseModel):
    Base64: str
