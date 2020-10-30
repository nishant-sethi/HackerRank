import React from "react";

class EmployeesList extends React.Component {
  state = {
    empList: this.props.employees,
  };
  getFilteredList(empList, val) {
    const filterEmps = empList.filter((emp) =>
      emp.name.toUpperCase().includes(val.toUpperCase())
    );
    this.setState({ empList: filterEmps });
  }

  render() {
    const { employees } = this.props;
    return (
      <React.Fragment>
        <div className="controls">
          <input
            type="text"
            className="filter-input"
            data-testid="filter-input"
            onChange={(e) => this.getFilteredList(employees, e.target.value)}
          />
        </div>
        <ul className="employees-list">
          {this.state.empList.map((employee) => (
            <li key={employee.name} data-testid="employee">
              {employee.name}
            </li>
          ))}
        </ul>
      </React.Fragment>
    );
  }
}

export default EmployeesList;
