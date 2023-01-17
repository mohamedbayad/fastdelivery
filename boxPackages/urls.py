from django.urls import path
from . import views

urlpatterns = [
    path("", views.showBoxPackages, name="box_packages"),
    path("ajouter-box/", views.addNewBox, name="add_new_box"),
    path(r"effacer-le-box/?P<pk>\d+", views.deleteBox, name="delete_box"),
    path(r"bone-box/?P<pk>\d+", views.pdfBox, name="pdf_box"),
]
