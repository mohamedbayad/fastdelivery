from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("inscription/", views.register, name="register"),
    path("connexion/", views.userLogin, name="connexion"),
    path("logout/", views.userLogout, name="logout"),

    # forgot password
    path("réinitialisation-du-mot-de-passe/",
        auth_views.PasswordResetView.as_view(
            template_name="registration/password_reset_form.html"),
        name="password_reset"),
    path("réinitialisation-du-mot-de-passe/effectuée/",
        auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path("effectuée/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path("réinitialisation/effectuée/",
        auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]
