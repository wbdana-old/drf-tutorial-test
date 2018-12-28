# drf-tutorial

```py
virtualenv env
source env/bin/activate

pip install django
pip install djangorestframework
pip install pygments

django-admin startproject tutorial
cd tutorial

python manage.py startapp snippets

# Create Snippet model

python manage.py makemigrations snippets
python manage.py migrate
```