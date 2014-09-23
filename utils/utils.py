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
            if argument.upper() == item:
                return True
        else:
            if argument == item:
                return True
    return False

def change_list_to_json(list):
    string = '{\n'

    for item in list:
        package = item[0]
        path = item [1]
        version = item[2]

        string += '  "%s":{\n    "path":"%s",\n    "versionName":"%s"\n  },\n' % (package, path, version)

    string = string[:-2]
    string += '\n}'

    fOut = open(config.STANDARD_GMS_FILE, 'w')
    fOut.write(string)
    fOut.close()

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
    command = 'adb shell pm dump %s|grep versionName'
    status, output = commands.getstatusoutput(command % pkg_name)
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
