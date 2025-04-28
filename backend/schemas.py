from pydantic import BaseModel
from datetime import datetime

class BookingCreate(BaseModel):
    user: str
    car: str
    start_time: datetime
    end_time: datetime

class CarCreate(BaseModel):
    name: str
