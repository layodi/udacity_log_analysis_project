#!/usr/bin/env python3

import psycopg2

DBNAME = "news"


def get_popular_articles():
    """Return the most popular three articles of all time"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select * from articles_view limit 3")
    articles = c.fetchall()
    db.close()
    print "1. What are the most popular three articles of all time?\n"
    for i in range(0, len(articles), 1):
        article_title = articles[i][0]
        number_of_views = str(articles[i][1])
        print "\"" + article_title + "\" - " + number_of_views + " views"


def get_popular_authors():
    """Return the most popular authors of all time"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select * from authors_view")
    authors = c.fetchall()
    db.close()
    print "\n2. What are the most popular authors of all time?\n"
    for i in range(0, len(authors), 1):
        authors_name = authors[i][0]
        number_of_views = str(authors[i][1])
        print "\"" + authors_name + "\" - " + number_of_views + " views"


def get_log_errors():
    """Return the most popular authors of all time"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select * from log_view where errorpercentage > 1")
    errors = c.fetchall()
    db.close()
    print "\n3. On which days did more than 1% of requests lead to errors?\n"
    for i in range(0, len(errors), 1):
        date_recorded = str(errors[i][0].strftime("%b %d, %Y"))
        number_of_errors = str(int(errors[i][1]))
        print date_recorded + " - " + number_of_errors + "% errors"


get_popular_articles()
get_popular_authors()
get_log_errors()
