# MyBlog2
a new version from [MyBlog](https://github.com/petersobhi/MyBlog) without commenting and liking systems but using Django with web sockets.

##### it  can run online through [AWS](http://18.194.226.178/) or locally.

### Requirements to run locally:

* [Python 3.x](https://www.python.org/)
* [Django 1.11](https://www.djangoproject.com/)
* [MySQL](https://www.mysql.com/)
* [Django Channels](https://channels.readthedocs.io/en/stable/)
* [Django ASGI Redis](https://github.com/django/asgi_redis)
* [Django Daphne](https://github.com/django/daphne)


### Installation

- clone or download the repo:
    ```sh
    $ git clone https://github.com/petersobhi/MyBlog2.git
    ```
  

- create a virtual environment with `python3` and activate it
    ```sh
    $ virtualenv {location} --python=python3
    $ source {location}/bin/activate
    ```
- upgrade pip and install requirements while virtual environment is activated:
    ```sh
    $ pip install --upgrade pip
    $ pip install -r {repo}/requirements.txt
    ```
  
- configure the database:
    - install MySQL
        ```sh
        $ sudo apt-get update
        $ sudo apt-get install mysql-server
        $ mysql_secure_installation
        ```
    
    - create a database in MySQL
    - edit `DATABASES` dict in `settings.py` with the MySQL username, password and database name
    - make the migrations:
        ```sh
        $ python manage.py makemigrations
        $ python manage.py migrate
        ```
- now you have to run two processes concurrently
    ```sh
    $ python manage.py runworker
    ```
    and:
    ```
    $ daphne -b {{ip_address}} -p {{port_number}} {{project_namee}}.asgi:channel_layer
    ```
    you can use [Supervisor](http://supervisord.org/installing.html) to do so.
    note that you can configure Supervisor to run the `runworker` task mare than once which is recommended.

