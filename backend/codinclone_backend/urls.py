from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

def home(request):
    return HttpResponse("Welcome to CodinClone API!")

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),
    path('api/problems/', include('problems.urls')),
    path('api/submissions/', include('submissions.urls')),
     path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # login to get token
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), # refresh token
]
