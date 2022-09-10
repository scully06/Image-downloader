import lxml.html
import os
from PIL import Image
import urllib.request
from urllib.request import urlopen
from concurrent import futures
#下はダウンロード用関数
def get_URL(url, file_path):
    opener = urllib.request.build_opener()
    opener.addheaders = [("User-Agent", "Mozilla/5.0")]
    urllib.request.install_opener(opener)
    tree = lxml.html.parse(urlopen(url))
    html = tree.getroot()
    image_list = html.cssselect("img")
    image = set(map(lambda image_list:image_list.get("src"),image_list))
    def get_img(link):
        try:
            a = 1
            urlData = urlopen(link).read()
            filename = os.path.basename(link)
            path = file_path + "/"
            with open(path + filename, "wb") as g:
                g.write(urlData)
            try:
                with Image.open(path + filename) as r:
                    width , height = r.size
                    im = Image.open(r, "r")
                    try:
                        im.verify()
                    except Exception:
                        a = 0
            except Exception:
                pass
            if width <= 500 or height <= 500:
                a = 0
            if a == 0:
                os.remove(path + filename)
        except Exception as e:
            if os.path.exists(file_path + "/" + filename) == True:
                os.remove(path + filename)
    with futures.ThreadPoolExecutor() as executor:
        executor.map(get_img, image)