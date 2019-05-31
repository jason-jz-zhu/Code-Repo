-- 1 dense_rank
/*
Name	  Sales	Sales_Rank
Greg	   50	      1
Sophia	 40	      2
Stella	 20	      3
Jeff	   20	      3
Jennifer 15	      4
John	   10	      5
*/

SELECT a1.Name, a1.Sales, COUNT(DISTINCT a2.Sales) Sales_Rank
FROM Total_Sales a1, Total_Sales a2
WHERE a1.Sales <= a2.Sales
GROUP BY a1.Name, a1.Sales
ORDER BY a1.Sales DESC, a1.Name DESC;


-- 2 rank
/*
Name	  Sales	Sales_Rank
Greg	   50	      1
Sophia	 40	      2
Stella	 20	      3
Jeff	   20	      3
Jennifer 15	      5
John	   10	      6
*/

SELECT a1.Name, a1.Sales, COUNT(a2.Sales) Sales_Rank
FROM Total_Sales a1, Total_Sales a2
WHERE a1.Sales < a2.Sales OR (a1.Sales = a2.Sales AND a1.Name = a2.Name)
GROUP BY a1.Name, a1.Sales
ORDER BY a1.Sales DESC, a1.Name DESC;


-- 3 row_number
/*
Name	  Sales	Sales_Rank
Greg	   50	      1
Sophia	 40	      2
Stella	 20	      3
Jeff	   20	      4
Jennifer 15	      5
John	   10	      6
*/

SELECT a1.Name, a1.Sales, COUNT(a2.Sales) Sales_Rank
FROM Total_Sales a1, Total_Sales a2
WHERE a1.Sales < a2.Sales OR (a1.Sales = a2.Sales AND a1.Name <= a2.Name)
GROUP BY a1.Name, a1.Sales
ORDER BY a1.Sales DESC, a1.Name DESC;
