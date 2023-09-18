if django note installed, install it with <br>
pip install django
<br>
create new django project with <br>
django-admin startproject django_ecommerce_project
<br>
navigate to project folder and create django app using this command <br>
python manage.py startapp store
<br>
add the store app in installed apps in project/settings.py file <br>
create model in app/models.py and then register it in app/admin.py <br>
then make and apply migration to create tables using commands makemigrations and migrate <br>
then add products by creating admin with this command createsuperuser <br>
then create views in app/views.py<br>
then create templates inside app/templates/app/ <br>
then define url patterns inside app/urls.py file <br>
then include current app url in the project/urls.py file <br>
then run server with runserver command <br>
<br>
<br>
CRUD
<br>
create form of product model to handle form data in app/forms.py
<br>
create views for insert, update, delete in the views.py
<br>
create templates for create, update, delete and product form in templates<br>
add new url patterns<br>
add edit, update and insert product buttons in products list page