from django.urls import path
from . import views

urlpatterns = [
    path('',views.base),
    path('details/',views.details),
    path('api/', views.workout_api),
    path('cmpapi/',views.completed),
    path('add/',views.add_api),
    path('updt/<int:id>/',views.update_api),
    path('delete/<int:id>/',views.delete_api),
]