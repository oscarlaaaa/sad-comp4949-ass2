# pages/urls.py
from django.urls import path
from .views import home, predict, predictPost, report, results

urlpatterns = [
    path('', home, name='home'),
    path('predict/', predict, name='predict'),
    path('predictPost/', predictPost, name='predictPost'),
    path('report/', report, name='report'),
    path('results/<str:predator>/<str:aquatic>/<str:hair>/<str:milk>/<str:classtype>/<str:eggs>/<str:air>/', results, name='results'),
]