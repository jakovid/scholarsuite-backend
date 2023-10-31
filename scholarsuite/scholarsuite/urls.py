from django.contrib import admin
from django.urls import path
from .views import CustomTokenObtainPairView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
]
