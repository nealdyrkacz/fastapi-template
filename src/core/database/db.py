from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from contextlib import asynccontextmanager
from sqlalchemy.ext.asyncio import AsyncSession
from core.config.settings import Config

ASYNC_DATABASE_URL = Config.async_db_uri

engine = create_async_engine(ASYNC_DATABASE_URL, echo=True)
AsyncSessionLocal = async_sessionmaker(engine, expire_on_commit=False)

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        yield session


'''
#outside of FASTAPI route injection use
async for session in get_db():
    repo = ExampleRepository(session)
    service = ExampleService(repo, session)
    await service.create_example(...)
'''