from typing import List
from app.db.repositories.base import  BaseRepository
from app.models.cleaning import CleaningCreate, CleaningUpdate, CleaningInDB


CREATE_CLEANING_QUERY = """
    INSERT INTO cleanings (name, description, price, cleaning_type)
    VALUES (:name, :description, :price, :cleaning_type)
    RETURNING id, name, description, price, cleaning_type;
"""
GET_CLEANING_QUERY = """
    SELECT * FROM cleanings;
"""

GET_DETAIL_CLEANING_QUERY = """
    SELECT * FROM cleanings where id = :cleaning_id;
"""


class CleaningsRepository(BaseRepository):
    
    async def get_all_cleanings(self) -> List[CleaningInDB]:
        return await self.db.fetch_all(query=GET_CLEANING_QUERY)
    
    async def get_detail_cleanings(self, cleaning_id) -> List[CleaningInDB]:
        return await self.db.fetch_one(query=GET_DETAIL_CLEANING_QUERY, values={"cleaning_id": cleaning_id})
    
    async def create_cleaning(self, *, new_cleaning: CleaningCreate) -> CleaningInDB:
        query_values = new_cleaning.dict()
        cleaning = await self.db.fetch_one(query=CREATE_CLEANING_QUERY, values=query_values)
        return CleaningInDB(**cleaning)