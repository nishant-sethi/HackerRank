import { useState } from 'react';

function EmployeesList({ employees }) {
  const [empList, setEmpList] = useState(employees);

  function getFilteredList(empList, val) {
    const filterEmps = empList.filter((emp) =>
      emp.name.toUpperCase().includes(val.toUpperCase())
    );
    setEmpList(filterEmps);
  }
  return (
    <>
      <div className='controls'>
        <input
          type='text'
          className='filter-input'
          data-testid='filter-input'
          onChange={(e) => getFilteredList(employees, e.target.value)}
        />
      </div>
      <ul className='employees-list'>
        {empList.map((employee) => (
          <li key={employee.name} data-testid='employee'>
            {employee.name}
          </li>
        ))}
      </ul>
    </>
  );
}
export default EmployeesList;
