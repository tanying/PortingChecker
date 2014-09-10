# -*- coding: utf8 -*-

__author__ = 'Tan Ying<ying.tan@tcl.com>' 

import os
import sys
import log
import json
import config
import commands

logger = log.getLogging('utils.py')

def compare_string(s1, s2):
    return (s1 == s2) and True or False

def get_standard_pkg_config():
    fIn = open(config.STANDARD_FILE, 'rb')
    text = fIn.read()
    fIn.close()
    standard_pkg_dict = json.loads(text)
    return standard_pkg_dict

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

    return pkg_dict

class Info(object):
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return self.message
    def show(self):
        print self.message 


class StandardJsonError(Exception):
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return self.message 
