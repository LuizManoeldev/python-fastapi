from fastapi import APIRouter

from api.v2.endpoints import curso_model


api_router = APIRouter()
api_router.include_router(curso_model.router, prefix='/cursos', tags=['cursos'])
