# Uncomment the imports below before you add the function code
import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve the backend URLs from environment variables
backend_url = os.getenv('backend_url', default="http://localhost:3030")
sentiment_analyzer_url = os.getenv('sentiment_analyzer_url', default="http://localhost:5050/")

# Define the get_request function for making API GET requests
def get_request(endpoint, **kwargs):
    params = ""
    # If there are any keyword arguments, format them into query parameters
    if kwargs:
        for key, value in kwargs.items():
            params += f"{key}={value}&"  # append each key-value pair as query parameter
    
    # Construct the final request URL with the endpoint and parameters
    request_url = f"{backend_url}{endpoint}?{params.strip('&')}"  # strip '&' at the end
    print(f"GET from {request_url}")

    try:
        # Make the GET request using the requests library
        response = requests.get(request_url)
        # If the response is successful (status code 200), return the JSON data
        response.raise_for_status()  # Raise exception if the request failed
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")  # Handle HTTP errors (e.g., 404, 500)
    except Exception as err:
        print(f"Network exception occurred: {err}")  # Handle other errors (network, etc.)
    return None  # Return None in case of an error
