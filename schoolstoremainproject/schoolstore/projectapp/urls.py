from . import views
from django .urls import path
urlpatterns=[
    path('',views.index1,name='index1'),
    path("home",views.home,name='home'),
    path("register",views.register_request,name="register"),
    path("login",views.login_request,name="login"),
    path("form",views.details,name="form"),
    path("detail",views.detail,name="detail"),
    path("logout",views.logout_request,name="logout"),
]