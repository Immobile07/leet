-- Last updated: 12/7/2025, 1:14:28 AM
# Write your MySQL query statement below
select unique_id,name from employees left join employeeuni on employees.id=employeeuni.id;