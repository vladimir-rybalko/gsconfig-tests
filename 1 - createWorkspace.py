#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''Create Geoserver WorkSpace'''
__author__ = "Vladimir Rybalko"

from geoserver.catalog import Catalog
cat = Catalog("http://localhost:8080/geoserver/rest", username="admin", password="geoserver")


ws = cat.get_workspace ("testWS")
if ws is None:
    cat.create_workspace("testWS", "http://testWS")
    cat.set_default_workspace('testWS')

ws = cat.get_default_workspace()
print u"Рабочее пространство создано {0}".format(ws)