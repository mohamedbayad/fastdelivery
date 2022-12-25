from django.urls import path
from . import views

urlpatterns = [
    path("dashboard-admin/", views.dashboardAdmin, name="dashboard-admin"),
    # show users 
    path(r"dashboard-admin/user/?P<pk>\d+/", views.viewProfileUser, name="view_user"),
    path(r"dashboard-admin/user/?P<pk>\d+?:/invoies-pdf/?P<npk>\d+?", views.pdfInvoicesAdmin, name="pdf_invoices"),
    path(r"dashboard-admin/user/?P<pk>\d+?:/lables-pdf/?P<npk>\d+?", views.savePdfLb, name="pdf_lables"),
    # path(r"dashboard-admin/user/?P<pk>\d+?:/invoies-pdf/?P<npk>\d+?", views.pdfInvoicesAdmin, name="pdf_invoices"),
    path(r"dashboard-admin/user/?P<pk>\d+?:/received/?P<npk>\d+?/", views.veiwReceive, name="view_received"),
    path(r"dashboard-admin/user/?P<pk>\d+?:/package/?P<npk>\d+?/", views.veiwPackages, name="view_package"),
    path(r"dashboard-admin/user/?P<pk>\d+?:/refund/?P<npk>\d+?/", views.viewRefund, name="view_refund"),
    path(r"dashboard-admin/user/?P<pk>\d+?:/exchange/?P<npk>\d+?/", views.viewExchange, name="view_exchange"),

    # add packages
    path(r"admin-delivery/?P<pk>\d+/add-packages/", views.addPackages, name="add_packages"),
    
    # show admin delivery 
    path(r"admin-delivery/?P<pk>\d+/", views.viewAdminMenDelivery, name="view_admin"),
    path(r"admin-delivery/?P<pk>\d+/package/?P<npk>\d+?", views.veiwPackages, name="edite_package"),
    path(r"admin-delivery/?P<pk>\d+/add/", views.addManDelivery, name="add_delivery"),

    # show man delivery 
    path(r"man-delivery/?P<pk>\d+?", views.viewManDelivery, name="view_delivery"),
    path(r"man-delivery/?P<pk>\d+?/package/?P<npk>\d+?", views.veiwPackages, name="edite_package_in_delivery"),
]