import os

from fastapi import APIRouter, Depends

from app.services.demo_service import DemoService
from ..dependencies import get_demo_service
from ..models.models import Message

router = APIRouter(prefix="/v1/hello", tags=["hello"])
service_version = os.environ.get("SERVICE_VERSION", "___")


@router.get(
    "/",
    operation_id="helloWorld",
    summary="Demonstrating FastAPI on Azure K8S Cluster.",
    response_model=Message,
)
async def root(
    service: DemoService = Depends(get_demo_service()),
) -> Message:
    return service.return_stub_data(service_version)
