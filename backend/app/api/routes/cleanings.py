from typing import List

from fastapi import APIRouter, Body, Depends, HTTPException
from starlette import status

from app.models.cleaning import CleaningCreate, CleaningPublic
from app.db.repositories.cleanings import CleaningsRepository
from app.api.dependencies.database import get_repository

router = APIRouter()


@router.get(
    "/",
    response_model=List[CleaningPublic],
    status_code=status.HTTP_200_OK,
    name="cleanings:get-all-cleanings",
)
async def get_all_cleanings(
    cleaning_repo: CleaningsRepository = Depends(get_repository(CleaningsRepository)),
) -> List[CleaningPublic]:
    return await cleaning_repo.get_all_cleanings()


@router.get(
    "/{id}",
    response_model=CleaningPublic,
    status_code=status.HTTP_200_OK,
    name="cleanings:get-cleaning-by-id",
)
async def get_detail_cleanings(
    id: int,
    cleaning_repo: CleaningsRepository = Depends(get_repository(CleaningsRepository)),
) -> List[CleaningPublic]:
    cleaning =  await cleaning_repo.get_detail_cleanings(id)


    if not cleaning:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No cleaning found with that id.")
 
    return cleaning
 


@router.post(
    "/",
    response_model=CleaningPublic,
    name="cleanings:create-cleaning",
    status_code=status.HTTP_201_CREATED,
)
async def create_new_cleaning(
    new_cleaning: CleaningCreate = Body(..., embed=True),
    cleanings_repo: CleaningsRepository = Depends(get_repository(CleaningsRepository)),
) -> CleaningPublic:
    new_cleaning = await cleanings_repo.create_cleaning(new_cleaning=new_cleaning)
    return new_cleaning

