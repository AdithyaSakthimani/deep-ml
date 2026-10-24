Select nth_salary From 
  ( Select salary as nth_salary , DENSE_RANK() OVER (Order By Salary Desc ) As Salary_rank
  	From employee ) As ranked
Where salary_rank = 3 Limit(1)
