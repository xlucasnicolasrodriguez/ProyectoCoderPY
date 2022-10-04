from django.urls import path
from django.contrib import admin
from AppCoder.views import familia

urlpatterns = [
    path("familia/", familia),
    path('admin/', admin.site.urls),
]