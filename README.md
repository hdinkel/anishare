# anishare
## Webservice to share animals to minimize animal usage

This django app is meant to be used by research institutes that want to share research animals. 
By sharing animals within the institute, less animals in total have to be sacrificed for research.


## Installation
Install django and other dependancies (We recommend using a virtual environment for this):

    virtualenv -p python3 .
    source bin/activate
    pip install -r requirements.txt

##  First time setup

First, in the folder ``anishare``, copy the file ``local_settings.py.template``
to ``local_settings.py`` and fill it in. If you want to use LDAP, comment in
the respective lines. Most importantly, you should configure the following lines:

    EMAIL_HOST = ''
    SECRET_KEY = ''
    ALLOWED_HOSTS = ['127.0.0.1', ]

Then, you can run migrations:

    python manage.py migrate

This will create the sqlite database ``db.sqlite3`` containing all the models as defined in ``models.py``.
Now create a superuser:

    python manage.py createsuperuser

Now you are able to login to the admin interface, but first run the dev server:

    python manage.py runserver

This will listen on ``http://localhost:8000``, so browse to the admin page 
``http://localhost:8000/admin`` and you should see this after login:

![empty admin](doc/img/admin_empty.png "Empty Admin")


After adding several animals, the main (index) view should look like this:
![index view](doc/img/anishare_index_view.png "Index View")

##  Running Tests
Tests reside in ``animals/tests.py``.
You can invoke the django tests like so:

    python manage.py test
