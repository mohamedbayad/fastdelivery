from django.urls import path
from . import views

urlpatterns = [
    path("ajouter-nouveau-colis/", views.newPackage, name="new-packages"),
    path("colis-en-attente-de-ramassage/", views.waitingPickup, name="packages-waiting-for-pickup"),
    # path("suivi-des-colis/", views.parcelTracking, name="parcel-tracking"),
    # path("statistiques_des_colis/", views.staticColis, name="static-package"),
    path("colis-ramasse/", views.packagePickedUp, name="packages-pickup"),
    path("edite/<str:id>/", views.updatePackage, name="update"),
    path("delete/<str:id>/", views.deletPackage, name="remove"),
    path("demande-de-remboursement/<str:id>", views.refundRequest, name="refund"),
    path("demande-d'echange/<str:id>", views.exchangeRequest, name="exchange"),
    path("changement-d'adresse/<str:id>/", views.change_address, name="exchange_address"),
]