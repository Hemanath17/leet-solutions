select w1.id
from weather w1, Weather w2
where datediff(w1.recordDate, w2.recordDate) = 1 AND w1.temperature > w2.temperature;
