from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import models, schemas
from database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/book/")
def create_booking(booking: schemas.BookingCreate, db: Session = Depends(get_db)):
    db_booking = models.Booking(**booking.dict())
    db.add(db_booking)
    db.commit()
    db.refresh(db_booking)
    return db_booking

@router.get("/bookings/")
def get_bookings(db: Session = Depends(get_db)):
    return db.query(models.Booking).all()

@router.post("/car/")
def add_car(car: schemas.CarCreate, db: Session = Depends(get_db)):
    db_car = models.Car(name=car.name)
    db.add(db_car)
    db.commit()
    db.refresh(db_car)
    return db_car

@router.get("/cars/")
def list_cars(db: Session = Depends(get_db)):
    return db.query(models.Car).all()

@router.delete("/car/{car_id}")
def delete_car(car_id: int, db: Session = Depends(get_db)):
    car = db.query(models.Car).get(car_id)
    db.delete(car)
    db.commit()
    return {"ok": True}
