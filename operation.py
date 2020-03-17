import requests
import re

def parts_size(url) -> list :
    """
    split file into 8 part from header
    param:
        - name : url
            - description : provided url
    responses:
        - name : split_size
            - description : list of possible part size ( in byte )
    """
    resquest = requests.head(url) # grab header
    full_size = int(resquest.headers['content-Length']) # full size 
    split_size = [ x for x in range(0,full_size,full_size // 8)] # create 
    split_size[8] = full_size # fix least size to remainder byte from split
    return split_size

def grab_file_name(url):
    file_name = re.findall(r'(?=\w+\.\w{3,4}$).+',url)
    return file_name[0]