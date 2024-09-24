from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import logging
import json
from .restapis import get_request, analyze_review_sentiments  # Import get_request and analyze_review_sentiments

# Get an instance of a logger
logger = logging.getLogger(__name__)

# Existing methods...

# Create a method to fetch reviews for a specific dealer
def get_dealer_reviews(request, dealer_id):
    # Check if dealer_id has been provided
    if dealer_id:
        endpoint = f"/fetchReviews/dealer/{str(dealer_id)}"
        reviews = get_request(endpoint)  # Fetch reviews using the get_request method

        # Analyze sentiment for each review and add it to the review detail
        for review_detail in reviews:
            response = analyze_review_sentiments(review_detail['review'])  # Call sentiment analysis
            print(response)  # Optional: log the response for debugging
            review_detail['sentiment'] = response.get('sentiment', 'unknown')  # Set sentiment value

        return JsonResponse({"status": 200, "reviews": reviews})  # Return reviews as a JsonResponse
    else:
        return JsonResponse({"status": 400, "message": "Bad Request"})  # Handle missing dealer_id
