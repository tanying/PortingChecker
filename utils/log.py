# -*- coding: utf8 -*-
#log

__author__ = 'Tan Ying<ying.tan@tcl.com>'

import os
import shutil
import logging
import config

if os.path.exists(config.LOG_FILE):
    os.remove(config.LOG_FILE)

os.mknod(config.LOG_FILE)

logging.basicConfig(level = config.LOG_LEVEL_FILE,
                    format ='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    filename =config.LOG_FILE,
                    filemode ='w')

console = logging.StreamHandler()
console.setLevel(config.LOG_LEVEL)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)

def getLogging(name=''):
    if name == '':
        name = 'tanya'
    return logging.getLogger(name)