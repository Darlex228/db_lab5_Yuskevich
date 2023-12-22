DO $$
DECLARE
	i INT;
BEGIN
    FOR i IN 1..30 LOOP
    	INSERT INTO director (birthday, film_count, country, career, director_id, name) 
		VALUES ('1939-08-23', i + 10, 'Europe or smth', '1914-06-28', i - 1, 'Otto Eduard Leopold von Bismark');
    END LOOP;
END $$;
