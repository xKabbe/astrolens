from fastapi import APIRouter

router = APIRouter()

@router.get('/', summary='Hello World Endpoint')
async def hello_world():
    return {'message': 'Hello, World!'}
