from typing import Generic, List, Optional, TypeVar
from urllib.parse import urlencode
from pydantic import BaseModel, model_validator
from fastapi import Request

T = TypeVar("T")


class ResponseItem(BaseModel, Generic[T]):
    item: T

class ResponseItems(BaseModel, Generic[T]):
    items: list[T]

class PaginatedLinks(BaseModel):
    self: str
    next_page: Optional[str] = None
    prev_page: Optional[str] = None
    first: Optional[str] = None
    last: Optional[str] = None


class PaginatedMeta(BaseModel):
    pages: int
    page: int
    page_size: int
    next_page: Optional[int] = None
    prev_page: Optional[int] = None


class PaginatedResponseItems(BaseModel, Generic[T]):
    items: List[T]
    meta: PaginatedMeta
    links: PaginatedLinks

    @classmethod
    def create(
        cls,
        *,
        items: List[T],
        total: int,
        page: int,
        page_size: int,
        base_url: str,
    ) -> "PaginatedResponseItems[T]":
        pages = (total + page_size - 1) // page_size
        next_page = page + 1 if page < pages else None
        prev_page = page - 1 if page > 1 else None

        def build_url(page_number: Optional[int]) -> Optional[str]:
            if page_number is None:
                return None
            
            return f"{base_url}?{urlencode({'page': page_number, 'page_size': page_size})}"

        links = PaginatedLinks(
            self=build_url(page),
            next=build_url(next_page),
            prev=build_url(prev_page),
            first=build_url(1),
            last=build_url(pages),
        )

        meta = PaginatedMeta(
            page=page,
            page_size=page_size,
            pages=pages,
            next_page=next_page,
            prev_page=prev_page,
        )

        return cls(items=items, meta=meta, links=links)


class Envelope(BaseModel, Generic[T]):
    data: List[T]
    meta: Optional[dict] = None
    links: Optional[dict] = None

    @model_validator(mode="before")
    def extract_meta_links(cls, values):
        data = values.get("data")

        # If this is a paginated object, unwrap items and extract meta/links
        if isinstance(data, PaginatedResponseItems):
            values["data"] = data.items
            values["meta"] = data.meta.model_dump()
            values["links"] = data.links.model_dump()

        return {k: v for k, v in values.items() if v is not None}
