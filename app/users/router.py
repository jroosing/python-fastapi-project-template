from fastapi import APIRouter, status, Depends, HTTPException, Response
from . import schemas, models
from app.database import get_db
from sqlalchemy.orm import Session


router = APIRouter()


@router.get("/")
def get_users(
    db: Session = Depends(get_db), limit: int = 10, page: int = 1, search: str = ""
):
    skip = (page - 1) * limit

    users = (
        db.query(models.User)
        .filter(models.User.full_name.contains(search))
        .limit(limit)
        .offset(skip)
        .all()
    )

    return {"status": "success", "results": len(users), "users": users}


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_user(payload: schemas.UserBaseSchema, db: Session = Depends(get_db)):
    new_user = models.User(**payload.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"status": "success", "user": new_user}


@router.get("/{userId}")
def get_user(userId: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == userId).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No user found with id: {userId}",
        )

    return {"status": "success", "user": user}


@router.patch("/{userId}")
def update_user(
    userId: int, payload: schemas.UserBaseSchema, db: Session = Depends(get_db)
):
    user_query = db.query(models.User).filter(models.User.id == userId)
    db_user = user_query.first()

    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No user found with id: {userId}",
        )

    update_data = payload.model_dump(exclude_unset=True)
    user_query.filter(models.User.id == userId).update(
        update_data, synchronize_session=False
    )

    db.commit()
    db.refresh(db_user)
    return {"status": "success", "user": db_user}


@router.delete("/{userId}")
def delete_user(userId: int, db: Session = Depends(get_db)):
    user_query = db.query(models.User).filter(models.User.id == userId)
    user = user_query.first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No user found with id: {userId}",
        )

    user_query.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)
