# -*- coding: utf8 –*-
import requests
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

patt=re.compile(u"([\u4e00-\u9fa5]+)")

f = open('position.txt', 'w')

china_url = 'http://webservice.webxml.com.cn/WebServices/WeatherWS.asmx/getRegionProvince'
s_0 = requests.get(china_url)
p_0 = patt.findall(s_0.text)
for province in p_0:
	f.write('中国, ' + province + '\n')
country_url = 'http://webservice.webxml.com.cn/WebServices/WeatherWS.asmx/getRegionCountry'
s_1 = requests.get(country_url)
p_1 = patt.findall(s_1.text)
BASE_URL = 'http://webservice.webxml.com.cn/WebServices/WeatherWS.asmx/getSupportCityString?theRegionCode={}'
for pos in p_1:
	print pos
	url = BASE_URL.format(pos)
	s_2 = requests.get(url)
	p_2 = patt.findall(s_2.text)
	for city in p_2:
		if '无城市' == city:
			f.write(pos + ', ' + '\n')
			break
		f.write(pos + ', ' + city + '\n')
f.close()