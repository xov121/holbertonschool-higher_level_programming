-- List genres and the number of shows linked to each
SELECT genres.name AS genre, COUNT(show_genres.show_id) AS number_of_shows
FROM genres
LEFT JOIN show_genres ON genres.id = show_genres.genre_id
GROUP BY genres.name
ORDER BY number_of_shows DESC, genre ASC;
