# -*- coding: utf8 -*-

__author__ = 'Tan Ying<ying.tan@tcl.com>' 

import os
import sys
import log
import json
import config
import commands

logger = log.getLogging('utils.py')

def is_argument_in_dataset(argument, dataset, ignore_case = False):
    """
    参数是否在数据集中
    """
    for item in dataset:
        if ignore_case:
            if argument.lower() == item.lower():
                return True
        else:
            if argument == item:
                return True
    return False

def change_list_to_json(list, file):
    string = ''
    if len(list) > 0:
        string = '{\n'

        for item in list:
            package = item[0]
            path = item [1]
            version = item[2]
            perso = item[3]

            string += '  "%s":{\n    "path":"%s",\n    "versionName":"%s",\n    "perso":"%s"\n  },\n' % (package, path, version, perso)

        string = string[:-2]
        string += '\n}'

    fOut = open(file, 'w')
    fOut.write(string)
    fOut.close()

def get_perso_attr(dir):
    dir = dir.lower()
    if dir[-4:-1] == 'gms' or dir[-8:-1] == 'gms_pri':
        return 'gms'
    elif dir[-8:-1] == 'tmobile' or dir[-12:-1] == 'tmobile_pri':
        return 'tmo'
    elif dir[-9:-1] == 'metropcs' or dir[-13:-1] == 'metropcs_pri':
        return 'mps'
    else:
        return 'all'

def compare_string(s1, s2):
    return (s1 == s2) and True or False

def merge_dict(dict1,dict2):
    dict_merged=dict(dict1, **dict2)
    return dict_merged

def get_standard_pkg_config(filepath):
    fIn = open(filepath, 'rb')
    text = fIn.read()
    fIn.close()
    file_dict = json.loads(text)
    return file_dict

def get_path_from_phone():
    shell_file_path = sys.path[0] + '/' + config.PULL_PATH_FILE
    os.system('source %s' % shell_file_path)
    if os.path.isfile(config.PATH_FILE):
        path_dict = get_pkg_path_dict()
        return path_dict
    else:
        sys.exit(1)

def get_version_from_phone(pkg_name):
    command = 'adb shell pm dump %s|grep versionName' % pkg_name
    status, output = commands.getstatusoutput(command)
    versionName = output.strip()
    index = versionName.find('=') + 1
    version = versionName[index:]
    return version

def get_pkg_path_dict():
    pkg_dict = {}
    f = open(config.PATH_FILE, 'r')
    while True:
        line = f.readline()
        if not line:
            break
        else:
            if line.find('=') > -1:
                row = line.split('=')
                name = row[1].strip('\r\n')
            else:
                row = line.strip('\r\n')
                name = ''

            #strip 'package:'
            index = row[0].find(':') + 1
            path = row[0][index:]
            pkg_dict[name] = path

    f.close()
    return pkg_dict

def generate_config_jsfile(path, js_path):
    """
    载入json文件,并生成js文件,用于导入html
    """
    fIn = open(path, 'r')
    lines = fIn.read()
    fIn.close()

    string = 'var json= %s' % lines
    fOut = open(js_path, 'w')
    fOut.write(string)
    fOut.close()
    return True

class Info(object):
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return self.message
    def show(self):
        print self.message 


class PortingCheckerError(Exception):
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return self.message 
