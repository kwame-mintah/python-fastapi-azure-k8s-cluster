import sys

import fastapi
from fastapi import APIRouter
from packaging import version

from app.models.models import Package

router = APIRouter(prefix="/v1/version", tags=["versions"])


@router.get(
    "/python",
    operation_id="pythonVersion",
    summary="Python version installed",
    response_model=Package,
)
async def python_version() -> Package:
    return Package(version=str(sys.version_info))


@router.get(
    "/fastapi",
    operation_id="fastapiVersion",
    summary="FastAPI version installed",
    response_model=Package,
)
async def fastapi_version() -> Package:
    return Package(version=version.parse(fastapi.__version__).base_version)
