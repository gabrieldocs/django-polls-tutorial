#Configurando rotas globais da aplicação 

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls), 
]
