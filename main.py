from fastapi import FastAPI

from core.configs import settings
from api.v1.api_v1 import api_router as api_v1_router
from api.v2.api_v2 import api_router as api_v2_router

app: FastAPI = FastAPI(title='Curso API - FastAPI SQL Model')

app.include_router(api_v1_router, prefix=settings.API_V1_STR)
app.include_router(api_v2_router, prefix=settings.API_V2_STR)


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000,
                log_level='info', reload=True)
