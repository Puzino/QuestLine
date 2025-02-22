from fastapi import APIRouter, Depends

from auth.authenticate import authenticate

game_router = APIRouter()

# TODO: Make a location in database with generate monsters on location
locations = {
    '1': {'name': 'local_1', 'monsters': [{'name': 'Goblin', 'level': 1}, {'name': 'Ork', 'level': 1}]},
    '2': {'name': 'local_2', 'monsters': [{'name': 'Bear', 'level': 2}, {'name': 'Ork', 'level': 3}]},
}


@game_router.get('/location')
async def location(user: str = Depends(authenticate)):
    return {'message': locations}
