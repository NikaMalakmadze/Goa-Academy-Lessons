SELECT * FROM movies
where director like "John%"
and title like '%r%'
and year >= 2000
and id % 2 == 0