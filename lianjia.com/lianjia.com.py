#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

import urllib
import urllib2
import json
import time




cities = (
{'id':'bj', 'name':'北京'},
{'id':'cd', 'name':'成都'},
{'id':'cq', 'name':'重庆'},
{'id':'cs', 'name':'长沙'},
{'id':'dl', 'name':'大连'},
#{'id':'dg', 'name':'东莞'},
#{'id':'fs', 'name':'佛山'},
{'id':'gz', 'name':'广州'},
{'id':'hz', 'name':'杭州'},
#{'id':'hui', 'name':'惠州'},
#{'id':'hk', 'name':'海口'},
{'id':'jn', 'name':'济南'},
#{'id':'jx', 'name':'嘉兴'},
#{'id':'lin', 'name':'临沂'},
{'id':'nj', 'name':'南京'},
#{'id':'nt', 'name':'南通'},
{'id':'qd', 'name':'青岛'},
#{'id':'sh', 'name':'上海'},
{'id':'sz', 'name':'深圳'},
#{'id':'su', 'name':'苏州'},
#{'id':'sjz', 'name':'石家庄'},
#{'id':'sy', 'name':'沈阳'},
#{'id':'san', 'name':'三亚'},
{'id':'tj', 'name':'天津'},
#{'id':'ts', 'name':'唐山'},
#{'id':'ty', 'name':'太原'},
{'id':'wh', 'name':'武汉'},
#{'id':'wz', 'name':'温州'},
#{'id':'wf', 'name':'潍坊'},
#{'id':'wx', 'name':'无锡'},
{'id':'xm', 'name':'厦门'},
#{'id':'xx', 'name':'西安'},
#{'id':'yt', 'name':'烟台'},
#{'id':'yz', 'name':'扬州'},
#{'id':'zs', 'name':'中山'},
#{'id':'zh', 'name':'珠海'}
)

# 成交均价、挂牌均价、成交量、新增房源量、新增客源量、带看量

# http://cs.lianjia.com/fangjia/priceTrend/
# http://cs.lianjia.com/fangjia/priceTrend/?analysis=1
# http://cs.lianjia.com/fangjia/priceTrend/?analysis=1&duration=day
# 城市分区价格
# http://cs.lianjia.com/fangjia/priceMap/




if __name__ == '__main__':

	add_date = 0

	now = time.strftime('%Y%m%d-%H%M%S')
	fp_qtt = open('lianjia.com_quantity_' + now + '.csv', 'w')
	fp_price = open('lianjia.com_price_' + now + '.csv', 'w')
	fp_list_price = open('lianjia.com_listprice_' + now + '.csv', 'w')
	#fp_house = open('lianjia.com_house_' + now + '.csv', 'w')
	#fp_customer = open('lianjia.com_customer_' + now + '.csv', 'w')
	#fp_show = open('lianjia.com_show_' + now + '.csv', 'w')


	for i in range(len(cities)):
		print 'Getting house price of ' + cities[i]['name'].decode('utf-8') + '...'
		url = "http://" + cities[i]['id'] + ".lianjia.com/fangjia/priceTrend/"
		#url2 = "http://" + cities[i]['id'] + ".lianjia.com/fangjia/priceTrend/?analysis=1"

		req = urllib2.Request(url)
		rsp = urllib2.urlopen(req)
		data = json.loads(rsp.read())
		
		month_array = data['currentLevel']['month']
		price_array = data['currentLevel']['dealPrice']['total']
		list_price_array = data['currentLevel']['listPrice']['total']
		quantity_array = data['currentLevel']['quantity']['total']
		
		#req = urllib2.Request(url2)
		#rsp = urllib2.urlopen(req)
		#data = json.loads(rsp.read())
		
		#house_cnt_array = data['houseAmount']
		#customer_cnt_array = data['customerAmount']
		#show_cnt_array = data['showAmount']
		
		# Write date
		if add_date == 0:
			add_date = 1
			for j in range(len(month_array)):
				fp_price.write(', %s' % month_array[j].encode('utf-8'))
				fp_list_price.write(', %s' % month_array[j].encode('utf-8'))
				fp_qtt.write(', %s' % month_array[j].encode('utf-8'))
				#fp_house.write(', %s' % month_array[j].encode('utf-8'))
				#fp_customer.write(', %s' % month_array[j].encode('utf-8'))
				#fp_show.write(', %s' % month_array[j].encode('utf-8'))
		
		# Write price
		fp_price.write('\n' + cities[i]['name'])
		fp_list_price.write('\n' + cities[i]['name'])
		fp_qtt.write('\n' + cities[i]['name'])
		#fp_house.write('\n' + cities[i]['name'])
		#fp_customer.write('\n' + cities[i]['name'])
		#fp_show.write('\n' + cities[i]['name'])
		for j in range(len(month_array)):
			fp_price.write(', %s' % price_array[j])
			fp_list_price.write(', %s' % list_price_array[j])
			fp_qtt.write(', %s' % quantity_array[j])
			#fp_house.write(', %s' % house_cnt_array[j])
			#fp_customer.write(', %s' % customer_cnt_array[j])
			#fp_show.write(', %s' % show_cnt_array[j])


	fp_price.close()
	fp_list_price.close()
	fp_qtt.close()
	#fp_house.close()
	#fp_customer.close()
	#fp_show.close()

	print 'All done!'






