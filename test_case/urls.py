"""test_case URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from django.urls import path
from user.views import OwnerCreateView, UserListView, CreateCompanyView, EmployeeCreateView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from django.contrib import admin
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

urlpatterns = [
    # Login user
    path('api/v1/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # Owner sign-up
    path('api/v1/owner/sign-up/', OwnerCreateView.as_view(), name='owner_sign_up'),
    # Create company after login
    path('api/v1/create-company/', CreateCompanyView.as_view(), name='create_company'),
    # Register new employee (only owner of company has access to it)
    path('api/v1/employee/register/', EmployeeCreateView.as_view(), name='employee_register'),
    # Show list of user
    path('api/v1/list-of-users/', UserListView.as_view(), name='list_of_user'),
    # Django admin
    path('admin/', admin.site.urls),

    # OpenAPI scheme
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/schema/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc",),
    path("api/schema/swagger-ui/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),

    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
]
