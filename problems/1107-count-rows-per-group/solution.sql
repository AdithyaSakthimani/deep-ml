-- Employees per department
SELECT department_id, COUNT(*) AS headcount
FROM employees
Group By department_id
