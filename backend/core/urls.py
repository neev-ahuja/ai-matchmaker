"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView # Import refresh view
from accounts.views import MyTokenObtainPairView # Import custom login view

urlpatterns = [
    path('admin/', admin.site.urls),

    # Authentication URLs from simple_jwt (Login and Refresh)
    # Use our custom view for login to potentially add more claims
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Include URLs from our 'accounts' app
    path('api/accounts/', include('accounts.urls')), # Prefix account related URLs
    path('api/aimodels/', include('aimodels.urls')), 
]
