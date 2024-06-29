from fastapi import APIRouter

from api.v1.endpoints import curso_alchemy

api_router = APIRouter()
api_router.include_router(curso_alchemy.router, prefix='/cursos', tags=['cursos'])