from django.contrib import admin
from django.urls import path
from mainpage.views import index_view, about_view, contact_view
urlpatterns = [
    # path('home' ,index_view),
    path('' ,index_view),
    path('about' ,about_view),
    path('contact' ,contact_view)
]