"""
This module manages the http request in a single point.
"""

from utils.file import read_yml
import requests

URLs = read_yml('data/urls.yml')


def get_data(key):
    """
    Retrieves the result from a http request, given a key.
    
    Args:
        key (str): It is the key related to an endpoint defined in urls/urls.yml.

    Returns:
        int: Status code
        list: Information retrieved from the endpoint.
    """
    try:
        response = requests.get(URLs[key])
        # Check if the request was successful
        if response.status_code == 200:
            # Print the response content
            return response.status_code, response.json()
        else:
            return response.status_code, None
    except Exception as e:
        return 0, None


if __name__ == '__main__':
    get_info(None)