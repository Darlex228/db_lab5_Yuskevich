INSERT INTO director (director_id, name, birthday, country, career, film_count)
VALUES
	(0, 'Frank Darabont', '1959.01.28', 'USA', '1981.01.01', 25),
	(1, 'Francis Ford Coppola', '1939.04.07', 'USA', '1962.01.01', 76),
	(2, 'Christopher Nolan', '1970.07.30', 'Great Britain', '1998.01.01', 12),
	(3, 'Sidney Lumet', '1924.06.25', 'USA', '1930.01.01', 43),
	(4, 'Steven Spielberg', '1946.12.18', 'USA', '1959.01.01', 58),
	(5, 'Peter Jackson', '1961.10.31', 'New Zealand', '1987.01.01', 27),
	(6, 'Quentin Tarantino', '1963.03.27', 'USA', '1983.01.01', 15),
	(7, 'David Fincher', '1962.08.28', 'USA', '1984.01.01', 15);
	
INSERT INTO film (film_id, film_name, publish_date, runtime, imdb_rating, director_id)
VALUES
	(0, 'The Shawshank Redemption', '1994.10.14', 142, 9.3, 0),
	(1, 'The Godfather', '1972.03.24', 175, 9.2, 1),
	(2, 'The Godfather: Part II', '1974.12.20', 202, 9.0, 1),
	(3, 'The Dark Knight', '2008.07.18', 152, 9.0, 2),
	(4, '12 Angry Men', '1957.04.01', 96, 8.9, 3),
	(5, 'Schindler s List', '1994.02.04', 195, 8.9, 4),
	(6, 'The Lord of the Rings: The Return of the King', '2003.12.17', 201, 8.9, 5),
	(7, 'Pulp Fiction', '1994.10.14', 154, 8.9, 6),
	(8, 'Fight Club', '1999.10.15', 139, 8.8, 7);
	
INSERT INTO genre (film_id, genre)
VALUES
	(0, 'Crime'),
	(0, 'Drama'),
	(1, 'Crime'),
	(1, 'Drama'),
	(2, 'Crime'),
	(2, 'Drama'),
	(3, 'Action'),
	(3, 'Crime'),
	(3, 'Drama'),
	(4, 'Crime'),
	(4, 'Drama'),
	(5, 'Biography'),
	(5, 'Drama'),
	(5, 'History'),
	(6, 'Adventure'),
	(6, 'Drama'),
	(6, 'Fantasy'),
	(7, 'Crime'),
	(7, 'Drama'),
	(8, 'Drama')