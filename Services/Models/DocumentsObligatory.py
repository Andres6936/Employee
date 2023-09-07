from pydantic import BaseModel

from Services.Models.Document import Document


class DocumentsObligatory(BaseModel):
    Process: str
    Documents: list[Document]
