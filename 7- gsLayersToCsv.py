#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''Print all layers Geoserver'''
__author__ = "Vladimir Rybalko"

import csv
from geoserver.catalog import Catalog
# cat = Catalog("http://localhost:8080/geoserver/rest", username="admin", password="geoserver")

base='http://192.168.0.213:8585/geoserver/rest'
user='admin'
password='geoserver'

cat = Catalog(base, username=user, password=password)

# store = cat.create_coveragestore("test", '/Volumes/data1/rob_coop/coop_data/DEM/mosaic/srtm/srtm_2000_30m_cgg2013.tif', workspace=hlrg, overwrite=True)
excludeWs = ["anivsky_go"]
# http://192.168.0.213:8585/geoserver/rest/workspaces/ugl_ugl_gp/datastores/v3_ugl_ugl_gp/featuretypes/v3_ugl_ugl_gp_urban_eng_gas_op.xml
excludeRs = ["v3_ukur_urban_red_line", "v3_uglgo_urban_eng_gas_op", "v3_uglgo_urban_eng_gas_ppm_ss", "v3_uglgo_urban_eng_gas_ppm_pr", "v3_mak_urban_eng_gas_ppm_pr", "v3_mak_urban_eng_gas_ppm_ss", "v3_mak_urban_eng_gas_op", "v3_ugl_ugl_gp_urban_eng_gas_ppm_pr", "v3_ugl_ugl_gp_urban_eng_gas_op", "v3_ugl_ugl_gp_urban_eng_gas_ppm_ss", "v3_dol_urban_eng_gas_ppm_pr", "v3_dol_urban_eng_gas_ppm_ss", "v3_dol_urban_eng_gas_op", "v3_tim_urban_eng_gas_ppm_ss", "v3_tim_urban_eng_gas_ppm_pr", "v3_tim_urban_eng_gas_op", "v3_tim_urban_f_zone_ppm", "v3_uglb_urban_eng_gas_op", "v3_uglb_urban_eng_gas_ppm_pr", "v3_uglb_urban_eng_gas_ppm_ss", "v3_nogl_urban_eng_gas_ppm_pr", "v3_nogl_trans_trainnetwork", "v3_nogl_urban_eng_gas_op", "v3_nogl_urban_eng_gas_ppm_ss", "v3_nogl_trans_roadnetwork", "v3_skur_urban_red_line", "v3_kur_urban_red_line", "v3_ugls_urban_eng_gas_ppm_ss", "v3_ugls_urban_eng_gas_op", "v3_ugls_urban_eng_gas_ppm_pr", "v3_nev_urban_eng_gas_ppm_pr", "v3_nev_urban_eng_gas_ppm_ss", "v3_nev_urban_eng_gas_op", "v3_por_urban_eng_gas_ppm_pr", "v3_por_urban_eng_gas_op", "v3_por_urban_eng_gas_ppm_ss"]
wss = cat.get_workspaces()
output_file = open("out.csv", "w")
def writeData(string):
    text = string.decode('utf8')
    string = text.encode('cp1251')
    output_file.write(string)
writeData("номер;имя слоя;воркспейс;хранилище;стиль[имя стиля: воркспейс];тип (Растр или PG или Иное);система координат\n")
count = 1

for ws in wss:
    if ws.name not in excludeWs:
        resources = cat.get_resources(workspace=ws.name)
        for res in resources:
            if res.name not in excludeRs:
                name = res.store.name
                typeStore = res.store.type
                projection = res.projection

                layer = cat.get_layer(res.name)
                # print ";".join([str(name), str(typeStore), str(projection)])
                style = layer.default_style
                workspace = ''
                if style.workspace != None:
                    workspace = style.workspace
                style = ":".join([str(style.name), str(workspace)])
                count +=1
                # print ";".join([res.name, ws.name, res.store.name, style, res.store.type, res.projection])
                writeData(";".join([str(count), res.name, ws.name, res.store.name, style, res.store.type, res.projection]) + "\n")
output_file.close()