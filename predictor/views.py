from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from . import model  # Assuming model is a module in the same directory

@csrf_exempt
def index(request):
    if request.method == 'POST':
        try:
            print('Prediction called')
            # Parse the JSON body of the request
            data = json.loads(request.body)
            number = float(data.get('number'))

            # Call the predict function with the extracted number
            print('number')
            print(number)
            prediction = model.predict(number)
            print('prediction')
            print(prediction)

            # Return the prediction as a JSON response
            return JsonResponse({'prediction': prediction})
        except (ValueError, TypeError) as e:
            # Print the error for debugging
            print(f"Error: {e}")
            return JsonResponse({'error': 'Invalid input'}, status=400)
        except json.JSONDecodeError as e:
            # Handle JSON parsing errors
            print(f"JSON Decode Error: {e}")
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)