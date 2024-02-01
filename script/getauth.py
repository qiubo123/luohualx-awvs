#coding:utf-8
#author:胖胖小飞侠
def main():
	import os
	import configparser
	# conf = 'script' + os.sep + 'config.conf'
	conf = 'config' + os.sep + 'config.conf'
	config = configparser.ConfigParser()
	config.read(conf,encoding='utf-8')
	awvs_url = config.get('awvsapi','awvs_url')
	apikey = config.get('awvsapi','apikey')
	headers = {
		"X-Auth": apikey,
		"Content-type": "application/json;charset=utf8"
	}
	auth = {}
	auth['awvs_url'] = awvs_url
	# auth['apikey'] = apikey
	auth['headers'] = headers
	# print(auth)
	return auth
# main()
