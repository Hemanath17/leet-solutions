select e1.name
from Employee e1
join(
    select managerID, count(*) as directReports
    from employee
    group by managerID
    having count(*)>=5
) e2 on e1.id = e2.managerID;