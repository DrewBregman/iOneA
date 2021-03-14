from django.urls import path
from .views import SearchResultsView, SearchPageView

urlpatterns = [
   path('results/', SearchResultsView.as_view(), name='search_results'),
   path('search/', SearchPageView.as_view(), name='search'),   


]