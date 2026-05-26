from django.urls import path
from . import views


urlpatterns = [
    path('',views.home),
    path('register/',views.signup_api),
    path('login/',views.login_api),
    path('profile/',views.profile),
    path('logout/',views.logout_api),
    path('profile/',views.profile),
    path('staff/',views.staff_dashboard),
]