import lxml.html
import os
from PIL import Image
import urllib.request
from urllib.request import urlopen
from concurrent import futures
import string
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
            info = [file_path,"/",filename]
            file_full = "".join(info)
            print(file_full)
            with open(file_full, "wb") as g:
                g.write(urlData)
            try:
                with Image.open(file_full) as r:
                    width , height = r.size
                    with Image.open(r, "r") as im:
                        try:
                            im.verify()
                        except Exception:
                            a = 0
            except Exception as fuck:
                print(fuck)
                pass
            if width * height < 250000:
                a = 0
            if a ==0:
                os.remove(file_full)
        except Exception as e:
            print(e)
            if os.path.exists(file_full) == True:
                os.remove(file_full)
    with futures.ThreadPoolExecutor() as executor:
        executor.map(get_img, image)