import requests

def fetch_product_json():
    # API request URL
    request_url = "https://www.thecocktaildb.com/api/json/v1/1/search.php?f=a"
    response = requests.get(request_url)

    # Parse the JSON response
    parsed_response = response.json()
    data = parsed_response["drinks"]

    # Select specific fields
    drinks = [
        {
            "name": drink.get("strDrink", "Unknown") or "Unknown",
            "description": drink.get("strCategory", "Unknown") or "Unknown",
            "url": drink.get("strDrinkThumb", "Unknown") or "Unknown"
        }
        for drink in data
    ]

    # Return the results
    return drinks
