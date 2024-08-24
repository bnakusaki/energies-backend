from django.shortcuts import render
from django.http import HttpResponse
from . import model

# Create your views here.
def index(request):
    # Extract the 'value' parameter from the GET request
    value = request.GET.get('value', None)
    
    if value is not None:
        prediction = model.predict(value)  # Assuming model has a predict function
        return HttpResponse(prediction)
    else:
        return HttpResponse("No value provided.")