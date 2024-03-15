from django.urls import path

from .views import HomeListView, AboutUsView

urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('aboutus/', AboutUsView.as_view(), name='aboutus'),
]
