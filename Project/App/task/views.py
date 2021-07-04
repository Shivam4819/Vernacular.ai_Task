
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .api import validate_finite_values_entity, validate_numeric_entity
import json

@csrf_exempt
def validate_finite_values_entity_api(request):
    if request.method == 'POST':

        # Parse the json data sent in body
        data = json.loads(request.body)
        
        # Get each data seperately
        values = data["values"]
        supported_values = data["supported_values"]
        invalid_trigger = data["invalid_trigger"]
        key = data["key"]
        support_multiple = data["support_multiple"]
        pick_first= data["pick_first"]

        response = validate_finite_values_entity(values, supported_values,invalid_trigger, key, support_multiple, 
                pick_first)

        # Sending response in Json
        return JsonResponse(response)
    else:
        return HttpResponse('Invalid Method')
                

@csrf_exempt
def validate_numeric_entity_api(request):
    if request.method == 'POST':

        # Parse the json data sent in body
        data = json.loads(request.body)
        
        # Get each data seperately
        values = data["values"]
        invalid_trigger = data["invalid_trigger"]
        key = data["key"]
        support_multiple = data["support_multiple"]
        pick_first= data["pick_first"]
        constraint= data["constraint"]
        var_name = data["var_name"]

        response = validate_numeric_entity(values, invalid_trigger, key, support_multiple, pick_first, constraint, var_name)

        # Sending response in Json
        return JsonResponse(response)
    else:
        return HttpResponse ('Invalid Requset')
