

-- returns most popular three articles of all time
select articles.title, count(log.path) as views 
from articles, log
where log.path = ('/article/'||articles.slug)
group by articles.title
order by views desc
limit 3;


--created view to select whatever number of top articles
create view top_articles as select articles.title, count(log.path) as views
from articles, log
where log.path = ('/article/'||articles.slug)
group by articles.title
order by views desc;

select * from top_articles limit 3;

-- returns most popular article authors of all time
select authors.name, count(log.path) as views
from articles, authors, log
where articles.author = authors.id
and log.path = ('/article/'||articles.slug)
group by authors.name
order by views desc;

-- returns days where more than 1% of requests lead to errors
create view error_per_day as
select to_char(time :: date, 'Month dd, yyyy') as day,
round((cast(count(case when status !='200 OK' then 0 end) as float)/cast(count(status) as float)*100.00)::numeric, 2) as percent_error
from log
group by day
having round((cast(count(case when status !='200 OK' then 0 end) as float)/cast(count(status) as float)*100.00)::numeric, 2) > 1.00;