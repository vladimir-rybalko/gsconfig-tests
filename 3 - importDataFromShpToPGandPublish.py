#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''Import shp data to Geoserver PGstore and publish layer'''
__author__ = "Vladimir Rybalko"

from geoserver.catalog import Catalog
cat = Catalog("http://localhost:8080/geoserver/rest", username="admin", password="geoserver")

ds = cat.get_store("testPGStore")

ft = cat.add_data_to_store(ds, "import", {
    'shp': 'testdata/polygons.shp',
    'shx': 'testdata/polygons.shx',
    'dbf': 'testdata/polygons.dbf',
    'prj': 'testdata/polygons.prj'
})
print u"Данные загружены в хранилище testPGStore, слой создан"