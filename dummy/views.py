import json 
from django.http import JsonResponse

def sample(*args, **kwargs):
    return JsonResponse({"message":"hello from the backend"})