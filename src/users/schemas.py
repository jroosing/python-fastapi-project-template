from pydantic import BaseModel
from typing import List


class UserBaseSchema(BaseModel):
    id: int | None = None
    first_name: str
    last_name: str
    full_name: str
    user_name: str
    active: bool = False

    class Config:
        from_attributes = True
        populate_by_name = True
        arbitrary_types_allowed = True


class ListUserResponse(BaseModel):
    status: str
    results: int
    users: List[UserBaseSchema]
