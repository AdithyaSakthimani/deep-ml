-- Average salary per department
SELECT department_id, AVG(salary) AS avg_salary
FROM employees Group By department_id
