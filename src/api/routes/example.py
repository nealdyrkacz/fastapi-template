import logging
from fastapi import APIRouter, Depends

from src.api.schemas.core.request import FilterOptions, PaginationOptions
from src.api.schemas.core.response import PaginatedResponseItems, ResponseItem
from src.api.schemas.example import ExampleCreate, ExampleResponse

import uuid

from src.core.dependency_injection.di import service_provider
from src.entities.example import Example
from src.persistence.example import ExampleRepository
from src.services.example import ExampleService

logger = logging.getLogger(__name__)

router = APIRouter()

@router.get("", response_model=PaginatedResponseItems[ExampleResponse])
async def get_examples(pagination: PaginationOptions = Depends(), filters: FilterOptions = Depends(), service: ExampleService = Depends(service_provider(ExampleService, ExampleRepository)),):

    result: list[Example] = None
    if pagination.is_pagination_enabled():
        result, total = await service.get_examples_by_pagination(pagination=pagination, filters=filters)
    else:
        result = await service.get_examples(filters=filters)

    return PaginatedResponseItems.create(
            items=result,
            page=pagination.page,
            page_size=pagination.page_size,
            total=total,
            base_url="/example"
        )



@router.post("", response_model=ResponseItem[ExampleResponse])
async def create_example(
    example: ExampleCreate,
    service: ExampleService = Depends(service_provider(ExampleService, ExampleRepository)),
):
    result: Example = await service.create_example(example)
    return ResponseItem(item=ExampleResponse.from_entity(result))