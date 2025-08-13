from typing import Optional
from pydantic import BaseModel, Field

class PaginationOptions(BaseModel):
    page: Optional[int] = Field(None, ge=1)
    page_size: Optional[int] = Field(None, ge=1, le=100)

    def is_pagination_enabled(self) -> bool:
        return self.page is not None and self.page_size is not None

class FilterOptions(BaseModel):
    sort_by: Optional[str] = None
    active: Optional[bool] = None
    ids: Optional[str] = None
