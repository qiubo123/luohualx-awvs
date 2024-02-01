#coding:utf-8
#author:胖胖小飞侠
def main(tar_id):
	import requests
	import json
	from requests.packages.urllib3.exceptions import InsecureRequestWarning
	requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
	import script.getauth as getauth
	auth = getauth.main()
	api_url = auth['awvs_url']+'/api/v1/scans'
	headers=auth['headers']
	data = {
		"target_id": tar_id,
		"profile_id": "11111111-1111-1111-1111-111111111111",
		"schedule":
			{"disable": False,
			"start_date": None,
			"time_sensitive": False
			}
	}
	data_json = json.dumps(data)
	r = requests.post(url=api_url, headers=headers, data=data_json, verify=False)
	print(f'[+]{tar_id}\t添加成功')
	target_id = r.json().get('target_id')
	scan_id = r.json().get('scan_id')
	# print(f'[+]target_id:\t{target_id}')
	# print(f'[+]scan_id:\t{scan_id}')
	scan = {}
	scan['target_id'] = target_id
	scan['scan_id'] = scan_id
	return scan