#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''Create new style in Geoserver from file'''
__author__ = "Vladimir Rybalko"

from geoserver.catalog import Catalog
cat = Catalog("http://localhost:8080/geoserver/rest")
with open("testdata/testStyle.sld") as f:
    cat.create_style("testStyle", f.read(), overwrite=True, workspace="testWS")
print u"Новый стиль создан из файла {0}".format("testdata/testStyle.sld")