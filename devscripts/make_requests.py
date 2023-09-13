import requests

def make_request(url):
    """    Takes a url as a string and returns a response obj    """
    try:
        response = requests.get(url, params={})
        response.raise_for_status()
    # except requests.exceptions.HTTPError as err:
    #     raise SystemExit(err)
    # except requests.exceptions.Timeout:
    #     # Maybe set up for a retry, or continue in a retry loop
    # except requests.exceptions.TooManyRedirects:
    #     # Tell the user their URL was bad and try a different one
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    
    return response