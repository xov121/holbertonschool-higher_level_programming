-- List genres of the show 'Dexter'
SELECT genres.name
FROM genres
JOIN show_genres ON genres.id = show_genres.genre_id
JOIN tv_shows ON tv_shows.id = show_genres.show_id
WHERE tv_shows.title = 'Dexter'
ORDER BY genres.name ASC;
