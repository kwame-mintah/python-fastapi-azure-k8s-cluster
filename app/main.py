import uvicorn
from fastapi import FastAPI

from app.internal import versions
from app.routers import demo

app = FastAPI()
app.include_router(demo.router)
app.include_router(versions.router)


@app.get("/")
async def root():
    return {"message": "FastAPI on Azure Kubernetes Cluster (AKS)"}


if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000)
