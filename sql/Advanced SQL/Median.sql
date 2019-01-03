SELECT Sales Median FROM
(SELECT a1.Name, a1.Sales, COUNT(a2.Sales) Rank
FROM Total_Sales a1, Total_Sales a2
WHERE a1.Sales < a2.Sales OR (a1.Sales=a2.Sales AND a1.Name <= a2.Name)
group by a1.Name, a1.Sales
order by a1.Sales desc) a3
WHERE Rank = floor((SELECT (COUNT(*)+1) / 2 FROM Total_Sales))
or Rank = floor((SELECT (COUNT(*)+2) / 2 FROM Total_Sales))
