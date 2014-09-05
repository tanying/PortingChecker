# -*- coding: utf8 -*-

__author__ = 'Tan Ying<ying.tan@tcl.com>' 

import os
import sys
import log
import json
import commands

logger = log.getLogging('utils.py')

def get_standard_pkg_config():
    fIn = open(config.STANDARD_FILE, 'rb')
    text = fIn.read()
    fIn.close()
    standard_pkg_dict = json.loads(text)
    logger.debug(standard_pkg_dict)
    return standard_pkg_dict

def get_path_from_phone():
    shell_file_path = sys.path[0] + '/PullApkInfoFromPhone.sh'
    os.system('source %s' % shell_file_path)
    if os.path.isfile('apkList.txt'):
        path_dict = get_pkg_path_dict()
        return path_dict

def get_version_from_phone(pkg_name):
    command = 'adb shell pm dump %s|grep versionName'
    status, output = commands.getstatusoutput(command % pkg_name)
    logger.debug(output.strip())
    return output.strip()

def get_pkg_path_dict():
    pkg_dict = {}
    f = open('apkList.txt', 'r')
    while True:
        line = f.readline()
        if not line:
            break
        else:

            row = line.split('=')
            name = row[1].strip('\r\n')

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
