-- Lists the number of records by score in second_table, sorted by the number of records descending
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
