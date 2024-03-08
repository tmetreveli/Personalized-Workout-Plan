import json
from django.http import (JsonResponse)
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET"])
def abc(request):
    try:
        payload = json.loads(request.body.decode('utf-8'))
        print(payload)
        return JsonResponse({"Happy": "happy"})
    except Exception as e:
        print(e)
        return JsonResponse({"Sad": "sad"})
