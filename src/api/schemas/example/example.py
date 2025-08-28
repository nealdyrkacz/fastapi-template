import uuid
from pydantic import BaseModel

from src.domain.example.models.example import Example

class ExampleCreate(BaseModel):
    name: str
    
class ExampleResponse(BaseModel):
    id: uuid.UUID
    name: str

    staticmethod
    def from_entity(example: Example):
        
        return ExampleResponse(
            id=str(example.id),
            name=example.name,
        )