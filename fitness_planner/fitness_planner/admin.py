from django.contrib import admin
from .models import *

admin.site.register(Exercise)
admin.site.register(WorkoutPlan)
admin.site.register(WorkoutPlanExercise)
admin.site.register(WeightTracking)
admin.site.register(FitnessGoal)
