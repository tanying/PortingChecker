# -*- coding: utf8 -*-

__author__ = 'Tan Ying<ying.tan@tcl.com>' 

import logging

OUTPUT_DIR = 'output/'
LOG_LEVEL = logging.DEBUG
LOG_LEVEL_FILE = logging.DEBUG
LOG_FILE = OUTPUT_DIR + 'PortingChecker.log'
STANDARD_3RD_FILE = 'config/3rd.json'
STANDARD_GMS_FILE = 'config/gms.json'
STANDARD_JSON_CONFIG_JS = 'js/jsonConfig.js'
RESULT_FILE =  OUTPUT_DIR + 'compareResult.txt'
PULL_PATH_FILE = 'utils/PullApkInfoFromPhone.sh'
PATH_FILE = OUTPUT_DIR + 'apkList.txt'
CONFIG_SET = ['gms.json', '3rd.json']
INVALID_CONFIG_ARGUMENT = 'Invalid config argument'
HTML_GENERATER = 'generater.html'