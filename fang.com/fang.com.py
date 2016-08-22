#!/usr/bin/python
#coding=utf-8

import urllib
import urllib2
import json
import time

citys = (
'深圳','上海','北京','广州','南京',
'杭州','福州','天津','武汉','郑州',
'合肥','南昌','济南','昆明','石家庄',
'成都','兰州','南宁','重庆','哈尔滨',
'太原','沈阳','长春','西安','长沙',
'贵阳','苏州','无锡','东莞','惠州')

# 将微秒转为年月
def us2month(us):
    format = '%Y-%m'
    curr_time = time.localtime(us / 1000)
    curr_month = time.strftime(format, curr_time)
    return curr_month


# 将中文编码为'%uXXXX'的特殊URL格式
def urlencode(url):
	url_u = url.decode('utf-8')
	url_u_s = ''
	for i in range(len(url_u)):
		url_u_s = url_u_s + '%u' + hex(ord(url_u[i])).replace('0x', '').upper()
	return url_u_s


if __name__ == '__main__':

	add_date = 0

	now = time.strftime('%Y%m%d-%H%M%S')
	f1 = open('new-house-price_fang.com_' + now + '.csv', 'w')
	f2 = open('2rd-house-price_fang.com_' + now + '.csv', 'w')

	for i in range(len(citys)):
		print 'Getting house price of ' + citys[i].decode('utf-8') + '...'
		city = urlencode(citys[i]);
		url = "http://fangjia.fang.com/pinggu/ajax/chartajax.aspx?dataType=4&city=" + city + "&Class=defaultnew&year=3"
		req = urllib2.Request(url)
		rsp = urllib2.urlopen(req)
		
		data = rsp.read().split('&')
		price_2rd = json.loads(data[0])
		price_new = json.loads(data[1])
		
		# Write date
		if add_date == 0:
			add_date = 1
			for j in range(len(price_new)):
				f1.write(',' + us2month(price_new[j][0]))
				f2.write(',' + us2month(price_new[j][0]))
		
		# Write price
		f1.write('\n' + citys[i])
		for j in range(len(price_new)):
			f1.write(', %d' % price_new[j][1])
			
		f2.write('\n' + citys[i])
		for j in range(len(price_2rd)):
			f2.write(', %d' % price_2rd[j][1])

	f1.close()
	f2.close()

	print 'All done!'






