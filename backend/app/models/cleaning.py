from enum import Enum
from typing import Optional

from app.models.core import IDModelMixin, CoreModel

class CleaningType(str, Enum):
    dust_up = "dust_up"
    spot_clean = "spot_clean"
    full_clean = "full_clean"
    
    
class CleaningBase(CoreModel):
    name: Optional[str]
    price: Optional[float]
    description: Optional[str]
    cleaning_type: Optional[CleaningType] = CleaningType.spot_clean


class CleaningCreate(CleaningBase):
    name: str
    price: float
    
    
class CleaningUpdate(CoreModel):
    cleaning_type: Optional[CleaningType]
    
    
class CleaningInDB(IDModelMixin, CleaningBase):
    name: str
    price: float
    cleaning_type: CleaningType


class CleaningPublic(IDModelMixin, CleaningBase):
    pass
