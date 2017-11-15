#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''Publishing table from PGstore'''
__author__ = "Vladimir Rybalko"

from geoserver.catalog import Catalog
cat = Catalog("http://localhost:8080/geoserver/rest", username="admin", password="geoserver")

ds = cat.get_store("testPGStore")

ft = cat.publish_featuretype("seas", ds, "EPSG:4326", srs="EPSG:4326")
cat.save(ft)
print u"Таблица seas из хранилища testPGStore опубликованна {0}".format(ft)