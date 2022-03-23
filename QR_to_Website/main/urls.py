from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path
from .views import *
from django.conf.urls.static import static
urlpatterns = [
    path('', home),
    path('<str:pk>/', doctor_page)
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

