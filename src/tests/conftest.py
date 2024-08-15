import pytest
from httpx import AsyncClient
from src.settings.settings import settings


@pytest.fixture
async def HttpxClient():
    async with AsyncClient(base_url=settings.url_settings.api_url) as client:
        yield client
