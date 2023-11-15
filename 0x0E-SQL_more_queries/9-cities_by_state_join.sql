-- a script that lists all the cities
select cities.id,cities.name, states.name FROM cities
JOIN states on cities.state_id = state.id ORDER BY cities.id
