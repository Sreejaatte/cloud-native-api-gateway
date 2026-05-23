
from fastapi import FastAPI
from app.api.routes.auth import router as auth_router

app = FastAPI(title="Cloud Native API Gateway")

app.include_router(auth_router, prefix="/api/v1/auth")

@app.get("/health")
def health():
    return {"status": "healthy"}
