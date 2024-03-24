-- List all shows and their associated genres, including shows without genres
SELECT tv_shows.title AS "title", genres.name AS "genre"
FROM tv_shows
LEFT JOIN show_genres ON tv_shows.id = show_genres.show_id
LEFT JOIN genres ON show_genres.genre_id = genres.id
ORDER BY tv_shows.title, genres.name;
