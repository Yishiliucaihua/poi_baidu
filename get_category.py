# -*- coding: UTF-8 -*-

import urllib.request
from bs4 import BeautifulSoup
import re
from utils import write_list_to_txt
from config import name
from config import suffix_category


url_path = "http://poi.mapbar.com/"
pattern = url_path + name + r"/[^.]+?/|.*?"


def get_category():
    page = urllib.request.urlopen(url_path + name + "/")
    data = page.read()
    data = data.decode("utf-8")
    soup = BeautifulSoup(data, "html.parser")
    tags = soup.select("a")
    res = [t["href"] + "|" + t.get_text() + "\n" for t in tags]

    tmp = []
    for i in range(0, len(res)):
        if re.match(pattern, str(res[i]), re.I | re.DOTALL).span()[1] > 0:
            tmp.append(res[i])
    print(tmp)
    write_list_to_txt(tmp, "./" + name + suffix_category, False)


get_category()
