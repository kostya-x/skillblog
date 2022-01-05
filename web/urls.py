from django.urls import path
from web import views


urlpatterns = [
    path('', views.index),
    path('contacts', views.contacts),
    path('publications', views.publications),
    path('publication/<int:number>', views.publication),
    path('publish', views.publish),
]
