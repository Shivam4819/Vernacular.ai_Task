from django.contrib import admin
from django.urls import path
from .task import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/validate_value', views.validate_finite_values_entity_api, name="validate_finite_values_entity_api"),   
    path('api/validate_numeric', views.validate_numeric_entity_api, name="validate_numeric_entity_api"),
]
