![example workflow](https://github.com/lijuli/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

Welcome to the li-mdb wiki!
This is an API for movie reviews.

### Usage

Start a project like this:

Create and activate virtual environment: \
`python -m venv venv && source venv/bin/activate`

Now make sure you have everything installed in your virtualenv: \
`pip install -r requirements.txt`

Migrate the database:\
`python manage.py makemigrations && python manage.py migrate`

Now you are all set and can run the project!\
`python manage.py runserver`

### Technologies:
* Python
* Django
* Django REST Framework
* Simple JWT

### API:
API documentation: \
http://localhost/redoc/

Admin: \
http://localhost/admin/

Access resources:\
http://localhost/api/v1/auth/email/ - get confirmation_code \
http://localhost/api/v1/auth/token/ - get token 
