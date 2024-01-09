from django.urls import path, include
from django.conf import settings
from . import views
from django.conf.urls.static import static

urlpatterns = [
        path('', views.weather, name = 'weather'),
        path('search/', views.SearchResultsView.as_view(), name = 'search_results'),
        path('details/<int:id>', views.details, name = 'details'),
        ]

