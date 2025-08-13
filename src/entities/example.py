from datetime import datetime
import uuid
from typing import List, Optional

from pydantic import BaseModel

class Example(BaseModel):
    id: uuid.UUID
    name: str

    model_config = {
        "frozen": True
    }
