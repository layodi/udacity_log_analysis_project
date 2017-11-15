# Udacity-Log-Analysis-Project

### Overview
>This is an internal reporting tool that uses information from a database to discover what kind of articles the site's readers like. The database contains newspaper articles, authors, as well as the web server log for the site. The log has a database row for each time a reader loaded a web page. The database contains thre tables: **authors** table, **articles** table and **log** table.

### Features
* Retrieves the most popular three articles of all time from the database.
* Retrieves the most popular article authors of all time from the database.
* Retrieves the days on which more than 1% of requests lead to errors.

### Dependencies | Requirements
* [Python3](https://www.python.org/)
* [Vagrant](https://www.vagrantup.com/)
* [VirtualBox](https://www.virtualbox.org/)

### Installation and Setup
* Install [Vagrant](https://www.vagrantup.com/) and [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
* Clone the repository to your local machine:
  ```
  git clone https://github.com/visheshbanga/Log-Analysis-Udacity-Project
  ```  
* Download this [file](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) and unzip it to retrieve **newsdata.sql**

* Start up the virtual machine inside the vagrant directory by running:
  ```
  vagrant up
  ```
* Log in to the virtual machine by running:
  ```
  vagrant ssh
  ```
* Access shared files by running:
  ```
  cd /vagrant
  ```
* Load the data into the databse by running:
  ```
  psql -d news -f newsdata.sql
  ```
* Connect to the database by running:
  ```
  psql -d newsdata
  ```

* Create views by running the following queries on the terminal while connected to the **news** database:
  - articles_view
    ```
    create view articles_view as select title, count(title) as views from articles,log where log.path like concat('%', articles.slug) group by articles.title order by views desc;
    ```
  - authors_view
    ```
    create view authors_view as select authors.name, count(articles.author) as views from articles, log, authors where log.path = concat('/article/',articles.slug) and articles.author = authors.id
    group by authors.name order by views desc;
    ```
  - log_view
    ```
    create view log_view as select date(time),round(100.0*sum(case log.status when '200 OK' then 0 else 1 end)/count(log.status),2) as "error percentage" from log group by date(time) order by "error percentage" desc;
    ```
### Running the Application
To run the application:

```python newsdata.py```
