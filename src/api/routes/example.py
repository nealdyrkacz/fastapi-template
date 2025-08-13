from fastapi import APIRouter, Depends

from src.api.schemas.core.response import PaginatedResponseItems, ResponseItem
from src.api.schemas.example import ExampleCreate, ExampleResponse

import uuid

from src.core.dependency_injection.di import service_provider
from src.entities.example import Example
from src.persistence.example import ExampleRepository
from src.services.example import ExampleService

router = APIRouter()

@router.get("", response_model=PaginatedResponseItems[ExampleResponse])
async def get_examples(page: int=1, page_size: int = 10, service: ExampleService = Depends(service_provider(ExampleService, ExampleRepository)),):

    result: list[Example] = await service.get_examples()
    return PaginatedResponseItems.create(
            items=result,
            page=page,
            page_size=page_size,
            total=len(result),
            base_url="/example"
        )


@router.post("", response_model=ResponseItem[ExampleResponse])
async def create_example(
    example: ExampleCreate,
    service: ExampleService = Depends(service_provider(ExampleService, ExampleRepository)),
):
    result: Example = await service.create_example(example)
    return ResponseItem(item=ExampleResponse.from_entity(result))