# -*- coding: utf-8 -*-

from import_code.coordTransform_utils import bd09_to_wgs84
from config import name
from config import suffix_poi_lng_lat
from config import suffix_poi_lng_lat_fin
from utils import write_line_to_txt
from utils import separate_store
from config import rect


def process():
    apd = False
    with open("./" + name + suffix_poi_lng_lat, "r", encoding="utf-8") as f:
        for line in f:
            line = line[:-1]
            sep = line.split("|")
            lon, lat = bd09_to_wgs84(float(sep[0]), float(sep[1]))
            if rect[0] <= lat <= rect[1] and rect[2] <= lon <= rect[3]:
                sep[0] = str(lon)
                sep[1] = str(lat)
                write_line_to_txt(separate_store(sep), "./" + name + suffix_poi_lng_lat_fin, apd)
                if not apd:
                    apd = True


process()
