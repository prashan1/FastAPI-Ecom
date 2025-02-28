from typing import List
 
from fastapi import APIRouter, Body, Depends  
from starlette.status import HTTP_201_CREATED  
 
from app.models.cleaning import CleaningCreate, CleaningPublic  
from app.db.repositories.cleanings import CleaningsRepository  
from app.api.dependencies.database import get_repository

router = APIRouter()

@router.get('/')
async def get_all_cleanings() -> List[dict]:
    return [
        {"id": 1, "name": "My house", "cleaning_type": "full_clean", "price_per_hour": 29.99},
    ] 
    
@router.post('/', response_model=CleaningPublic, name='cleanings:create-cleaning', status_code=HTTP_201_CREATED)
async def create_new_cleaning(
    new_cleaning: CleaningCreate = Body(..., embed=True),
    cleanings_repo: CleaningsRepository = Depends(get_repository(CleaningsRepository))
) -> CleaningPublic:
    new_cleaning = cleanings_repo.create_cleaning(new_cleaning=new_cleaning)
    return new_cleaning
