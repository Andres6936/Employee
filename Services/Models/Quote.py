from pydantic import BaseModel


class Quote(BaseModel):
    Name: str
    Email: str
    NumberPhone: str
    Address: str
    Observation: str
    Value: int
    Plan: str
