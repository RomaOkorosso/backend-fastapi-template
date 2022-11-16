from typing import Generic, TypeVar
from sqlalchemy.orm import Session
from pydantic import BaseModel, validator

from app.db.base import Base
from app.db.session import SessionLocal

# Define custom types for SQLAlchemy model, and Pydantic schemas
ModelType = TypeVar("ModelType", bound=Base)


class BaseEnum(Generic[ModelType], BaseModel):
    class Config:
        arbitrary_types_allowed = True

    @validator("*", pre=True, always=True)
    def validate(cls, value: str):
        model: ModelType = cls.model

        db: Session = SessionLocal()
        items = db.query(model).all()
        db.close()

        db_item: ModelType | None = next(filter(lambda x: x.name == value, items), None)

        if db_item is None:
            #  logger.error(f"unsupported {ModelType} item received: {value}")
            return value

        return db_item
