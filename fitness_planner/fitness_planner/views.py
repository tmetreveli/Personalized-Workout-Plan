import json
import os
from rest_framework.views import APIView
from django.http import HttpRequest, JsonResponse
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.views.decorators.http import require_http_methods

from .models import WorkoutPlanExercise, WorkoutPlan, Exercise, WeightTracking, FitnessGoal
from .serializers import WorkoutPlanSerializer, ExerciseSerializer, \
    WorkoutPlanExerciseSerializer, WeightTrackingSerializer, UserSerializer, FitnessGoalSerializer

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import WorkoutPlan, WorkoutPlanExercise, Exercise
from .serializers import WorkoutPlanSerializer, WorkoutPlanExerciseSerializer

class UserListView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
 



class WorkoutPlanListView(generics.ListCreateAPIView):
    queryset = WorkoutPlan.objects.all()
    serializer_class = WorkoutPlanSerializer
    permission_classes = [IsAuthenticated]


class WorkoutPlanDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = WorkoutPlan.objects.all()
    serializer_class = WorkoutPlanSerializer
    permission_classes = [IsAuthenticated]


class ExerciseListView(generics.ListCreateAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    permission_classes = [IsAuthenticated]


class ExerciseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    permission_classes = [IsAuthenticated]


class WorkoutPlanExerciseListView(generics.ListCreateAPIView):
    queryset = WorkoutPlanExercise.objects.all()
    serializer_class = WorkoutPlanExerciseSerializer
    permission_classes = [IsAuthenticated]


class WorkoutPlanExerciseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = WorkoutPlan.objects.all()
    serializer_class = WorkoutPlanExerciseSerializer
    permission_classes = [IsAuthenticated]


class WeightTrackingListView(generics.ListCreateAPIView):
    queryset = WeightTracking.objects.all()
    serializer_class = WeightTrackingSerializer
    permission_classes = [IsAuthenticated]


class WeightTrackingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = WeightTracking.objects.all()
    serializer_class = WeightTrackingSerializer
    permission_classes = [IsAuthenticated]


@require_http_methods(["POST"])
def create_sample_exercises(request):
    try:
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
    except Exception as e:
        return JsonResponse({"error": str(e)})  # Return error message in JSON format
    

class FitnessGoalListView(generics.ListCreateAPIView):
    queryset = FitnessGoal.objects.all()
    serializer_class = FitnessGoalSerializer
    permission_classes = [IsAuthenticated]


class FitnessGoalDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FitnessGoal.objects.all()
    serializer_class = FitnessGoalSerializer
    permission_classes = [IsAuthenticated]


class UserDetailAPIView(APIView):

    def get(self, request, pk):
        weight_trackings = WeightTracking.objects.filter(user_id=pk)
        fitness_goals = FitnessGoal.objects.filter(user_id=pk)

        weight_tracking_serializer = WeightTrackingSerializer(weight_trackings, many=True)
        fitness_goal_serializer = FitnessGoalSerializer(fitness_goals, many=True)

        user_details = {
            'weight_tracking': weight_tracking_serializer.data,
            'fitness_goals': fitness_goal_serializer.data,
        }

        return JsonResponse(user_details)




class WorkoutPlanViewSet(viewsets.ModelViewSet):
    queryset = WorkoutPlanExercise.objects.all()
    serializer_class = WorkoutPlanExerciseSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['post'])
    def update_progress(self, request, pk=None):
        workout_plan_exercise = self.get_object()
        workout_plan = workout_plan_exercise.workout_plan.pk
        current_exercise_id = request.data.get('exercise')
        repetitions_completed = request.data.get('reps')
        sets_completed = request.data.get('sets')

        try:    
            current_wpe = WorkoutPlanExercise.objects.get(workout_plan=workout_plan, exercise=current_exercise_id)
            if current_wpe.sets <= sets_completed and current_wpe.reps <= repetitions_completed:
                current_wpe.completed = True
                current_wpe.save()

            # Fetch and return the next exercise
                next_wpe = WorkoutPlanExercise.objects.filter(workout_plan=workout_plan, completed=False).first()
            

                if next_wpe is None:
                    return Response({'workout_plan_status': 'completed'}, status=status.HTTP_200_OK)
                return Response(WorkoutPlanExerciseSerializer(next_wpe).data, status=status.HTTP_200_OK)
        except WorkoutPlanExercise.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(current_wpe)
        return Response(serializer.data, status=status.HTTP_200_OK)
