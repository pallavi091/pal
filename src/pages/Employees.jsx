// export default function Employees() {
//   return <h1>Employees Page</h1>;
// }


import { useEffect, useState } from "react";
import api from "../api/axios";

export default function Employees() {
  const [employees, setEmployees] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // Fetch employees
  const fetchEmployees = async () => {
    try {
      setLoading(true);
      const res = await api.get("/employees/");
      setEmployees(res.data);
    } catch (err) {
      setError("Failed to fetch employees");
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchEmployees();
  }, []);

  // Delete employee
  const handleDelete = async (employeeId) => {
    try {
      await api.delete(`/employees/${employeeId}`);
      setEmployees(employees.filter((e) => e.employeeId !== employeeId));
    } catch {
      alert("Failed to delete employee");
    }
  };

  if (loading) return <p>Loading employees...</p>;
  if (error) return <p>{error}</p>;
  if (employees.length === 0) return <p>No employees found.</p>;

  return (
    <div>
      <h1>Employees</h1>
      <table border="1" cellPadding="10">
        <thead>
          <tr>
            <th>ID</th>
            <th>Employee ID</th>
            <th>Full Name</th>
            <th>Email</th>
            <th>Department</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          {employees.map((emp) => (
            <tr key={emp.id}>
              <td>{emp.id}</td>
              <td>{emp.employee_id}</td>
              <td>{emp.full_name}</td>
              <td>{emp.email}</td>
              <td>{emp.department}</td>
              <td>
                <button onClick={() => handleDelete(emp.id)}>Delete</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
