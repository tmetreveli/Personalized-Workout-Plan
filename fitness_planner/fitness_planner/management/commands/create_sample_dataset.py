from django.core.management.base import BaseCommand
import os
import json

from fitness_planner.models import Exercise


class Command(BaseCommand):
    help = 'Creates exercises from JSON file'

    #
    # def add_arguments(self, parser):
    #     parser.add_argument('file_path', type=str, help='Path to the JSON file', )

    def handle(self, *args, **kwargs):
        # file_path = kwargs['file_path']
        file_path = os.path.join(os.path.dirname(__file__), './sample_exercises.json')

        if not os.path.exists(file_path):
            self.stdout.write(self.style.ERROR("Error: File does not exist."))
            return

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

            self.stdout.write(self.style.SUCCESS("Exercises created successfully."))