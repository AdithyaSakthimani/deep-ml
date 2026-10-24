SELECT MAX(nth_salary) AS nth_salary
FROM (
    SELECT salary AS nth_salary,
           DENSE_RANK() OVER (ORDER BY salary DESC) AS salary_rank
    FROM (SELECT DISTINCT salary FROM employee) AS unique_salaries
) AS ranked
WHERE salary_rank = 3;