from django.contrib import admin
from django.urls import path, include
from PrimeraEntregaFinalApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('PrimeraEntregaFinalApp/', include('PrimeraEntregaFinalApp.urls')),
]
