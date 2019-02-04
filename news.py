#!/usr/bin/python3
import psycopg2

DBNAME = "news"
QUERY1 = """select articles.title, count(log.path) as views
            from articles, log
            where log.path = ('/article/'||articles.slug)
            group by articles.title
            order by views desc limit 3;"""
QUERY2 = """select authors.name, count(log.path) as views
            from articles, authors, log
            where articles.author = authors.id
            and log.path = ('/article/'||articles.slug)
            group by authors.name
            order by views desc;"""
QUERY3 = """select to_char(time :: date, 'Month dd, yyyy') as day,
            round(
            (cast(count(case when status !='200 OK' then 0 end)
            as float)/
            cast(count(status) as float)*100.00)
            ::numeric, 2) as percent_error
            from log
            group by day
            having round(
            (cast(count(case when status !='200 OK' then 0 end)
            as float)/
            cast(count(status) as float)*100.00)
            ::numeric, 2) > 1.00;"""

try:
    db_conn = psycopg2.connect(database=DBNAME)
except psycopg2.Error as err:
    print("Error connecting to database")

c = db_conn.cursor()


def top3_articles():
    '''Prints the most popular 3 articles'''
    c.execute(QUERY1)
    top_articles = c.fetchall()
    print("The most popular 3 articles of all time are: ")
    for row in top_articles:
        print("*{} - {} views".format(row[0], row[1]))


top3_articles()
print("\n")


def top_authors():
    '''Prints the most popular article authors of all time'''
    c.execute(QUERY2)
    top_authors = c.fetchall()
    print("The most popular article authors of all time are: ")
    for row in top_authors:
        print("*{} - {} views".format(row[0], row[1]))


top_authors()
print("\n")


def days_more_than_one_percent_error():
    '''Prints days where more than 1% of requests lead to errors'''
    c.execute(QUERY3)
    days_error = c.fetchall()
    print("The day(s) more than 1 percent of requests led to errors is/are: ")
    for row in days_error:
        print("*{} - {} percent".format(row[0], row[1]))


days_more_than_one_percent_error()
print("\n")


db_conn.close()


print("psycopg2 connection is closed")
