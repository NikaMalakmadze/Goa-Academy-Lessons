-- Task 1
SELECT role, COUNT(*) as total_artists FROM employees
WHERE role = "Artist";

-- Task 2
SELECT role, COUNT(*) FROM employees
GROUP BY role;

-- Task 3
SELECT role, SUM(years_employed) FROM employees
GROUP BY role
HAVING role = "Engineer";

-- Task 4
SELECT director, COUNT(id) as total_movies FROM movies
GROUP BY director;

-- Task 5
SELECT director, SUM(domestic_sales + international_sales) as total_earned 
FROM movies
    INNER JOIN boxoffice
        ON movies.id = boxoffice.movie_id
GROUP BY director;

-- Task 6
INSERT INTO movies VALUES (4, "Toy Story 4", "BlaBla", 2004, 70);

-- Task 7
INSERT INTO boxoffice VALUES (4, 8.7, 340000000, 270000000);

-- Task 8
UPDATE movies
SET director = "John Lasseter"
WHERE id = 2;

-- Task 9
UPDATE movies
SET year = 1999
WHERE id = 3;

-- Task 10
UPDATE movies
SET title = "Toy Story 3", director = "Lee Unkrich"
WHERE id = 11;

-- Task 11
DELETE FROM movies
where year < 2005;

-- Task 12
DELETE FROM movies
where director = "Andrew Stanton";