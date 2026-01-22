# from sqlalchemy import Column, Integer, String, Date, ForeignKey
# from app.database import Base
# from sqlalchemy.orm import relationship

# class Attendance(Base):
#     __tablename__ = "attendances"

#     id = Column(Integer, primary_key=True, index=True)
#     employee_id = Column(Integer, ForeignKey("employees.id"), nullable=False)
#     date = Column(Date, nullable=False)
#     status = Column(String, nullable=False)

#     employee = relationship("Employee", backref="attendances")




from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base 
from .employee import Employee

class Attendance(Base):
    __tablename__ = "attendance"

    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey("employees.id"), nullable=False)
    status = Column(String, default="present")  
    date = Column(DateTime, default=datetime.utcnow)

    employee = relationship("Employee", back_populates="attendances")



