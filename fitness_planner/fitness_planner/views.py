import json
import os

from django.http import HttpRequest, JsonResponse
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.views.decorators.http import require_http_methods

from .models import WorkoutPlanExercise, WorkoutPlan, Exercise, WeightTracking
from .serializers import WorkoutPlanSerializer, ExerciseSerializer, \
    WorkoutPlanExerciseSerializer, WeightTrackingSerializer, UserSerializer


class UserListView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Create your views here.
class WorkoutPlanListView(generics.ListCreateAPIView):
    queryset = WorkoutPlan.objects.all()
    serializer_class = WorkoutPlanSerializer


class WorkoutPlanDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = WorkoutPlan.objects.all()
    serializer_class = WorkoutPlanSerializer


class ExerciseListView(generics.ListCreateAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    permission_classes = [IsAuthenticated]


class ExerciseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer


class WorkoutPlanExerciseListView(generics.ListCreateAPIView):
    queryset = WorkoutPlanExercise.objects.all()
    serializer_class = WorkoutPlanExerciseSerializer


class WorkoutPlanExerciseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = WorkoutPlan.objects.all()
    serializer_class = WorkoutPlanExerciseSerializer


class WeightTrackingListView(generics.ListCreateAPIView):
    queryset = WeightTracking.objects.all()
    serializer_class = WeightTrackingSerializer


class WeightTrackingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = WeightTracking.objects.all()
    serializer_class = WeightTrackingSerializer


@require_http_methods(["POST"])
def create_sample_exercises(request):
    # try:
    # Specify the path to your JSON file
    file_path = os.path.join(os.path.dirname(__file__), 'sample_exercises.json')

    # Read the JSON file
    with open(file_path, 'r') as file:
        data = json.load(file)

    exercise_data = data.get("exercises")

    for exercise in exercise_data:
        Exercise.objects.create(
            name=exercise['name'],
            description=exercise['description'],
            execution_steps=exercise['execution_steps'],
            target_muscles=exercise['target_muscles']
        )

    return JsonResponse({"success": True})  # Corrected the JsonResponse syntax
# except Exception as e:
#     return JsonResponse({"error": str(e)})  # Return error message in JSON format