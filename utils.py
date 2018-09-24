import sys
from bs4 import BeautifulSoup


def get_classes(html):
    """
    returns a list of classes and titles, parsing through 'html'
    """
    # elements = html.find_all("span", "code")
    # titles = html.find_all("span", "title")
    # classes = []
    # for i in range(len(elements)):
    #     item = elements[i]
    #     tit = titles[i]
    #     classes += [(item.text.replace('\xa0', ' '), tit.text.replace('\xa0', ' '))]
    # return classes
