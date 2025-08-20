from typing import Optional
from pydantic import BaseModel

class FilterOptions(BaseModel):
    sort_by: Optional[str] = None
    active: Optional[bool] = None
    ids: Optional[str] = None