import sys
import json
from scraping_helpers import get_html

def lambda_handler(event: dict, context) -> dict:
    return {'status_code': '200',
            'body': json.dumps(event)
            }

def send_class_request(c):
    url = 'http://guide.berkeley.edu/courses/' + c + '/'
    return url

if __name__ == '__main__':
    print(lambda_handler({}, None))
