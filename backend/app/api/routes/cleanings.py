from fastapi import APIRouter
from typing import List

router = APIRouter()

@router.get('/')
async def get_all_cleanings() -> List[dict]:
    return [
        {"id": 1, "name": "My house", "cleaning_type": "full_clean", "price_per_hour": 29.99},
    ] 