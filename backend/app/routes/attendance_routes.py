


from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas
from app.database import SessionLocal, engine

# Create tables if not exist
# models.Attendance.metadata.create_all(bind=engine)

router = APIRouter()

# @router.get("/")
# def get_attendance():
#     return {"message": "Attendance route working"}

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Mark Attendance
@router.post("/", response_model=schemas.AttendanceResponse)
def mark_attendance(attendance: schemas.AttendanceCreate, db: Session = Depends(get_db)):
    employee = db.query(models.Employee).filter(models.Employee.id == attendance.employee_id).first()
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    
    db_attendance = models.Attendance(**attendance.dict())
    db.add(db_attendance)
    db.commit()
    db.refresh(db_attendance)
    return db_attendance

# # Mark attendance
# @router.post("/{employee_id}")
# def mark_attendance(employee_id: str, db: Session = Depends(get_db)):
#     employee = db.query(Employee).filter(Employee.employee_id == employee_id).first()
#     if not employee:
#         raise HTTPException(status_code=404, detail="Employee not found")

#     attendance = Attendance(employee_id=employee.employee_id)
#     db.add(attendance)
#     db.commit()
#     db.refresh(attendance)
#     return attendance


# Get attendance for employee
@router.get("/{employee_id}", response_model=list[schemas.AttendanceResponse])
def get_attendance(employee_id: int, db: Session = Depends(get_db)):
    employee = db.query(models.Employee).filter(models.Employee.id == employee_id).first()
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return db.query(models.Attendance).filter(models.Attendance.employee_id == employee_id).all()
