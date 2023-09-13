from pydantic import BaseModel


class Operator(BaseModel):
    Name: str
    NumberPhone: str
