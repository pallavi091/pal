from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from app.database import Base, engine
from app.routes import employee_routes, attendance_routes
from app.models import employee, attendance
from app.routes import attendance_routes

Base.metadata.create_all(bind=engine)

app = FastAPI(title="HRMS Lite API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(employee_routes.router, prefix="/employees", tags=["Employees"])
app.include_router(attendance_routes.router, prefix="/attendance", tags=["Attendance"])
# app.include_router(attendance_routes.router)

@app.get("/")
def home():
    return {"message": "HRMS running"}









