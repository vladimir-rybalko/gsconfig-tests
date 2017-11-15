#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''Create Geoserver RasterStore from tiff file'''
__author__ = "Vladimir Rybalko"

from geoserver.catalog import Catalog
cat = Catalog("http://localhost:8080/geoserver/rest", username="admin", password="geoserver")

tiffdata = {
    'tiff': 'testdata/testTiff.tif',
    'tfw':  'testdata/testTiff.tfw',
    'prj':  'testdata/testTiff.prj'
}

sf = cat.get_workspace("testWS")
ft = cat.create_coveragestore("testTiff", tiffdata, sf)
print u"Растровый слой опубликованн"