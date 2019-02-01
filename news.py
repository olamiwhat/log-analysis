
#!/usr/bin/env python3

import psycopg2


DBNAME = "news"


def top3_articles():
	'''Returns the most popular 3 articles'''
	db_conn = psycopg2.connect(database=DBNAME) 
	c = db_conn.cursor() 
	c.execute("""select articles.title, count(log.path) as views
		from articles, log
		where log.path = ('/article/'||articles.slug)
		group by articles.title
		order by views desc limit 3;""")
	result = c.fetchall()
	db_conn.close()
	return result


print("The most popular 3 articles of all time are: ")
print(top3_articles())


def top_authors():
	'''Returns the most popular article authors of all time'''
	db_conn = psycopg2.connect(database=DBNAME) 
	c = db_conn.cursor()
	c.execute("""select authors.name, count(log.path) as views
		from articles, authors, log
		where articles.author = authors.id
		and log.path = ('/article/'||articles.slug)
		group by authors.name
		order by views desc;""")
	result = c.fetchall()
	db_conn.close()
	return result


print("The most popular articles authors of all time are: ")
print(top_authors())


def days_more_than_one_percent_error():
	'''Returns days where vmore than 1% of requests lead to errors'''
	db_conn = psycopg2.connect(database=DBNAME) 
	c = db_conn.cursor()
	c.execute("""select to_char(time :: date, 'Month dd, yyyy') as day,
		round((cast(count(case when status !='200 OK' then 0 end) as float)/cast(count(status) as float)*100.00)::numeric, 2) as percent_error
		from log
		group by day
		having round((cast(count(case when status !='200 OK' then 0 end) as float)/cast(count(status) as float)*100.00)::numeric, 2) > 1.00;""")
	result = c.fetchall()
	db_conn.close()
	return result


print("The day(s) where more than one percent of requests lead to errors is/are: ")
print(days_more_than_one_percent_error())
