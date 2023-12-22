import psycopg2
from datetime import datetime
import csv

username = 'postgres'
password = '12345'
database = 'LAB5'

import_rage = 250

csv_file_path = "imdb_top250_movies.csv"

def main():
    conn = psycopg2.connect(user=username, password=password, dbname=database)
    cursor = conn.cursor()

    with open(csv_file_path, 'r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)

        id = 0
        for row in csv_reader:
            id += 1
            film_id,Num,Title,Year,Released,Runtime,Genre,Director,Writer,Actors,Plot,Language,Country,Awards,Metascore,imdbRating,imdbVotes,imdbID,Type,DVD,BoxOffice,Production,Website = row
            Runtime = int(Runtime.split()[0])



            if Released == "":
                Release = f"{Year} Jan 01"
            else:
                Release = Released.split()[2] + " " + Released.split()[1] + " " + Released.split()[0]


            release = datetime.strptime(Release, "%Y %b %d")

            release_d = release.strftime("%Y-%m-%d")

            cursor.execute("insert into director (birthday, film_count, country, career, director_id, name) VALUES (%s, %s, %s, %s, %s, %s)",
                           (datetime.now().date(), -1, Country, datetime.now().date(), id, Director))

            cursor.execute("insert into film (runtime, publish_date, film_id, film_name, imdb_rating, director_id) values (%s, %s, %s, %s, %s, %s) returning film_id, director_id",
                           (Runtime, release_d, film_id, Title, imdbRating, id))


            if "," in Genre:
                genres = {Genre.strip() for Genre in Genre.split(',')}
            else:
                genres = {Genre.strip()}
            for g in genres:
                cursor.execute("insert into genre (genre, film_id) values (%s, %s)", (g, film_id))
            if id == import_rage:
                break

    conn.commit()

    cursor.close()
    conn.close()

def clear_tables():
    conn = psycopg2.connect(user=username, password=password, dbname=database)
    cursor = conn.cursor()

    cursor.execute("delete from genre")
    cursor.execute("delete from film")
    cursor.execute("delete from director")

    conn.commit()

    cursor.close()
    conn.close()

clear_tables()
main()