import sys
import json
from scraping_helpers import get_html
from classInfo import get_enrollment_info, get_teacher_info

def lambda_handler(event: dict, context) -> dict:
    p = event['queryStringParameters']['param']
    cmd = event['queryStringParameters']['cmd']
    if (cmd == "scores"):
        return {'status_code': '200',
                'body': json.dumps(get_teacher_info(p))
                }
    elif (cmd == "enrollment"):
        return {'status_code': '200',
                'body': json.dumps(get_enrollment_info(p))
                }
    else:
        return {'status_code': '400',
                'body': json.dumps('Command not found')
                }

def test_lambda_handler():
    """This may be helpful when testing your function"""
    with open(file='sample_input.json', mode='r') as f:
        sample_event = json.load(f)

    response = lambda_handler(sample_event, None)
    # print(json.dumps(response, indent=4))
    print(response)


if __name__ == '__main__':
    test_lambda_handler()
