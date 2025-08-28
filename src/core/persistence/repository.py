from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Generic, TypeVar, Optional, Sequence

T = TypeVar("T")

@dataclass
class FilterOptions:
    limit: Optional[int] = None
    offset: Optional[int] = None
    page: Optional[int] = None
    page_size: Optional[int] = 50
    sort_by: Optional[str] = None
    sort_order: str = "asc"

class Repository(ABC, Generic[T]):
    @abstractmethod
    async def exists(self, id: str) -> bool:
        """Check if an entity with the given ID exists."""
        pass

    @abstractmethod
    async def get_by_id(self, id: str) -> Optional[T]:
        """Get an entity by its ID. Returns None if not found."""
        pass

    @abstractmethod
    async def get_by_ids(self, ids: Sequence[str], sort_by: Optional[str] = None, sort_order: str = "asc") -> list[T]:
        """Get multiple entities by their IDs."""
        pass

    @abstractmethod
    async def create(self, entity: T) -> T:
        """Create a new entity."""
        pass

    @abstractmethod
    async def update(self, entity: T) -> T:
        """Update an existing entity."""
        pass

    @abstractmethod
    async def delete(self, id: str) -> bool:
        """Delete an entity by ID. Returns True if deleted, False if not found."""
        pass

    @abstractmethod
    async def filter(self, *args, **kwargs) -> list[T]:
        """
        Filter method that each repository can implement with their own signature.
        Children define their own parameters based on their needs.
        """
        pass

