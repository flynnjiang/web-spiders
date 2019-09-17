#!/usr/bin/python
#coding=utf-8

import importlib

import urllib.parse
import urllib.request

import json
import time
import sys


def query_page(page_num):
	req_url = "http://www.cpppc.org:8086/pppcentral/map/getPPPList.do"
	req_data = bytes(urllib.parse.urlencode({
            'queryPage' : page_num,
            'distStr' : '',
            'induStr' : '',
            'investStr' : '',
            'publTimeStr' : '',
            'projName' : '',
            'sortby' : '',
            'orderby' : '',
            'stageArr' : '',
            'projStateType' : 1
        }), encoding='utf-8')
	rsp = urllib.request.urlopen(url = req_url, data = req_data)
	return rsp.read().decode('utf-8')

	
def main():
	importlib.reload(sys)
	#sys.setdefaultencoding('utf-8')

	# get pages
	data = json.loads(query_page(1))
	total_page = data['totalPage']
	print("total_page = %d" % total_page)
	
	fp = open('ppp_projects_' + time.strftime('%Y%m%d-%H%M%S') + '.csv', 'w', 1)
	fp.write('项目编号,项目名称,类别1,类别2,阶段,区域1,区域2,偿付模式,金额（万）,创建时间,更新时间,项目引用编号\n')

	for i in range(1, total_page):
		print("getting page %d/%d..." % (i, total_page))

		data = json.loads(query_page(i))
		projects = data['list']
		for j in range(len(projects)):
			print("saving project: " + projects[j]['PROJ_NAME'])
			
			# these maybe null
			if (projects[j]['IVALUE2'] == None):
				ivalue2 = ""
			else:
				ivalue2 = projects[j]['IVALUE2']
				
			if (projects[j]['UPDATING_TIME'] == None):
				updating_time = ""
			else:
				updating_time = projects[j]['UPDATING_TIME']
			
			# write to file
			fp.write(
				projects[j]['PROJ_NO'] + ','
			  + projects[j]['PROJ_NAME'] + ','
			  + projects[j]['IVALUE'] + ','
			  + ivalue2 + ','
			  + projects[j]['PROJ_STATE_NAME'] + ','
			  + projects[j]['PRV1'] + ','
			  + projects[j]['PRV2'] + ','
			  + projects[j]['RETURN_MODE_NAME'] + ','
			  + str(projects[j]['INVEST_COUNT']) + ','
			  + projects[j]['CREATING_TIME'] + ','
			  + updating_time + ','
			  + projects[j]['PROJ_RID'] + '\n')

	fp.close()

	print("All done!")
	
if __name__ == '__main__':
	main()