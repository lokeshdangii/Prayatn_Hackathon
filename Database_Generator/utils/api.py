import requests

def api_calling():

    # Defining the API endpoint and access key
    url = "http://13.48.136.54:8000/api/api-code/"
    access_key = "b5a33d60-327c-4e36-9050-5726e10d0eb1"

    headers = {"Authorization": f"Bearer {access_key}"}

    # Make a POST request to the API
    response = requests.post(url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:

        # Extract the API code from the response
        api_code = response.json()["api_code"]
        return f'API code:, {api_code}'
    else:
        return f'Error: {response.status_code}'
