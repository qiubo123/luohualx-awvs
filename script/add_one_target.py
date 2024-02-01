#coding:utf-8
#author:胖胖小飞侠
#添加一个扫描目标和描述
def main(url,desc='默认任务'):
	import json
	import requests
	from requests.packages.urllib3.exceptions import InsecureRequestWarning
	requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
	import script.getauth as getauth
	auth = getauth.main()
	# print(auth['headers'])
	api_url = auth['awvs_url']+'/api/v1/targets'
	headers=auth['headers']
	data = {
		"address": url,
		"description": desc,
		"criticality": "10"
	}
	data_json = json.dumps(data)
	r = requests.post(url=api_url, headers=headers, data=data_json, verify=False)
	# print(r.json())
	if r.status_code == 201:
		target_id = r.json().get("target_id")
		print(f'[+]目标添加成功,target_id: {target_id}')
	else:
		print('[+]目标添加失败')
	return target_id