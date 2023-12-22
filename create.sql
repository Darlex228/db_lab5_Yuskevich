CREATE TABLE director
(
  birthday DATE NOT NULL,
  film_count INT NOT NULL,
  country VARCHAR(100) NOT NULL,
  career DATE NOT NULL,
  director_id INT NOT NULL,
  name VARCHAR(100) NOT NULL,
  PRIMARY KEY (director_id)
);

CREATE TABLE film
(
  runtime INT NOT NULL,
  publish_date DATE NOT NULL,
  film_id INT NOT NULL,
  film_name VARCHAR(100) NOT NULL,
  imdb_rating FLOAT NOT NULL,
  director_id INT NOT NULL,
  PRIMARY KEY (film_id),
  FOREIGN KEY (director_id) REFERENCES director(director_id)
);

CREATE TABLE genre
(
  genre VARCHAR(100) NOT NULL,
  film_id INT NOT NULL,
  PRIMARY KEY (genre, film_id),
  FOREIGN KEY (film_id) REFERENCES film(film_id)
);