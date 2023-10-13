from django.urls import path
from .views import registration_view,CustomTokenObtainPairView,profile_view

urlpatterns = [
    path('reg/',registration_view,name='registration'),
    path('log/',CustomTokenObtainPairView.as_view(),name="LogIn"),
    path('view/',profile_view,name='profile_view')
]
