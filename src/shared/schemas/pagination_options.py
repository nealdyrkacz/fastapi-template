from pydantic import BaseModel, Field

class PaginationOptions(BaseModel):
    page: int = Field(1, ge=1)
    page_size: int = Field(10, ge=1, le=1000)

    def is_pagination_enabled(self) -> bool:
        return self.page is not None and self.page_size is not None