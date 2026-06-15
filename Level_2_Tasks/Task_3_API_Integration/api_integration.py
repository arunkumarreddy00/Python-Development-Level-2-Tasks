import requests

url = "https://api.coindesk.com/v1/bpi/currentprice.json"

try:
    response = requests.get(url)
    response.raise_for_status()

    data = response.json()

    print("Bitcoin Price Information")
    print("Updated Time:", data["time"]["updated"])
    print("USD Price:", data["bpi"]["USD"]["rate"])
    print("GBP Price:", data["bpi"]["GBP"]["rate"])
    print("EUR Price:", data["bpi"]["EUR"]["rate"])

except requests.exceptions.RequestException:
    print("Failed to fetch API data")
except KeyError:
    print("Invalid API response")
