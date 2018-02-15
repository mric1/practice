from django.conf.urls import url, include
from django.contrib import admin
from basic_app import views

#TEMPLAT TAGGING
app_name = "basic_app"

urlpatterns = [
    url(r"^relative/$",views.relative,name="relative"),
    url(r"^other/$",views.other,name="other")
]
