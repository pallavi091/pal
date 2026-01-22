import { useState } from "react";
import api from "../api/axios";

export default function AddEmployee() {
  const [form, setForm] = useState({
    employee_id: "",
    full_name: "",
    email: "",
    department: "",
  });
  const [message, setMessage] = useState("");

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await api.post("/employees/", form);
      setMessage("Employee added successfully!");
      setForm({ employee_id: "", full_name: "", email: "", department: "" });
    } catch (err) {
      setMessage(err.response?.data?.detail || "Error adding employee");
    }
  };

  return (
    <div>
      <h1>Add Employee</h1>
      {message && <p>{message}</p>}
      <form onSubmit={handleSubmit}>
        <input
          name="employee_id"
          placeholder="Employee ID"
          value={form.employee_id}
          onChange={handleChange}
          required
        />
        <input
          name="full_name"
          placeholder="Full Name"
          value={form.full_name}
          onChange={handleChange}
          required
        />
        <input
          type="email"
          name="email"
          placeholder="Email"
          value={form.email}
          onChange={handleChange}
          required
        />
        <input
          name="department"
          placeholder="Department"
          value={form.department}
          onChange={handleChange}
          required
        />
        <button type="submit">Add Employee</button>
      </form>
    </div>
  );
}



// import { useState } from "react";
// import api from "../api/axios";

// export default function AddEmployee({ onEmployeeAdded }) {
//   const [form, setForm] = useState({
//     employee_id: "",
//     full_name: "",
//     email: "",
//     department: "",
//   });
//   const [message, setMessage] = useState("");

//   const handleChange = (e) => {
//     setForm({ ...form, [e.target.name]: e.target.value });
//   };

//   const handleSubmit = async (e) => {
//     e.preventDefault();
//     try {
//       await api.post("/employees/", form);
//       setMessage("Employee added successfully!");
//       setForm({ employee_id: "", full_name: "", email: "", department: "" });

//       // Refresh the employee list if callback is provided
//       if (onEmployeeAdded) onEmployeeAdded();

//       // Clear message after 3 seconds
//       setTimeout(() => setMessage(""), 3000);
//     } catch (err) {
//       setMessage(err.response?.data?.detail || "Error adding employee");
//       setTimeout(() => setMessage(""), 5000);
//     }
//   };

//   return (
//     <div>
//       <h1>Add Employee</h1>
//       {message && <p>{message}</p>}
//       <form onSubmit={handleSubmit}>
//         <input
//           name="employee_id"
//           placeholder="Employee ID"
//           value={form.employee_id}
//           onChange={handleChange}
//           required
//         />
//         <input
//           name="full_name"
//           placeholder="Full Name"
//           value={form.full_name}
//           onChange={handleChange}
//           required
//         />
//         <input
//           type="email"
//           name="email"
//           placeholder="Email"
//           value={form.email}
//           onChange={handleChange}
//           required
//         />
//         <input
//           name="department"
//           placeholder="Department"
//           value={form.department}
//           onChange={handleChange}
//           required
//         />
//         <button type="submit">Add Employee</button>
//       </form>
//     </div>
//   );
// }
