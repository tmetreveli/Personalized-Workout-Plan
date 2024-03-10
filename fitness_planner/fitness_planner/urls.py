"""iproxy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.contrib import admin
from .views import *

from user import views

schema_view = get_schema_view(
    openapi.Info(
        title="Fitness Tracker",
        default_version='v1',
        description="APIs to enable fitness tracking and enable workour plan creation",
    ),
    public=True
)

urlpatterns = [

    path('admin/', admin.site.urls),
    path('api/login/', views.LoginAPIView.as_view(), name='login'),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('api/exercise/', ExerciseListView.as_view(), name='exercise-list'),
    path('api/exercise/<int:pk>/', ExerciseDetailView.as_view(), name='exercise-detail'),

    path('api/weight_tracking/', WorkoutPlanExerciseListView.as_view(), name='exercise-list'),
    path('api/weight_tracking/<int:pk>/', WorkoutPlanExerciseDetailView.as_view(), name='exercise-detail'),

    path('api/workout_plan/', WorkoutPlanListView.as_view(), name='exercise-list'),
    path('api/workout_plan/<int:pk>/', WorkoutPlanDetailView.as_view(), name='exercise-detail'),

    path('api/workout_plan/', WeightTrackingListView.as_view(), name='exercise-list'),
    path('api/workout_plan/<int:pk>/', WeightTrackingDetailView.as_view(), name='exercise-detail'),
    path('api/create_user/', UserListView.as_view(), name = "create_user")
]
