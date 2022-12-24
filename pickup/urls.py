from django.urls import path
from . import views

urlpatterns = [
    path("créer-nouveau-bon-de-ramassage", views.pickedup, name="pickup"),
    path("bon-de-ramassage-reçu", views.received, name="collection-voucher-received"),
    path("bon-de-ramassage-non-reçu", views.no_received, name="collection-voucher-no-received"),
    path("supprimer-reçu/<str:id>", views.no_received_del, name="delet_receive"),
    path("étiquettes/<str:id>", views.savePdfLb, name="labels"),
    path("bon-de-ramassage-pdf/<str:pk>", views.pdfPickeup, name="pickedup_pdf"),
]