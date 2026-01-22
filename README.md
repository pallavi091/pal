# React + Vite

This template provides a minimal setup to get React working in Vite with HMR and some ESLint rules.

Currently, two official plugins are available:

- [@vitejs/plugin-react](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react) uses [Babel](https://babeljs.io/) (or [oxc](https://oxc.rs) when used in [rolldown-vite](https://vite.dev/guide/rolldown)) for Fast Refresh
- [@vitejs/plugin-react-swc](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react-swc) uses [SWC](https://swc.rs/) for Fast Refresh

## React Compiler

The React Compiler is not enabled on this template because of its impact on dev & build performances. To add it, see [this documentation](https://react.dev/learn/react-compiler/installation).

## Expanding the ESLint configuration

If you are developing a production application, we recommend using TypeScript with type-aware lint rules enabled. Check out the [TS template](https://github.com/vitejs/vite/tree/main/packages/create-vite/template-react-ts) for information on how to integrate TypeScript and [`typescript-eslint`](https://typescript-eslint.io) in your project.


# HRMS (Human Resource Management System)

## Project Overview
This is a Human Resource Management System (HRMS) web application that allows managing employees and tracking attendance.  
Features include:
- Add, view, and delete employees
- Mark and view employee attendance
- RESTful API backend with FastAPI
- Responsive frontend with React/Vite

---

## Tech Stack
**Frontend:**
- React.js (with Vite)
- Axios (for API requests)
- JavaScript, HTML, CSS

**Backend:**
- Python FastAPI
- SQLAlchemy ORM
- PostgreSQL Database
- Uvicorn (ASGI server)
- Pydantic (schemas & validation)

**Deployment:**
- Frontend: Vercel
- Backend: Render / Railway
- Database: PostgreSQL (Render / local)

---

## Project Structure

hrms-lite/
│
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── config.py
│   │   ├── database.py
│   │   │
│   │   ├── models/
│   │   │   ├── employee.py
│   │   │   └── attendance.py
│   │   │
│   │   ├── schemas/
│   │   │   ├── employee.py
│   │   │   └── attendance.py
│   │   │
│   │   ├── routes/
│   │   │   ├── employee_routes.py
│   │   │   └── attendance_routes.py
│   │   │
│   │   ├── services/
│   │   │   ├── employee_service.py
│   │   │   └── attendance_service.py
│   │   │
│   │   ├── utils/
│   │   │   └── validators.py
│   │   │
│   │   └── core/
│   │       └── exceptions.py
│   │
│   ├── requirements.txt
│   └── .env
│
├── frontend/
│   ├── src/
│   │   ├── api/
│   │   │   └── axios.js
│   │   │
│   │   ├── components/
│   │   │   ├── EmployeeForm.jsx
│   │   │   ├── EmployeeList.jsx
│   │   │   ├── AttendanceForm.jsx
│   │   │   └── AttendanceTable.jsx
│   │   │
│   │   ├── pages/
│   │   │   ├── Dashboard.jsx
│   │   │   ├── Employees.jsx
│   │   │   └── Attendance.jsx
│   │   │
│   │   ├── layouts/
│   │   │   └── MainLayout.jsx
│   │   │
│   │   ├── App.jsx
│   │   ├── main.jsx
│   │   └── styles.css
│   │
│   ├── package.json
│   └── vite.config.js
│
├── README.md
└── docker-compose.yml


## Running Locally

### **Backend Setup**
1. Navigate to the backend folder:

cd backend
Create a virtual environment and activate it:

python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
Install dependencies:

pip install -r requirements.txt
4. Set up PostgreSQL database and update database.py with your database credentials.

Run the backend server:

uvicorn app.main:app --reload
The API will run at: http://127.0.0.1:8000





Frontend Setup

Navigate to the frontend folder:

cd frontend


Install dependencies:

npm install


Update the API base URL in src/api/axios.js if needed:

const api = axios.create({
  baseURL: "http://127.0.0.1:8000", // or live backend URL
});

Start the development server:

npm run dev


The frontend will run at http://localhost:5173



DATABASE:
As i am using postgres databse for the backend so you need to create the credentials in local first and in the backend databses.py file you have to update the DATABASE_URL(password) and then you need to create the databse in the postgres itself. in my case it is hrms. 



Deployment

Frontend: Deploy to Vercel by connecting GitHub repo

Backend: Deploy to Render or Railway with PostgreSQL database

Update frontend API base URL to point to the live backend


ASSUMPTION OR LIMITATION: 
because of shortage of the time, this is left but i can do it easily when it comes to an actual implementation, there is a primary_id and employee_id in the databse table. so when to delete or update or mark attendance you need to pass the primary_id not the employee_id. so this is the only limitaion.
 

THANK YOU!