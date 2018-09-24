import sys
from requests import get
from requests.exceptions import RequestException
from bs4 import BeautifulSoup
from utils import get_classes

def get_html(url):
    """
    gets the html of the url specified
    """
    response = simple_get(url)
    html = BeautifulSoup(response, 'html.parser')
    return html

def simple_get(url):
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    """
    try:
        response = get(url)
        if is_good_response(response):
            return response.content

        else:
            return None

    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None


def is_good_response(resp):
    """
    Returns True if the response seems to be HTML, False otherwise.
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1)


def log_error(e):
    """
    It is always a good idea to log errors.
    This function just prints them, but you can
    make it do anything.
    """
    print(e)
