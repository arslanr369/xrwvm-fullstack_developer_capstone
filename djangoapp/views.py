from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import logging
import json
from .restapis import get_request, analyze_review_sentiments, post_review  # Import required methods

# Get an instance of a logger
logger = logging.getLogger(__name__)

@csrf_exempt  # Allow CSRF exemption for this view if necessary
def add_review(request):
    # Check if the user is authenticated
    if not request.user.is_anonymous:
        data = json.loads(request.body)  # Load the JSON data from the request body
        try:
            response = post_review(data)  # Call post_review with the data dictionary
            print(response)  # Optionally log the response for debugging
            if response and response.get("status") == 200:
                return JsonResponse({"status": 200, "message": "Review posted successfully"})  # Return success response
            else:
                return JsonResponse({"status": 400, "message": "Failed to post review"})  # Handle failure case
        except Exception as e:
            return JsonResponse({"status": 401, "message": "Error in posting review", "error": str(e)})  # Return error response
    else:
        return JsonResponse({"status": 403, "message": "Unauthorized"})  # Handle unauthorized access
