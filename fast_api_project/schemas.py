from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel, validator


class CreatedModifiedMixin(BaseModel):
    created: Optional[datetime]
    modified: Optional[datetime]

    @validator('created', 'modified', pre=True, always=True)
    def default_datetime(cls, value: datetime) -> datetime:
        return value or datetime.now()


class IdModelMixin(BaseModel):
    id: int
