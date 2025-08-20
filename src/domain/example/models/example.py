import uuid
from pydantic import BaseModel

class Example(BaseModel):
    id: uuid.UUID
    name: str

    model_config = {
        "frozen": True
    }
