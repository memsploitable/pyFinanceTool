# encoding: UTF-8
#
# Project: pyFinanceTool
# Author: borlittle
# CreateDate: 2017/11/19
"""
  BriefIntroduction:
    
    
  Update:
    
    
  Reference:
    
  RunningEnvironment: python 3.5 and above  
"""

# import packages

import logging
import os
import time

# create file for logging and config it.Then you can log in all the progect
nowTime = time.strftime("%Y%m%d_%H%M%S")
logFileName = os.path.join(os.path.abspath('log'), 'main' + nowTime + '.log')  # log file in the log directory

logger = logging.getLogger('')
logger.setLevel(logging.DEBUG)

fmter = logging.Formatter("%(asctime)s-%(levelname)s:%(message)s-[%(filename)s:%(lineno)d]")

filehandler = logging.FileHandler(filename=logFileName, mode='w', encoding="utf-8")
filehandler.setFormatter(fmter)

console = logging.StreamHandler()
console.setLevel(logging.INFO)
console.setFormatter(fmter)

logger.addHandler(filehandler)
logger.addHandler(console)


# just for unit test
if __name__ == '__main__':
    # TODO
    pass
