from typing import Type, TypeVar, Callable
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.core.database.db import get_db

TRepo = TypeVar("TRepo")
TService = TypeVar("TService")

def repository_provider(repo_cls: Type[TRepo]) -> Callable:
    async def _get_repo(session: AsyncSession = Depends(get_db)) -> TRepo:
        return repo_cls(session)
    return _get_repo

def service_provider(service_cls: Type[TService], repo_cls: Type[TRepo]) -> Callable:
    async def _get_service(
        repo: TRepo = Depends(repository_provider(repo_cls)),
        session: AsyncSession = Depends(get_db)
    ) -> TService:
        # Pass both repo and session so service can control transactions
        return service_cls(repo, session)
    return _get_service