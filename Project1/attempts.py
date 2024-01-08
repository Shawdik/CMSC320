import sqlite3
import pandas as pd

#
conn = sqlite3.connect("movies.sqlite")
#query='select movies.director_id, directors.name, avg(movies.Budget) from movies inner join directors on directors.name=movies.director_id group by movies.director_id order by avg(movies.Budget) desc' # average budget for each director
#query = 'select convert(integer,avg(Budget)), name from (select movies.director_id, movies.Budget, directors.name from movies inner join directors on movies.director_id=directors.id) group by director_id order by avg(Budget) desc'
query = 'select movies.director_id, directors.name, avg(movies.budget) from movies inner join directors on directors.id=movies.director_id group by director_id order by avg(budget) desc limit 5'

df = pd.read_sql(query, conn)
print(df.head(20))