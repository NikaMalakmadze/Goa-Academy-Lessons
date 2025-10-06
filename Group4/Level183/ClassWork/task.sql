-- Task 1
CREATE TABLE IF NOT EXISTS Database (
    name TEXT,
    version FLOAT,
    download_count INTEGER
);

-- Task 2
ALTER TABLE Movies
  ADD COLUMN Aspect_ratio FLOAT DEFAULT 2.39;

-- Task 3
ALTER TABLE Movies
  ADD COLUMN Language TEXT DEFAULT "English";

-- Task 4
DROP TABLE Movies;

-- Task 5
DROP TABLE BoxOffice;