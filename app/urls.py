from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage),
    path('search/',views.search),
    path('search/result/',views.result),
    path('about/',views.about),
]
