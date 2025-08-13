# services/user_service.py
from typing import Optional, Tuple
from sqlalchemy.ext.asyncio import AsyncSession
from persistence.example import ExampleRepository

from api.schemas.example import ExampleCreate

from entities.example import Example
from src.api.schemas.core.request import FilterOptions, PaginationOptions



class ExampleService:
    def __init__(self, repo: ExampleRepository, session: AsyncSession):
        self.repo = repo
        self.session = session

    async def create_example(self, dto: ExampleCreate) -> Example:
        async with self.session.begin():  # Transaction scope
            example: Example = await self.repo.create(dto)
        # Commit happens automatically at the end of `begin()` block
        
        return example
    
    async def get_examples_by_pagination(self, pagination: Optional[PaginationOptions] = None, filters: Optional[FilterOptions] = None) -> Tuple[Example, int]:
        async with self.session.begin():
            examples, total = await self.repo.filter(pagination, filters)
            return examples, total

    
    async def get_examples(self, filters: Optional[FilterOptions] = None) -> Tuple[Example, int]:
        async with self.session.begin():
            examples, total = await self.repo.filter(pagination=None, filters=filters)
            return examples, total

    
'''
# Alternative: Let the service control transactions more explicitly
class ExampleServiceExplicit:
    def __init__(self, repo: ExampleRepository, session: AsyncSession):
        self.repo = repo
        self.session = session

    async def create_example(self, dto: ExampleCreate):
        try:
            # Start transaction
            await self.session.begin()
            
            result = await self.repo.create(dto)
            
            # Commit transaction
            await self.session.commit()
            
            return {"status": "ok"}
            
        except Exception as e:
            # Rollback on error
            await self.session.rollback()
            raise e
'''