import requests
from bs4 import BeautifulSoup
from tenacity import retry, wait_fixed
import os
from PIL import Image
from fake_useragent import UserAgent
import urllib.request, urllib.error
@retry(wait=wait_fixed(3))
def get_URL(url, file_path):
    ua = UserAgent()
    hedder={"User-Agent":str(ua.chrome)}
    res = requests.get(url, headers=hedder)
    soup = BeautifulSoup(res.text,"html.parser")
    for link in soup.find_all("img"):
        try:
            temp_direc= file_path + "/" + os.path.basename(link.get("src"))
            urlData = requests.get(link.get("src"), headers=hedder).content
            filename = os.path.basename(link.get("src"))
            try:
                opener = urllib.request.build_opener()
                opener.addheaders = [("User-Agent", "Mozilla/5.0")]
                urllib.request.install_opener(opener)
                url_temp = urllib.request.urlopen(link.get("src"))
                url_temp.close()
            except Exception as h:
                print(h)
                continue
            else:
                with open(file_path + "/" + filename,"wb") as g:
                    g.write(urlData)
                try:
                    with Image.open(file_path + "/" + filename) as r:
                        width ,height = r.size
                        im = Image.open(r, "r")
                        try:
                            im.verify()
                        except Exception as q:
                            print("1")
                            print(q)
                            a = 0
                except Exception as j:
                    print(j)
                    a = 0
                if width <= 500 or height <= 500:
                    a = 0
                else:
                    continue
            if a == 0:
                os.remove(file_path + "/" + filename)             
        except Exception as e:
            if os.path.exists(file_path + "/" + filename) == True:
                os.remove(file_path + "/" + filename)
            continue