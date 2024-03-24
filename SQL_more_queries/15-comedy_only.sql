-- List all Comedy shows
SELECT tv_shows.title
FROM tv_shows
JOIN show_genres ON tv_shows.id = show_genres.show_id
JOIN genres ON genres.id = show_genres.genre_id
WHERE genres.name = 'Comedy'
ORDER BY tv_shows.title ASC;
