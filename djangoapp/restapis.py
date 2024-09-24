import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve the backend URLs from environment variables
backend_url = os.getenv('backend_url', default="http://localhost:3030")

# Define the post_review function to send a POST request
def post_review(data_dict):
    request_url = f"{backend_url}/insert_review"
    try:
        response = requests.post(request_url, json=data_dict)  # Send POST request with JSON data
        print(response.json())  # Print the response for debugging
        return response.json()  # Return the response JSON
    except Exception as e:
        print(f"Network exception occurred: {e}")  # Log any exceptions that occur
        return None  # Return None if there was an error
