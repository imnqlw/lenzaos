from utils.attach import response_logging, response_attaching
import requests

def api_request(url, endpoint, method, params=None):
    url = f"{url}{endpoint}"
    headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 YaBrowser/24.4.0.0 Safari/537.36'}
    response = requests.request(method, url, params=params, headers=headers)
    response_logging(response)
    response_attaching(response)
    return response


