from pydantic import BaseModel


class ScheduleService(BaseModel):
    Service: str
    At: str
    Operator: str
    Manifest: str
