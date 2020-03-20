import re
from exception import InCorrectUrl
import sys
import requests

def check_url(url) -> None:
    """
    validation url format

    parameters:
        - name : url
            description : download link provided by user
    responses:
        None
    """
    try:
        # check if url contain .[extension]
        if len(list(re.findall(r'([.][\w]+)',url))) <= 2:
            raise InCorrectUrl
    except InCorrectUrl:
        print("")
        print("provided url doesn't coinatin file to download.")
        print("please enter url in correct format : ")
        print("")
        print(" [http or https]://[domain].[domain suffix]/[file name].[extension]")
        sys.exit(1)

    try:
        # check if url is correct
        res = requests.head(url)
    except ValueError:
        print("url provided is not ture .")
        sys.exit(1)