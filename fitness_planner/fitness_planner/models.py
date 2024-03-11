from django.db import models
from django.contrib.auth.models import User


class Exercise(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    execution_steps = models.TextField(default=None, blank=True, null=True)
    target_muscles = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class WorkoutPlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    exercises = models.ManyToManyField(Exercise, through='WorkoutPlanExercise')
    frequency = models.PositiveIntegerField()  # in days
    session_duration = models.PositiveIntegerField()  # in minutes
    goal = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class WorkoutPlanExercise(models.Model):
    workout_plan = models.ForeignKey(WorkoutPlan, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    sets = models.PositiveIntegerField()
    reps = models.PositiveIntegerField()


class WeightTracking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    weight = models.DecimalField(max_digits=5, decimal_places=2)


class FitnessGoal(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    weight_log = models.ForeignKey(WeightTracking, on_delete=models.CASCADE)
    goal_weight = models.DecimalField(max_digits=5, decimal_places=2)
    target_date = models.DateField()

    def __str__(self):
        return f"{self.user}'s Fitness Goal"


class JWTToken(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.TextField()
