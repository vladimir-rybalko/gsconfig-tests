#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''Delete layers from list Geoserver WorkSpace'''
__author__ = "Vladimir Rybalko"

import sys
from geoserver.catalog import Catalog
cat = Catalog("http://localhost:8080/geoserver/rest", username="admin", password="geoserver")

if len(sys.argv) > 2:
    file = open(sys.argv[1])
    layerArray = []
    for line in file.read().splitlines():
        layerArray.append(line)
    all_layers = cat.get_resources(workspace='{0}'.format(sys.argv[2]))
    # all_layers = cat.get_layers()
    for l in all_layers:
        if(l.name in layerArray):
            cat.delete(l, recurse=True)
            print u'Слой {0} удален.'.format(l.name)
else:
    print u'Необходимо указать аргумент - файл с слоями для удаления.'
