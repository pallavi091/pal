from pydantic import BaseModel
from datetime import datetime

# class AttendanceCreate(BaseModel):
#     employee_id: int
#     date: datetime
#     status: str  

# class AttendanceResponse(AttendanceCreate):
#     id: int

#     class Config:
#          from_attributes = True


class AttendanceBase(BaseModel):
    employee_id: int
    status: str

class AttendanceCreate(AttendanceBase):
    pass

class AttendanceResponse(AttendanceBase):
    id: int
    date: datetime

    class Config:
        from_attributes = True