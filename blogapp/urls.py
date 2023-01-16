from django.urls import path
from . import views
app_name="blog"

urlpatterns = [
    path('',views.index,name="index"),
    path('components',views.components, name="components"),
    path ('no',views.no, name="no"),
    path('single',views.single, name="single"),
]
