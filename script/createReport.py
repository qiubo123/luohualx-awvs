#coding:utf-8
#author:胖胖小飞侠
#生成漏洞扫描报告
import json
import os
def creat_report(id):
	import requests
	from requests.packages.urllib3.exceptions import InsecureRequestWarning
	requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
	import script.getauth as getauth
	auth = getauth.main()
	api_url = auth['awvs_url']+'/api/v1/reports'
	headers=auth['headers']
	data = {
		"template_id":"11111111-1111-1111-1111-111111111115",
		"source":{
			"list_type":"targets",
			"id_list":[id]
		}
	}
	data_json = json.dumps(data)
	r = requests.post(api_url,headers=headers,data=data_json,verify=False)
	print(r.json())
def main():
	file_path = 'data' + os.sep + 'scans.json'
	with open(file_path,'r') as file:
		data = json.load(file)
		for d in data:
			target_id = d['target_id']
			print(target_id)
			creat_report(target_id)
