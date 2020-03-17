import requests


def parts_size(url) -> list :
    resquest = requests.head(url)
    file_size = int(resquest.headers['content-Length'])
    each_split = int(res.headers['content-Length']) // 8
    split_size = [ x for x in range(0,int(res.headers['content-Length']),each_split)]
    split_size[6] = file_size

    return split_size
