import requests
import urllib
import time
import os
import sys
from exception import UrlDoesNotExists

class Shivan(object):
    def __init__(self,url):
        self.url = url


if __name__ == "__main__":
    try:
        if len(sys.argv) > 1:
            url = sys.argv[1]
        else:
            raise UrlDoesNotExists
    except UrlDoesNotExists:
        print("please enter url ......")
        sys.exit(1)
    action = Shivan(url)
    print(action)