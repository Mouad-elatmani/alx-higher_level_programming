-- a script that lists all the cities of California state
-- that can be found in the database hbtn_0d_usa
SELECT id,name FROM cities where cities.id = (SELECT id from states where name ='California') ORDER by id ASC;
