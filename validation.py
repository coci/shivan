import validators


def check_url(url):
    valid=validators.url(url)
    return bool(valid==True)
