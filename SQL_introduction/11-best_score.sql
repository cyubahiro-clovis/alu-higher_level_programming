-- Lists records with a score of 10 or more, ordered by score
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
