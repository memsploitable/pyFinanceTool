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


# logging.debug('This is debug message')
# logging.info('This is info message')
# logging.warning('This is warning message')

# # founction utils
# def configLog():


# # class utils
# class utils():
#     def __init__(self, parent=None):
#         pass

def configLogging(logFileName='main.log'):
    # logging.basicConfig(level=logging.DEBUG,
    #                     format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
    #                     datefmt='%a, %d %b %Y %H:%M:%S',
    #                     filename=logFileName,
    #                     filemode='w')

    logger = logging.getLogger('log')
    logger.setLevel(logging.DEBUG)

    fmter = logging.Formatter("%(asctime)s-%(name)s-%(levelname)s:%(message)s-[%(filename)s:%(lineno)d]")

    filehandler = logging.FileHandler(filename=logFileName, mode='w', encoding="utf-8")
    filehandler.setFormatter(fmter)

    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    console.setFormatter(fmter)

    logger.addHandler(filehandler)
    logger.addHandler(console)

    return logger


# just for unit test
if __name__ == '__main__':
    # TODO
    pass
