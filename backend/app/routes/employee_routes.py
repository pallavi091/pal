from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas
from app.schemas.employee import EmployeeCreate, EmployeeResponse
from app.models import Employee, Attendance
from app.database import SessionLocal, engine
from typing import List

router = APIRouter()
# router = APIRouter(prefix="/attendance", tags=["Attendance"])

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Add Employee
@router.post("/", response_model=schemas.EmployeeResponse)
def create_employee(employee: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    existing = db.query(models.Employee).filter(
        (models.Employee.employee_id == employee.employee_id) | 
        (models.Employee.email == employee.email)
    ).first()
    if existing:
        raise HTTPException(status_code=400, detail="Employee ID or Email already exists")
    
    db_employee = models.Employee(**employee.dict())
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee

# Get all employees
@router.get("/", response_model=list[schemas.EmployeeResponse])
def get_employees(db: Session = Depends(get_db)):
    return db.query(models.Employee).all()

# Delete employee
@router.delete("/{employee_id}")
def delete_employee(id: int, db: Session = Depends(get_db)):
    employee = db.query(models.Employee).filter(models.Employee.id == id).first()
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    db.delete(employee)
    db.commit()
    return {"detail": "Employee deleted successfully"}

@router.get("/", response_model=list[schemas.EmployeeResponse])
def get_employees(db: Session = Depends(get_db)):
    return db.query(models.Employee).all()

@router.put("/{employee_id}", response_model=schemas.EmployeeResponse)
def update_employee(
    employee_id: str,
    employee: schemas.EmployeeUpdate,
    db: Session = Depends(get_db)
):
    db_employee = db.query(models.Employee).filter(
        models.Employee.employee_id == employee_id
    ).first()

    if not db_employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    db_employee.full_name = employee.full_name
    db_employee.email = employee.email
    db_employee.department = employee.department

    db.commit()
    db.refresh(db_employee)

    return db_employee




# Mark attendance
@router.post("/", response_model=schemas.AttendanceResponse)
def mark_attendance(attendance: schemas.AttendanceCreate, db: Session = Depends(get_db)):
    db_attendance = models.Attendance(**attendance.dict())
    db.add(db_attendance)
    db.commit()
    db.refresh(db_attendance)
    return db_attendance

# List attendance
@router.get("/", response_model=List[schemas.AttendanceResponse])
def list_attendance(db: Session = Depends(get_db)):
    return db.query(models.Attendance).all()
