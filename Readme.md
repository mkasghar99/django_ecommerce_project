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
add edit, update and insert product buttons in products list page<br>
<br>
<br>
<br>
3 User Auth
<br>
django has builtin system for user authentication so no need to create user model or table and ensure that installed apps has     'django.contrib.auth',
<br>
create user registeration form and login form in forms.py after importing necessary builtin authentication modules<br>
import necessary modules in views.py<br>
create registeration view which will register new user<br>
then create regiser and login template inside new registeration directory<br>
add register and login url pattern <br>
also include django.contrib.auth.urls in urls.py of project <br>
add login and logout redirect url in settings.py <br>
then create login view too which checks user <br>
made all existing views private by placing @login_required before each view<br>
create logout button in admin template, and its view and then also define it in url pattern<br>
create a products display page for public by creating view, its template and define it in url pattern. <br>
<br>
<br>
<br>
4_Pagination
Django has builtin feature for pagination<br>
first we need to import Paginator module in views.py<br>
then we pass number of items per page and fetched products object to paginator<br>
then we pass current page number to paginator, this number is recieved from get method of page<br>
the we pass the paginator object which includes the products of current page, and info about pagination<br>
then the above information is accessed in public products template and display the pagination accordingly<br>