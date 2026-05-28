CREATE TABLE books (
  id INTEGER,
  title TEXT,
  author TEXT
);
-- Do not modify above this line --

ALTER TABLE books 
    ADD COLUMN age INTEGER;

ALTER TABLE books
    RENAME COLUMN id TO isbn;

ALTER TABLE books
    DROP COLUMN author;

-- ALTER TABLE published_year RENAME COLUMN id TO _id INTEGER;








-- Do not modify below this line --
SELECT column_name, data_type, column_default
FROM information_schema.columns
WHERE table_name = 'books'
ORDER BY column_name;
