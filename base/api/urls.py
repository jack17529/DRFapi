from django.urls import path
from . import views
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls

from rest_framework_simplejwt.views import(
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns=[
    path('', views.getRoutes),
    path('profiles', views.getAddProfiles),
    path('profiles/<str:pk>', views.getUpdateRemoveProfile),
    # path('profiles/<str:pk>/resumes/', views.addResume),
    path('profiles/<str:pk>/resumes', views.getUpdateAddResumes),

    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # POST Request
    # {
    #     "username": "superuser",
    #     "password": "superuser"
    # }

    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    # POST Request
    # {
    #     "refresh": "This field is required."
    # }

    path('docs', include_docs_urls(title='qrateAPI')),

    path('schema', get_schema_view(
        title="qrateAPI",
        description="API for qrate backend",
        version="1.0.0"
    ), name='openapi-schema'),
]