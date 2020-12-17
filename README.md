# Baidu POIs Downloader
## Utility
### find lots of POIs in specified city such as "chengdu" and "beijing"
## File Description
### config.py
config file of downloading and data clean
### get_category.py
download categories of POIs of specified city
### get_keyword.py
download keywords of POIs of specified city
### get_poi.py
download POIs of specified city
### convert_location.html
convert projection coordination to baidu coordination
### poi_filter.py
convert baidu coordination to wgs-84(if you don't want to do this, you can change the corresponding code 
with coordination transform tool in ./import_code) and remove POI that out of specified range
## How To Use
### 1. adjust the config.py according to your purpose
### 2. run get_category.py
### 3. run get_keyword.py
### 4. run get_poi.py(this may takes 2-3 days normally)
### 5. run convert_location.html in your browser and move the downloaded file to the directory of this project and rename this file like "chengdu_poi_lng_lat.txt" if necessary
### 6. run poi_filter.py
## Reference
### https://blog.csdn.net/my_lovely_lemon_tree/article/details/78418625
### https://github.com/wandergis/coordTransform_py
### https://github.com/eligrey/FileSaver.js
## Limitation
### POIs dataset downloaded by this tool isn't very precise, it may only used in some interesting tests/demos, if you want to get the real POIs dataset, you may use the API of baidu map SDK(http://lbsyun.baidu.com/index.php?title=webapi)