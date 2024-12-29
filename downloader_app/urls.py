from django.urls import path
from downloader_app import views

urlpatterns = [
    path("",views.home, name =  'home'),
    #path("linksubmit",views.submit, name ="submit"),
    path("linksubmit",views.download, name = "download"),
    path("",views.final, name = "final"),
]
