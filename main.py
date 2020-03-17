import requests
import urllib
import time
import os
import sys
from exception import UrlDoesNotExists
from core import parts_size

class Shivan(object):
    def __init__(self,url):
        self.url = url
        self._download()

    def _split(self):
       return parts_size(self.url)

    def _download(self):
        parts = self._split()
        path_to_download = str(os.getcwd()) + "/.temp"
        for i in range(0,len(parts)-1):
            start = parts[i] + 1 if i > 0 else parts[i]
            end = parts[i+1]
            res = requests.get(self.url,headers={"Range": f"bytes={start}-{end}"})
            with open(path_to_download+f"/part{i}.jpg", 'wb') as f:
                f.write(res.content)

        
        files = []
        final = open(str(os.getcwd())+"/final.jpg","wb")
        for r, d, f in os.walk(path_to_download):
            for file in f:
                if 'jpg' in file:
                    files.append(os.path.join(r, file))
        files = sorted(files)

        for i in files:
            temp = open(i, 'rb')
            temp = temp.read()
            final.write(temp)
        final.close()
        for i in files:
            if not 'final.jpg' in i:
                os.remove(i)
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