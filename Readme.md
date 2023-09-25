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
5 cart
<br>
create following utility functions in store/utils.py file, and import these functions views.py <br>
1. add to cart, it will add given product in session
2. Remove from cart, it will remove given product from session
3. Cart summary
<br>
create following three views <br>
1. add to cart: this view will be called from form button on products page, which will send product id to this view and this view will call the util func to add item to cart <br>
2. remove from cart: as above <br>
3. cart view: this view call cart_summary utils func to get cart items and send it to cart.html template to display items<br>
add url patterns for above three views.
<br>
<br>
<br>