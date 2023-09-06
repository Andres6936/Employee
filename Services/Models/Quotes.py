from pydantic import BaseModel


class Quotes(BaseModel):
    Name: str
    Email: str
    NumberPhone: str
    Address: str
    Observation: str
