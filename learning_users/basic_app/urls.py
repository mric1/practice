from django.conf.urls import url,include
from django.contrib import admin
from basic_app import views

#TEMPLATE URLS!

app_name = "basic_app"

urlpatterns = [
    url(r"^register/$",views.register,name="register"),
    url(r'^user_login/$',views.user_login,name="login"),
    url(r'^logout/$',views.user_logout,name="logout"),
    url(r'^special/',views.special,name="special"),
]
