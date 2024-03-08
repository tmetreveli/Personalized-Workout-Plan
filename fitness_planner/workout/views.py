import json
from django.http import (JsonResponse)
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET"])
def abc(request):
    try:
        name = request.GET.get('name', 'happy')
        return JsonResponse({"Happy": name})
    except Exception as e:
        print(e)
        return JsonResponse({"Sad": "sad"})
