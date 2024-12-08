from app.database import Base
from sqlalchemy import TIMESTAMP, Column, String, Boolean, Integer
from sqlalchemy.sql import func


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    full_name = Column(String, nullable=False, index=True)
    user_name = Column(String, nullable=False, index=True)
    active = Column(Boolean, nullable=False, default=True)
    created_at = Column(
        TIMESTAMP(timezone=False), nullable=False, server_default=func.now()
    )
    updated_at = Column(TIMESTAMP(timezone=False), default=None, onupdate=func.now())
