from pydantic import BaseModel
from typing import Optional


class ExampleBase(BaseModel):
    name: str


class ExampleCreate(ExampleBase):
    pass


class ExampleUpdate(ExampleBase):
    id: int
    name: Optional[str] = None


class ExampleInDBBase(ExampleBase):
    id: int
    name: str

    # here will be placed all fields without fks and m2m fields (like user_id, group_id, etc)

    class Config:
        orm_mode = True


class ExampleInDB(ExampleInDBBase):
    pass
    # here will be model's fks and m2m fields
