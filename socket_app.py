# -*- coding: utf-8 -*-

import json

def data():
    ifDO = ifDO_para()
    DOSpeed = DOSpeed_para()
    ifCE = ifCE_para()
    CESpeed = CESpeed_para()
    ifUP = ifUP_para()
    UPSpeed = UPSpeed_para()
    data = {
        'mainControl':1,
        'data':{
            'ifDO':ifDO,
            'DOSpeed':DOSpeed,
            'ifCE':ifCE,
            'CESpeed':CESpeed,
            'ifUP':ifUP,
            'UPSpeed':UPSpeed,
        }
    }
    data_json = json.dumps(data)
    return data_json

def ifDO_para():
    ifDO = 'True'           #此处要传参
    return ifDO

def DOSpeed_para():
    DOSpeed = 'zengying'    #此处要传参
    return DOSpeed

def ifCE_para():
    ifCE = 'True'           #此处要传参
    return ifCE

def CESpeed_para():
    CESpeed = 'zengying'    #此处要传参
    return CESpeed

def ifUP_para():
    ifUP = 'True'           #此处要传参
    return ifUP

def UPSpeed_para():
    UPSpeed = 'zengying'    #此处要传参
    return UPSpeed


'''
    print('data:', data_json)
    print(type(data_json))
'''

