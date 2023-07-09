from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboardAdmin, name="dashboard-admin"),
    # show users 
    path(r"user/?P<pk>\d+/", views.viewProfileUser, name="view_user"),
    path(r"user/?P<pk>\d+?:/invoies-pdf/?P<npk>\d+?", views.pdfInvoicesAdmin, name="pdf_invoices"),
    path(r"user/?P<pk>\d+?:/lables-pdf/?P<npk>\d+?", views.savePdfLb, name="pdf_lables"),
    # path(r"user/?P<pk>\d+?:/invoies-pdf/?P<npk>\d+?", views.pdfInvoicesAdmin, name="pdf_invoices"),
    path(r"user/?P<pk>\d+?:/received/?P<npk>\d+?/", views.veiwReceive, name="view_received"),
    path(r"user/?P<pk>\d+?:/package/?P<npk>\d+?/", views.veiwPackages, name="view_package"),
    path(r"user/?P<pk>\d+?:/refund/?P<npk>\d+?/", views.viewRefund, name="view_refund"),
    path(r"user/?P<pk>\d+?:/exchange/?P<npk>\d+?/", views.viewExchange, name="view_exchange"),

    # add packages
    path(r"admin-delivery/?P<pk>\d+/add-packages/", views.addPackages, name="add_packages"),
    
    # show admin delivery 
    path(r"admin-delivery/?P<pk>\d+/", views.viewAdminMenDelivery, name="view_admin"),
    path(r"admin-delivery/?P<pk>\d+/package/?P<npk>\d+?", views.veiwPackages, name="edite_package"),
    path(r"admin-delivery/?P<pk>\d+/add/", views.addManDelivery, name="add_delivery"),

    # show man delivery 
    path(r"man-delivery/?P<pk>\d+?", views.viewManDelivery, name="view_delivery"),
    path(r"man-delivery/?P<pk>\d+?/package/?P<npk>\d+?", views.veiwPackages, name="edite_package_in_delivery"),

    # show pages
    path(r"parcel-box", views.boxPackages, name="parcel_box"),
    path(r"tracking", views.tracking, name="tracking_admin"),
    path(r"customers", views.customers, name="customers"),
    path(r"admins-delivery", views.adminDelivery, name="admins_delivery"),
    path(r"packages", views.package, name="packages_admin"),
    path(r"exchanges", views.exchange, name="exchanges_admin"),
    path(r"refunds", views.refundPage, name="refunds_admin"),
    path(r"invoices", views.invoice, name="invoices_admin"),
    path(r"support", views.support, name="support_admin"),
    path(r"settings/", views.settings, name="settings"),

    path(r"add-city", views.addCity, name="addCity"),
    path(r"edit-city/?P<pk>\d+/", views.editCity, name="editCity"),
    path(r"delete-city/?P<pk>\d+/", views.deleteCity, name="deleteCity"),

    path(r"add-update", views.addUpdate, name="addUpdate"),
    path(r"edit-update/?P<pk>\d+/", views.editUpdate, name="editUpdate"),
    path(r"delete-update/?P<pk>\d+/", views.deleteUpdate, name="deleteUpdate"),


]