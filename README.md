# django-mash

First I had **MariaDB** installed on my machine. It is drop in replacement for **MySQL**, so the packages relating to database connection will still be the **MySQL** ones.

The python version used was **python3.10.11** as a venv. The exact packages installed on this system by order of importance were `pip` == 23.1.1, `wheel` == 0.40.0, `requests` == 2.31.0, `urllib3` == 2.0.2, `django` == 4.2.1, `djangorestframework` == 3.14.0, `mysqlclient` == 2.1.1. The packages to reproduce might not have to be same minor release, eg `requests` 2.31.X.

The database "crud_app_db" was created separately using MariaDB as root user. With the root user I create a user "ADjangoAdmin" with a password "1test5". Privileges to the database "crud_app_db" were granted to the user "ADjangoAdmin".

I created superuser with the username "AnAdmin", an email adress of "anadmin@example.com" and a password of "23test56=-".

For the database table `CRUD_APP_client_info` I implemented the query as:
CREATE TABLE `CRUD_APP_client_info` (`client_id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `id_number` varchar(13) NOT NULL UNIQUE, `first_name` varchar(50) NOT NULL, `last_name` varchar(50) NOT NULL, `date_of_birth` datetime(6) NOT NULL, `title` varchar(4) NOT NULL, `phone_number` varchar(11) NOT NULL, `email` varchar(254) NOT NULL)

_Note_ There is a db.mysql file in the root of the repository though empty. I t is symbolic, the database used here is in the system, not the source tree.
