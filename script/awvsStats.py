#coding:utf-8
#author:胖胖小飞侠
def main():
	import requests
	import json
	from requests.packages.urllib3.exceptions import InsecureRequestWarning
	requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
	import script.getauth as getauth
	auth = getauth.main()
	api_url = auth['awvs_url']+'/api/v1/me/stats'
	headers=auth['headers']
	res = requests.get(url= api_url,headers=headers,verify=False).json()
	# print(res)
	scans_conducted_count = res['scans_conducted_count']#总扫描个数
	scans_running_count = res['scans_running_count']#正在扫描的个数
	scans_waiting_count = res['scans_waiting_count']#等待扫描的个数
	targets_count = res['targets_count']#所有任务数量
	top_vulnerabilities = res['top_vulnerabilities']#排名靠前漏洞分布
	vuln_count_by_criticality = res['vuln_count_by_criticality']#通过危险程度进行漏洞等级个数分布
	vuln_count = res['vuln_count']#漏洞数据
	vulnerabilities_open_count = res['vulnerabilities_open_count']#共发现漏洞总数
	print(f'当前总扫描个数为： {scans_conducted_count} 个')
	print(f'当前正在扫描个数为： {scans_running_count} 个')
	print(f'等待扫描的个数为： {scans_waiting_count} 个')
	print(f'总任务数量为： {targets_count} 个')
	print(f'排名靠前漏洞分布情况： {top_vulnerabilities}')
	print(f'通过危险程度进行漏洞等级个数分布情况： {vuln_count_by_criticality}')
	print(f'漏洞数据: {vuln_count} ')
	print(f'发现的漏洞总数： {vulnerabilities_open_count} 个')
