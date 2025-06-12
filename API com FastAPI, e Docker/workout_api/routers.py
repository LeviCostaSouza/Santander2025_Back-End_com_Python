from fastapi import APIRouter  
from workout_api.atleta.controller import router as atleta
from workout_api.categorias.controller import router as categorias
from workout_api.centro_treinamentos.controller import router as centro_treinamentos

api_router = APIRouter()
api_router.include_router(atleta, prefix='/atletas', tags=['atletas'])
api_router.include_router(categorias, prefix='/categorias', tags=['categorias'])
api_router.include_router(centro_treinamentos, prefix='/centro_treinamentos', tags=['centro_treinamentos'])
