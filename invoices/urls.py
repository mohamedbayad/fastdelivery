from django.urls import path
from . import views

urlpatterns = [
    path("colis-non-facturé/", views.parcel_not_inv, name="not_invoices"),
    path("colis-facturé/", views.parcel_inv, name="invoices"),
    path("colis-facturé/<str:id>", views.parcel_inv_packages,
        name="invoices_packages"),
    path("facturé/<str:pk>", views.pdfInvoices, name="factur_pdf"),
]
