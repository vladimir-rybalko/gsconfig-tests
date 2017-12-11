#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''Clear Geoserver WorkSpace'''
__author__ = "Vladimir Rybalko"

import sys
from geoserver.catalog import Catalog
cat = Catalog("http://localhost:8080/geoserver/rest", username="admin", password="geoserver")
default = None

if len(sys.argv) > 1:
    ws = cat.get_workspace (sys.argv[1])
    all_workspaces = cat.get_workspaces()
    if ws is None:
        print u'Не получилось найти рабочее пространство с таким именем'
        exit(1)

    for w in all_workspaces:
        print w.url
        if(w.name == ws.name):
            href = w.href
    default_ws = cat.get_default_workspace()
    if(default_ws.name == ws.name):
        print 
        default = True
    cat.delete(ws, recurse=True)
    cat.create_workspace(ws.name, href)
    if(default):
        cat.set_default_workspace(ws.name)
    print u'Слои из рабочего пространства "{0}" были успешно удалены'.format(sys.argv[1])
else:
    print u'Необходимо указать аргумент - рабочее пространство'
