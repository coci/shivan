import validators


def check_url(url) -> bool:
    """
    validation url format

    parameters:
        - name : url
            description : download link provided by user
    responses:
        boolean
    """
    valid=validators.url(url)
    return bool(valid==True)
