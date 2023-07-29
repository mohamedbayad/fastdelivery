"""delivry URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.views.generic.base import TemplateView

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
]


urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('robots.txt/', TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
    path("", include("main.urls")),
    path("dashboard/", include("dashboard.urls")),
    path("account/", include("account.urls")),
    path("colis/", include("packages.urls")),
    path("ramassage/", include("pickup.urls")),
    path("factures/", include("invoices.urls")),
    path("suivi-colis/", include("tracking.urls")),
    path("les-bons-de-commandes/", include("boxPackages.urls")),
    path("dashboard/nous-contacter/", include("contactUs.urls")),
    path("dashboard-admin/", include("adminManager.urls")),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# handler404 = "helpers.views.page_404"
