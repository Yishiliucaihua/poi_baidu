# -*- coding: UTF-8 -*-

import socket
import urllib.request
from urllib.parse import quote
import json
import time
from utils import write_list_to_txt
from utils import separate_store
from config import name
from config import name_zh
from config import suffix_keyword
from config import suffix_poi
from config import socket_timeout
from config import sleep_span


socket.setdefaulttimeout(socket_timeout)


def get_poi():
    apd = False
    with open("./" + name + suffix_keyword, "r") as f:
        for line in f:
            data = []
            _, _, wd = line[:-1].split("|")
            wd = name_zh + " " + wd
            url = "http://map.baidu.com/?newmap=1&reqflag=pcmap&biz=1&from=webmap&da_par=direct&pcevaname=pc4.1&qt=s" \
                  "&da_src=searchBox.button&wd=%s&pn=0" % quote(wd)
            print(wd)
            time.sleep(sleep_span)
            try:
                page = urllib.request.urlopen(url)
                res = json.load(page)
                if "content" in res:
                    contents = res["content"]
                    if "acc_flag" in contents[0]:
                        for item in contents:
                            t_l = [item["diPointX"], item["diPointY"]]
                            # name
                            if "name" in item:
                                t_l.append(item["name"])
                            else:
                                t_l.append("")
                            # addr
                            if "addr" in item:
                                t_l.append(item["addr"])
                            else:
                                t_l.append("")
                            # di_tag
                            if "di_tag" in item:
                                t_l.append(item["di_tag"])
                            else:
                                t_l.append("")
                            # std_tag
                            if "std_tag" in item:
                                t_l.append(item["std_tag"])
                            else:
                                t_l.append("")
                            data.append(separate_store(t_l))
                    if data:
                        write_list_to_txt(data, "./" + name + suffix_poi, apd)
                        if not apd:
                            apd = True
            except Exception as e:
                print(e)


get_poi()
