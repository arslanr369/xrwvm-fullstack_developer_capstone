# Uncomment the required imports before adding the code
# from django.shortcuts import render
# from django.http import HttpResponseRedirect, HttpResponse
# from django.contrib.auth.models import User
# from django.shortcuts import get_object_or_404, render, redirect
# from django.contrib.auth import logout
# from django.contrib import messages
# from datetime import datetime

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import logging
import json
from .restapis import get_request  # Import get_request from restapis.py

# Get an instance of a logger
logger = logging.getLogger(__name__)

# Update the `get_dealerships` method to fetch and return a list of dealerships
def get_dealerships(request, state="All"):
    # Check if the state filter is applied
    if state == "All":
        endpoint = "/fetchDealers"
    else:
        endpoint = f"/fetchDealers/{state}"  # Use state if provided

    # Fetch data from the API using get_request
    dealerships = get_request(endpoint)

    # If data is fetched successfully, return it with a success status
    if dealerships is not None:
        return JsonResponse({"status": 200, "dealers": dealerships})
    
    # If something went wrong, return an error response
    return JsonResponse({"status": 500, "message": "Could not fetch dealerships"})

# View to fetch dealer details based on dealer_id
def get_dealer_details(request, dealer_id):
    if dealer_id:
        endpoint = f"/fetchDealer/{str(dealer_id)}"
        dealership = get_request(endpoint)
        if dealership:
            return JsonResponse({"status": 200, "dealer": dealership})
        return JsonResponse({"status": 404, "message": "Dealer not found"})
    return JsonResponse({"status": 400, "message": "Bad Request"})
