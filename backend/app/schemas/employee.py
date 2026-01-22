from pydantic import BaseModel, EmailStr

class EmployeeCreate(BaseModel):
    employee_id: str
    full_name: str
    email: EmailStr
    department: str

class EmployeeResponse(EmployeeCreate):
    id: int

    class Config:
        from_attributes = True
        # orm_mode = True

class EmployeeUpdate(BaseModel):
    full_name: str
    email: EmailStr
    department: str
