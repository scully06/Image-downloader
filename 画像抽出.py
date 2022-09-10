import requests
import lxml.html
from tenacity import retry, wait_fixed
import os
from PIL import Image
from fake_useragent import UserAgent
import urllib.request
from urllib.request import urlopen
from concurrent import futures

@retry(wait=wait_fixed(3))
def get_URL(url, file_path):
    opener = urllib.request.build_opener()
    opener.addheaders = [("User-Agent", "Mozilla/5.0")]
    urllib.request.install_opener(opener)
    url_list = []
    ua = UserAgent()
    hedder = {"User-Agent": str(ua.chrome)}
    tree = lxml.html.parse(urlopen(url))
    html = tree.getroot()
    for image in html.cssselect("img"):
        url_list.append(image.get("src"))
    set_url = set(url_list)
    def get_img(link):
        try:
            a = 1
            urlData = urlopen(link).read()
            filename = os.path.basename(link)
            with open(file_path + "/" + filename, "wb") as g:
                g.write(urlData)
                print("1")
            try:
                with Image.open(file_path + "/" + filename) as r:
                    width , height = r.size
                    im = Image.open(r, "r")
                    try:
                        im.verify()
                    except Exception as q:
                        #print("1")
                        print(q)
                        a = 0
            except Exception as j:
                print(j)
                #a = 0
            if width <= 500 or height <= 500:
                a = 0
            if a == 0:
                #print("2")
                os.remove(file_path + "/" + filename)
        except Exception as e:
            if os.path.exists(file_path + "/" + filename) == True:
                os.remove(file_path + "/" + filename)
            #print(e)
    try:
        with futures.ThreadPoolExecutor() as executor:
            executor.map(get_img, set_url)
    except Exception as j:
        print(j)
