#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''Print all layers Geoserver'''
__author__ = "Vladimir Rybalko"

from geoserver.catalog import Catalog
cat = Catalog("http://localhost:8080/geoserver/rest", username="admin", password="geoserver")

all_layers = cat.get_layers()

count = 1
for l in all_layers:
    print u"{3} - Имя слоя {0}, Стиль по умолчанию {1}, Ссылка на слой {2}".format(l.name, l.default_style.name, l.href, count)
    count +=1
exit
