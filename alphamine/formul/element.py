#coding=utf-8
#author=godpgf


class DataElement(object):

    def __init__(self, name, data, unit_flag):
        self.name = name
        self.data = data
        self.unit_flag = unit_flag


class OptElement(object):

    def __init__(self, name, fun_cal, fun_check):
        self.name = name
        self.fun_cal = fun_cal
        self.fun_check = fun_check

    