# -*- coding: UTF-8 -*-

import socket
import urllib.request
from bs4 import BeautifulSoup
import time
from utils import write_list_to_txt
from config import name
from config import suffix_category
from config import suffix_keyword
from config import socket_timeout


span = 2
socket.setdefaulttimeout(socket_timeout)


def get_keyword():
    apd = False
    with open("./" + name + suffix_category, "r") as f:
        for line in f:
            url, wd = line.split("|")
            print(url)
            time.sleep(span)
            try:
                page = urllib.request.urlopen(url)
                data = page.read().decode("utf-8")
                soup = BeautifulSoup(data, "html.parser")
                tags = soup.select("dd a")
                res = [wd[:-1] + "|" + t["href"] + "|" + t.get_text() + "\n" for t in tags]

                write_list_to_txt(res, "./" + name + suffix_keyword, apd)
                if not apd:
                    apd = True
            except Exception as e:
                print(e)


get_keyword()
