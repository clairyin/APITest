#!/user/bin/python
# -*- coding: utf-8 -*-

######################################################################################
# Automation Scripts
#
# File: SceneAPI.py
# Author: clairyin
# Purpose: This script is used to generrate API report (Scene)
# Version: 1.0
# Requirements:python 2.6
# Supported OS: Linux 2.6, Mac OX 10.6 and above
#
#########################################################################################

#Parameter Descriptions:
#--$1: The *.jtl file path
#--$2: The summary.html file 
#--$3: The result.html file path
#--$4: The numbers of API in one scene
#--$4: The name of this scene
 
from xml.dom import minidom
from xml.dom.minidom import parse, parseString, Document
import xml.etree.ElementTree
import os, sys, string, datetime, time, re, codecs, decimal, optparse

def SceRepo(resultFilePath, summaryRepoPath, detailRepoPath, sceName,numAPI):
    resultfile = open(resultFilePath)
    sumFileR = open(summaryRepoPath,"r")
    s = sumFileR.read() 
    sumFileR.close()
    detFileR = open(detailRepoPath,'r')
    d = detFileR.read()
    detFileR.close()
    sumFileW = open(summaryRepoPath,'w')
    detFileW = open(detailRepoPath,'w')
    sce_total = 0
    sce_fail = 0
    result = []
    count = 0
    r = True
    #print 'numAPI =',numAPI
    #print 'sceName =',sceName

    try:
          for line in resultfile:
                testcase = line.split(',')
                name = testcase[5]
                apiresult = testcase[7]
                #print name

                if  (name.count(sceName)): 
                     count = count + 1
                     #print 'count =',count
                     #print 'apitest = ',apiresult
                     if (apiresult == 'false'):
                          r = False
                if (count == int(numAPI)):
                     #print 'two if'
                     result.append(r)
                     count = 0
                     r = True
          #print 'The result list is :',result
          sce_total = len(result) 
          print 'total =',sce_total
          sce_fail = result.count(False)

          s = s.replace(sceName + '_total' , str(sce_total))
          rate = str(round((float(sce_total) - float(sce_fail)) / float(sce_total),3)*100)
          res = str(sce_fail) + ' ' + '/' + ' ' + str(sce_total)
          
          if (sce_fail == 0):
              s = s.replace('<font color="red">' + sceName + '_fail' , '<font color="green">' + str(sce_fail))
              s = s.replace(sceName + '_rate' , rate + "%")
              d = d.replace('<font>' + sceName + '_result' , '<font color="green">' + res)

          else:
              s = s.replace(sceName + '_fail' , str(sce_fail))
              s = s.replace('<font color="green">' + sceName + '_rate' , '<font color="red">' + rate + "%")
              d = d.replace('<font>' + sceName + '_result' , '<font color="red>' + res)

    finally:
          resultfile.close()
          sumFileW.write(s)         #将最终结果写入summary。html中
          sumFileW.close()
          detFileW.write(d)         #将最终结果写入summary。html中
          detFileW.close()

if __name__ == '__main__':
       resultFilePath = sys.argv[1]
       summaryRepoPath = sys.argv[2]
       detailRepoPath = sys.argv[3]
       sceName = sys.argv[4]
       numAPI = sys.argv[5]
       SceRepo(resultFilePath, summaryRepoPath, detailRepoPath, sceName,numAPI)




















