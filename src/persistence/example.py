import logging
from typing import Optional, Sequence
from sqlalchemy.ext.asyncio import AsyncSession

from sqlalchemy.orm import declarative_base, Mapped, mapped_column
from sqlalchemy import UUID as saUUID, String

from uuid import UUID, uuid4

from src.api.schemas.example import ExampleCreate
from src.core.persistence.repository import Repository

from src.entities.example import Example as ExampleEntity

Base = declarative_base()

logger = logging.getLogger(__name__)

class Example(Base):
    __tablename__ = "example"
    id: Mapped[UUID] = mapped_column(saUUID(as_uuid=True), primary_key=True, insert_default=uuid4)
    name: Mapped[str] = mapped_column(String)


def map_orm_to_entity(orm: Example) -> ExampleEntity:
    return ExampleEntity(id=orm.id, name= orm.name)


class ExampleRepository(Repository[Example]):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def exists(self, id: str) -> bool:
        """Check if an entity with the given ID exists."""
        pass

    async def get_by_id(self, id: str) -> Optional[ExampleEntity]:
        """Get an entity by its ID. Returns None if not found."""
        pass

    async def get_by_ids(self, ids: Sequence[str], sort_by: Optional[str] = None, sort_order: str = "asc") -> list[ExampleEntity]:
        """Get multiple entities by their IDs."""
        pass

    async def create(self, dto: ExampleCreate) -> ExampleEntity:
        try:
            example = Example(**dto.model_dump())
            self.session.add(example)
            await self.session.flush()  # assigns ID without committing
            
            return map_orm_to_entity(example)
        except:
            logger.error("there was an error creating the example")
            raise
    

    async def update(self, entity: ExampleEntity) -> ExampleEntity:
        """Update an existing entity."""
        pass

    async def delete(self, id: str) -> bool:
        """Delete an entity by ID. Returns True if deleted, False if not found."""
        pass


    async def filter(self, *args, **kwargs) -> list[ExampleEntity]:
        try:
            q = self.session.query(Example)
            total = q.count()
            examples = q.offset((page - 1) * page_size).limit(page_size).all()

        return examples, total
            
            return map_orm_to_entity(example)
        except:
            logger.error("there was an error creating the example")
            raise