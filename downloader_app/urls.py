from django.urls import path
from downloader_app import views

urlpatterns = [
    path("", views.home, name='home'),  # The home page.
    path("linksubmit", views.download, name="download"),  # The download page.
    path("final", views.final, name="final"),  # The final download success page.
]
