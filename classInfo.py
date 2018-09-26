import sys
import json
from bs4 import BeautifulSoup
from scraping_helpers import get_html


def get_enrollment_info(c):
    url = 'http://classes.berkeley.edu/content/' + c + '/'
    html = get_html(url)
    elements = html.find_all("div", "handlebarData theme_is_whitehot")
    js = elements[0]['data-json']
    dic = json.loads(js)
    return dic['enrollmentStatus']

def get_teacher_info(c):
    url = 'http://www.ratemyprofessors.com/ShowRatings.jsp?tid=' + str(c)
    print(url)
    scores = []
    html = get_html(url)
    elements = html.find_all("div", "grade")
    for x in elements:
        scores += [x.getText().strip('\r').strip('\n').strip(' ').strip('\r\n')]
    return scores


#              Overall Quality
#                   <div class="grade" title="">4.7</div>
# </div>
# </div>
# </div>
# <div class="breakdown-header">
# <div class="breakdown-section takeAgain 97">
# <span class="title-container">
# <!-- <div class="title"> -->
#                     Would Take Again
#                   <!-- </div> -->
# <div class="help-toggle" data-target=".take-again-help-text"></div>
# </span>
# <div class="grade" title="">
#                   97%
#                 </div>
# </div>
# <div class="breakdown-section difficulty">
#                 Level of Difficulty
#                 <div class="grade" title="">
#                   3.3
