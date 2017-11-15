#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''Create Geoserver PGstore'''
__author__ = "Vladimir Rybalko"

from geoserver.catalog import Catalog
cat = Catalog("http://localhost:8080/geoserver/rest", username="admin", password="geoserver")

ds = cat.create_datastore("testPGStore", "testWS")
ds.connection_parameters.update(host='localhost', port='5432', database='tmp', user='postgres', passwd='123456', dbtype='postgis', schema='public')
cat.save(ds)

print u"Источник данных PG testPGStore создан"