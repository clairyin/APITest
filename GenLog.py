#!/usr/bin/python
# -*- coding: utf-8 -*-
######################################################################################
# Automation Scripts
#
# File: GenLog.py
# Author: flyyou
# Purpose: This script is used to generate report
# Version: 1.0
# Requirements: Python 2.6
# Supported OS: Linux 2.6, Mac OX 10.6 and above
#
#####################################################################################

#Parameter Descriptions:
#--$1: The *.jtl file path
#--$2: The results.html file path
#--$3: The total test times of each API
from xml.dom import minidom
from xml.dom.minidom import parse, parseString, Document
import xml.etree.ElementTree
import os, sys, string, datetime, time, re, codecs, decimal, optparse
import codecs;
reload(sys)
sys.setdefaultencoding( "utf-8" )

def GenSummaryResult(filePath, genFilePath):
        # print "filePath: " + filePath
        inputfile = open(filePath)
        fileR = open(genFilePath, "r")
        s = fileR.read()
        fileR.close()

        fileW = open(genFilePath, "w")
        # wechat_total = 0
        weiliao_total = 0
        anjuke_total = 0
        haozu_total = 0
        aifang_total = 0
        jingjiren_total = 0
        # wechat_fail = 0
        weiliao_fail = 0
        anjuke_fail = 0
        haozu_fail = 0
        aifang_fail = 0
        jingjiren_fail = 0       
	try:
                while 1:                        
                        lines = inputfile.readlines()
                        if not lines:
                                break

                        for line in lines:
                                
                                #print 'total_Line:' + str(total_Line)
                                temp = line.split(',')
                                testcase = temp[2]
                                app = temp[5]
                                result = temp[7]
                                #print testcase
                                #print total_Line
                                if(app == 'Anjuke_SERVER 1-1'):
                                        #print anjuke_total
                                        anjuke_total = anjuke_total + 1
                                        if(result != 'true'):
                                               anjuke_fail = anjuke_fail + 1 
                                        
                                if(app == 'Haozu_SERVER 1-1'):
                                        haozu_total = haozu_total + 1
                                        if(result != 'true'):
                                               haozu_fail = haozu_fail + 1 

                                if(app == 'Aifang_SERVER 1-1'):
                                        aifang_total =  aifang_total + 1
                                        if(result != 'true'):
                                               aifang_fail = aifang_fail + 1 

                                if(app == 'Jingjiren_SERVER 1-1'):
                                        jingjiren_total = jingjiren_total + 1
                                        if(result != 'true'):
                                               jingjiren_fail = jingjiren_fail + 1 

                                # if(app == 'WeChat_SERVER 1-1'):
                                #         wechat_total = wechat_total + 1
                                #         if(result != 'true'):
                                #                wechat_fail = wechat_fail + 1 

                                if(app == 'Wechat_Common 1-1'):
                                        weiliao_total = weiliao_total + 1
                                        if(result != 'true'):
                                               weiliao_fail = weiliao_fail + 1 

                if filePath.count('anjuke.jtl') > 0:
                        #print str(anjuke_total)
                        s = s.replace("anjuke_total" , str(anjuke_total))
                        #s = s.replace("anjuke_fail" , str(anjuke_fail))
                        if(anjuke_fail == 0):
                                s = s.replace('<font>anjuke_fail','<font color="green">' +  '0')
                        else:
                                s = s.replace('<font>anjuke_fail','<font color="red">'  + str(anjuke_fail))
                        s = s.replace("anjuke_pass" , str(int(anjuke_total) - int(anjuke_fail)))
                        temp = str(round((float(anjuke_total) - float(anjuke_fail)) / float(anjuke_total),3)*100)
                        s = s.replace("anjuke_rate" , temp + "%")
                        #print str(int(anjuke_total) - int(anjuke_fail))
                        #print anjuke_fail
                        #print str(((float(anjuke_total) - float(anjuke_fail)) / float(anjuke_total))*100) + "%"
                                        
                if filePath.count('haozu.jtl') > 0:
                        s = s.replace("haozu_total" , str(haozu_total))
                        #s = s.replace("haozu_fail" , str(haozu_fail))
                        if(haozu_fail == 0):
                                s = s.replace('<font>haozu_fail','<font color="green">' +  '0')
                        else:
                                s = s.replace('<font>haozu_fail','<font color="red">'  + str(haozu_fail))
                        s = s.replace("haozu_pass" , str(int(haozu_total) - int(haozu_fail)))
                        temp1 = str(round((float(haozu_total) - float(haozu_fail)) / float(haozu_total),3)*100)
                        s = s.replace("haozu_rate" , temp1 + "%")

                if filePath.count('aifang.jtl') > 0:
                        s = s.replace("aifang_total" , str(aifang_total))
                        #s = s.replace("aifang_fail" , str(aifang_fail))
                        if(aifang_fail == 0):
                                s = s.replace('<font>aifang_fail','<font color="green">' +  '0')
                        else:
                                s = s.replace('<font>aifang_fail','<font color="red">'  + str(aifang_fail))
                        s = s.replace("aifang_pass" , str(int(aifang_total) - int(aifang_fail)))
                        temp2 = str(round((float(aifang_total) - float(aifang_fail)) / float(aifang_total),3)*100)
                        s = s.replace("aifang_rate" , temp2 + "%")

                if filePath.count('jingjiren.jtl') > 0:
                        s = s.replace("jingjiren_total" , str(jingjiren_total))
                        #s = s.replace("jingjiren_fail" , str(jingjiren_fail))
                        if(jingjiren_fail == 0):
                                s = s.replace('<font>jingjiren_fail','<font color="green">' +  '0')
                        else:
                                s = s.replace('<font>jingjiren_fail','<font color="red">'  + str(jingjiren_fail))
                        s = s.replace("jingjiren_pass" , str(int(jingjiren_total) - int(jingjiren_fail)))
                        temp3 = str(round((float(jingjiren_total) - float(jingjiren_fail)) / float(jingjiren_total),3)*100)
                        s = s.replace("jingjiren_rate" , temp3 + "%")

                # # if filePath.count('wechat.jtl') > 0:
                # #         s = s.replace("wechat_total" , str(wechat_total))
                # #         #s = s.replace("wechat_fail" , str(wechat_fail))
                # #         if(wechat_fail == 0):
                # #                 s = s.replace('<font>wechat_fail','<font color="green">' +  '0')
                # #         else:
                # #                 s = s.replace('<font>wechat_fail','<font color="red">'  + str(wechat_fail))
                # #         s = s.replace("wechat_pass" , str(int(wechat_total) - int(wechat_fail)))
                # #         temp4 = str(round((float(wechat_total) - float(wechat_fail)) / float(wechat_total),3)*100)
                #         s = s.replace("wechat_rate" , temp4 + "%")

                if filePath.count('weiliao_common.jtl') > 0:
                        s = s.replace("weiliao_total" , str(weiliao_total))
                        #s = s.replace("wechat_fail" , str(wechat_fail))
                        if(weiliao_fail == 0):
                                s = s.replace('<font>weiliao_fail','<font color="green">' +  '0')
                        else:
                                s = s.replace('<font>weiliao_fail','<font color="red">'  + str(weiliao_fail))
                        s = s.replace("weiliao_pass" , str(int(weiliao_total) - int(weiliao_fail)))
                        temp4 = str(round((float(weiliao_total) - float(weiliao_fail)) / float(weiliao_total),3)*100)
                        s = s.replace("weiliao_rate" , temp4 + "%")
                        
                        

        finally:
                inputfile.close()                

                fileW.write(s)
                fileW.close()                                
        
def GenResult(filePath, genFilePath,times):
        # print "filePath: " + filePath
        genFilePath='results.html'
        inputfile = open(filePath)
        fileR = open(genFilePath, "r")
        s = fileR.read()
        fileR.close()

        fileW = open(genFilePath, "w")
        
        total = 0
        error = [0,0,0,0,0]
        result_List = [([''] * 3) for i in range(10000)]
        anjuke_List = [([0] * 2) for i in range(10000)]
        haozu_List = [([0] * 2) for i in range(10000)]
        aifang_List = [([0] * 2) for i in range(10000)]
        jingjiren_List = [([0] * 2) for i in range(10000)]
        # wechat_List = [([0] * 2) for i in range(10000)]
        weiliao_List = [([0] * 2) for i in range(10000)]
        total_Line = 0
 
	try:
                while 1:                        
                        lines = inputfile.readlines()
                        if not lines:
                                break

                        for line in lines:
                                
                                #print 'total_Line:' + str(total_Line)
                                temp = line.split(',')
                                testcase = temp[2]
                                app = temp[5]
                                result = temp[7]
                                #print total_Line
                                result_List[total_Line][0] = testcase
                                result_List[total_Line][1] = app
                                result_List[total_Line][2] = result

                                total_Line = total_Line + 1
                        #print result_List
                                
                                #myList[api,num]                                
                                #Anjuke_List[i][0] = testcase                                
                                #print "myList[i][0]:" + str(myList[i][0])
                #total_Line = total_Line - 1
                for x in range(0, total_Line):
                        #print x%(total_Line/int(times))
                        #print '--------'
                        #print result_List[x][1] == 'Anjuke_SERVER 1-1' and result_List[x][2] == 'true'
                        if(result_List[x][1] == 'Anjuke_SERVER 1-1'):                                
                                anjuke_List[x%(total_Line/int(times))][0] = result_List[x][0]
                                if(result_List[x][2] != 'true'):
                                        #print x%(total_Line/int(times))
                                        anjuke_List[x%(total_Line/int(times))][1] = anjuke_List[x%(total_Line/int(times))][1] + 1
                        if(result_List[x][1] == 'Haozu_SERVER 1-1'):
                                haozu_List[x%(total_Line/int(times))][0] = result_List[x][0]
                                #print result_List[x][2]
                                if(result_List[x][2] != 'true'):
                                        #print x%(total_Line/int(times))
                                        haozu_List[x%(total_Line/int(times))][1] = haozu_List[x%(total_Line/int(times))][1] + 1

                        if(result_List[x][1] == 'Aifang_SERVER 1-1'):
                                aifang_List[x%(total_Line/int(times))][0] = result_List[x][0]
                                if(result_List[x][2] != 'true'):
                                        aifang_List[x%(total_Line/int(times))][1] = aifang_List[x%(total_Line/int(times))][1] + 1

                        if(result_List[x][1] == 'Jingjiren_SERVER 1-1'):
                                jingjiren_List[x%(total_Line/int(times))][0] = result_List[x][0]
                                if(result_List[x][2] != 'true'):
                                        jingjiren_List[x%(total_Line/int(times))][1] = jingjiren_List[x%(total_Line/int(times))][1] + 1

                        if(result_List[x][1] == 'Wechat_Common 1-1'):            
                                weiliao_List[x%(total_Line/int(times))][0] = result_List[x][0]
                                if(result_List[x][2] != 'true'):
                                        weiliao_List[x%(total_Line/int(times))][1] = weiliao_List[x%(total_Line/int(times))][1] + 1
                                       

                        # if(result_List[x][1] == 'WeChat_SERVER 1-1'):
                        #         wechat_List[x%(total_Line/int(times))][0] = result_List[x][0]
                        #         if(result_List[x][2] != 'true'):
                        #                 wechat_List[x%(total_Line/int(times))][1] = wechat_List[x%(total_Line/int(times))][1] + 1

                if filePath.count('anjuke.jtl') > 0:
                        for i in range(0,total_Line/int(times)):
                                #print '<font>' + str(i) + '_anjuke_result'
                                if(anjuke_List[i][1] == 0):
                                        s = s.replace('<font>' + str(i) + '_anjuke_result','<font color="green">' +  '0 / ' + str(times))
                                else:
                                        s = s.replace('<font>' + str(i) + '_anjuke_result','<font color="red">'  + str(anjuke_List[i][1]) + ' ' + '/ ' + str(times))
                                        
                elif filePath.count('haozu.jtl') > 0:
                        for i in range(0,total_Line/int(times)):
                                if(haozu_List[i][1] == 0):
                                        s = s.replace('<font>' + str(i) + '_haozu_result','<font color="green">' +  '0 / ' + str(times))
                                else:
                                        s = s.replace('<font>' + str(i) + '_haozu_result','<font color="red">'  + str(haozu_List[i][1]) + ' ' + '/ ' + str(times))
                                        
                elif filePath.count('aifang.jtl') > 0:
                        for i in range(0,total_Line/int(times)):
                                if(aifang_List[i][1] == 0):
                                        s = s.replace('<font>' + str(i) + '_aifang_result','<font color="green">' +  '0 / ' + str(times))
                                else:
                                        s = s.replace('<font>' + str(i) + '_aifang_result','<font color="red">'  + str(aifang_List[i][1]) + ' ' + '/ ' + str(times))
                                        
                elif filePath.count('jingjiren.jtl') > 0:
                        for i in range(0,total_Line/int(times)):
                                if(jingjiren_List[i][1] == 0):
                                        s = s.replace('<font>' + str(i) + '_jingjiren_result','<font color="green">' +  '0 / ' + str(times) + ' '  + '</font>')
                                else:
                                        s = s.replace('<font>' + str(i) + '_jingjiren_result','<font color="red">'  + str(jingjiren_List[i][1]) + ' ' + '/ ' + str(times))

                elif filePath.count('weiliao_common.jtl') > 0:
                        for i in range(0,total_Line/int(times)):
                                if(weiliao_List[i][1] == 0):
                                        s = s.replace('<font>' + str(i) + '_weiliao_result','<font color="green">' +  '0 / ' + str(times) + ' '  + '</font>')
                                else:
                                        s = s.replace('<font>' + str(i) + '_weiliao_result','<font color="red">'  + str(weiliao_List[i][1]) + ' ' + '/ ' + str(times))

                # elif filePath.count('wechat.jtl') > 0:
                #         for i in range(0,total_Line/int(times)):
                #                 if(wechat_List[i][1] == 0):
                #                         s = s.replace('<font>' + str(i) + '_wechat_result','<font color="green">' +  '0 / ' + str(times) + ' '  + '</font>')
                #                 else:
                #                         s = s.replace('<font>' + str(i) + '_wechat_result','<font color="red">'  + str(wechat_List[i][1]) + ' ' + '/ ' + str(times))
        


                                        
        finally:
                inputfile.close()                

                fileW.write(s)
                fileW.close()

def ReadConfig():
    # coding=gbk
    print "enter ReadConfig"
    APIDetailDict = {}
    APIDetailList = []
    anjuke_count = 0
    jingjiren_count = 0
    haozu_count = 0
    aifang_count = 0
    weiliao_count = 0
    readoutFp = codecs.open('../APIDetails.txt', 'r', 'UTF-8');
    #here already is unicode, for we have pass "UTF-8" to codecs.open
    try:
        os.remove( 'results.html' )
    except:
        pass
    outputFp = codecs.open("results.html", 'w');
    s='<table border="1"><tr><th colspan=9><caption align="center"><b>API-CI自动化测试报告</b></caption></th></tr><tbody><tr><td width="80" align=center><font>应用模块</font></td><td width="80" align=center><font>API版本</font></td><td width="80" align=center><font>接口名字</font></td><td width="80" align=center><font>接口描述</font></td><td width="170" align=center><font>测试结果（失败/总数）</font></td></tr>'
    try:
                        for line in readoutFp:
                            temp = line.split(' ')
                            if(temp[0].find("安居客")>=0):
                                APIDetailDict = dict(seq=anjuke_count,app=temp[0],ver=temp[1],api=temp[2],desc=temp[3],result=0)
                                APIDetailList.append(APIDetailDict)
                                anjuke_count=anjuke_count+1

                                s=s+'<tr><td width="80" align=center><font>'+ APIDetailDict['app']+'</font></td>'
                                s=s+'<td width="80" align=right><font>'+ APIDetailDict['ver']+'</font></td>'
                                s=s+'<td width="180"><font>'+ APIDetailDict['api']+'</font></td>'
                                s=s+'<td width="260"><font>'+APIDetailDict['desc']+'</font></td>'
                                s=s+'<td width="260"><font>'+ str(APIDetailDict['seq'])+'_anjuke_result'+'</font></td></tr>'
                                # print APIDetailDict['api'] + str(APIDetailDict['seq'])

                            elif(temp[0].find("好租")>=0):
                                #print temp[2]
                                #print haozu_count
                                APIDetailDict = dict(seq=haozu_count,app=temp[0],ver=temp[1],api=temp[2],desc=temp[3],result=0)
                                APIDetailList.append(APIDetailDict)
                                haozu_count=haozu_count+1

                                s=s+'<tr><td width="80" align=center><font>'+ APIDetailDict['app']+'</font></td>'
                                s=s+'<td width="80" align=right><font>'+ APIDetailDict['ver']+'</font></td>'
                                s=s+'<td width="180"><font>'+ APIDetailDict['api']+'</font></td>'
                                s=s+'<td width="260"><font>'+APIDetailDict['desc']+'</font></td>'
                                s=s+'<td width="260"><font>'+ str(APIDetailDict['seq'])+'_haozu_result'+'</font></td></tr>'
                                # print APIDetailDict['api'] + str(APIDetailDict['seq'])

                            elif(temp[0].find("爱房")>=0):
                                APIDetailDict = dict(seq=aifang_count,app=temp[0],ver=temp[1],api=temp[2],desc=temp[3],result=0)
                                APIDetailList.append(APIDetailDict)
                                aifang_count=aifang_count+1

                                s=s+'<tr><td width="80" align=center><font>'+ APIDetailDict['app']+'</font></td>'
                                s=s+'<td width="80" align=right><font>'+ APIDetailDict['ver']+'</font></td>'
                                s=s+'<td width="180"><font>'+ APIDetailDict['api']+'</font></td>'
                                s=s+'<td width="260"><font>'+APIDetailDict['desc']+'</font></td>'
                                s=s+'<td width="260"><font>'+ str(APIDetailDict['seq'])+'_aifang_result'+'</font></td></tr>'
                                # print APIDetailDict['api'] + str(APIDetailDict['seq'])

                            elif(temp[0].find("经纪人")>=0):
                                APIDetailDict = dict(seq=jingjiren_count,app=temp[0],ver=temp[1],api=temp[2],desc=temp[3],result=0)
                                APIDetailList.append(APIDetailDict)
                                jingjiren_count=jingjiren_count+1

                                s=s+'<tr><td width="80" align=center><font>'+ APIDetailDict['app']+'</font></td>'
                                s=s+'<td width="80" align=right><font>'+ APIDetailDict['ver']+'</font></td>'
                                s=s+'<td width="180"><font>'+ APIDetailDict['api']+'</font></td>'
                                s=s+'<td width="260"><font>'+APIDetailDict['desc']+'</font></td>'
                                s=s+'<td width="260"><font>'+ str(APIDetailDict['seq'])+'_jingjiren_result'+'</font></td></tr>'
                                # print APIDetailDict['api'] + str(APIDetailDict['seq'])

                            elif(temp[0].find("微聊")>=0):
                                APIDetailDict = dict(seq=weiliao_count,app=temp[0],ver=temp[1],api=temp[2],desc=temp[3],result=0)
                                APIDetailList.append(APIDetailDict)
                                weiliao_count=weiliao_count+1

                                s=s+'<tr><td width="80" align=center><font>'+ APIDetailDict['app']+'</font></td>'
                                s=s+'<td width="80" align=right><font>'+ APIDetailDict['ver']+'</font></td>'
                                s=s+'<td width="180"><font>'+ APIDetailDict['api']+'</font></td>'
                                s=s+'<td width="260"><font>'+APIDetailDict['desc']+'</font></td>'
                                s=s+'<td width="260"><font>'+ str(APIDetailDict['seq'])+'_weiliao_result'+'</font></td></tr>'
                                # print APIDetailDict['api'] + str(APIDetailDict['seq'])
                        s=s+'</table>'
    finally:
        readoutFp.close();
        outputFp.write(s);
        outputFp.flush();
        outputFp.close();

if __name__ == '__main__':
        filePath = sys.argv[1]
        sumPath = sys.argv[2]
        detailPath = sys.argv[3]
        times = sys.argv[4]
        print "start.."
        GenSummaryResult(filePath, sumPath)
        ReadConfig()
        GenResult("anjuke.jtl", detailPath, times)
        GenResult("haozu.jtl", detailPath, times)
        GenResult("aifang.jtl", detailPath, times)
        GenResult("jingjiren.jtl", detailPath, times)
        GenResult("weiliao_common.jtl", detailPath, times)


