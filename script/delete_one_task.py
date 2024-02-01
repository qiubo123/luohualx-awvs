#coding:utf-8
#author:胖胖小飞侠
#根据target_id 删除一个扫描目标
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
import script.getauth as getauth
auth = getauth.main()
headers=auth['headers']
def target(target_id):
	api_url = auth['awvs_url']+'/api/v1/targets/'+target_id
	resp = requests.delete(api_url,headers=headers,verify=False)
	if resp.status_code == 204:
		print(f'[+]任务删除成功 {target_id}！')
	else:
		print('[+]任务删除失败！')
def scan(scan_id):
	api_url = auth['awvs_url']+'/api/v1/scans/'+scan_id
	resp = requests.delete(api_url,headers=headers,verify=False)
	if resp.status_code == 204:
		print(f'[+]任务删除成功 {scan_id}')
	else:
		print('[+]任务删除失败！')
def report(report_id):
	# print(report_id)
	api_url = auth['awvs_url']+'/api/v1/reports/'+report_id
	resp = requests.delete(api_url,headers=headers,verify=False)
	# print(resp)
	if resp.status_code == 204:
		print(f'[+]任务删除成功 {report_id}')
	else:
		print('[+]任务删除失败！')