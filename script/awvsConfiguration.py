#coding:utf-8
#author:胖胖小飞侠
#生成所有target、scan、report的id文件
import requests
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
import script.getauth as getauth
auth = getauth.main()
target_api_url = auth['awvs_url']+'/api/v1/targets'
scan_api_url = auth['awvs_url']+'/api/v1/scans'
report_api_url = auth['awvs_url']+'/api/v1/reports'
headers = auth['headers']
def targets():
	r = requests.get(url=target_api_url, headers=headers, verify=False).json()
	count = r['pagination']['count']#总目标数
	page = count/100
	intpage = int(page)
	if page > intpage:
		intpage = intpage + 1
	# print(intpage)#目标总页数
	print(f'[+]当前共有目标：{count}\n[+]总页数：{intpage}')
	upath = [target_api_url+"?c="+str(i*100)+'&l=100' for i in range(0,intpage+1)]
	i = 0#计数和标志
	details = []
	for u in upath:
		res = requests.get(url=u, headers=headers, verify=False).json()
		targets = res['targets']
		for t in targets:
			detail = {}
			i = i + 1
			detail['num'] = i
			detail['addr_name'] = t['description']
			detail['address'] = t['address']
			detail['target_id'] =  t['target_id']
			detail['severity_counts'] = t['severity_counts']
			details.append(detail)
	with open('./data/targets.json','w',encoding='utf-8') as f:
		json.dump(details,f)
		print('[+]targets.json文件生成成功！')
def scans():
	r = requests.get(url=scan_api_url, headers=headers, verify=False).json()
	count = r['pagination']['count']
	page = count/100
	intpage = int(page)
	if page > intpage:
		intpage = intpage + 1#目标总页数
	print(f'[+]当前共有目标：{count}\n[+]总页数：{intpage}')
	upath = [scan_api_url+"?c="+str(i*100)+'&l=100' for i in range(0,intpage)]
	i = 0#计数和标志
	details = []
	for u in upath:
		res = requests.get(url=u, headers=headers, verify=False).json()
		# print(res)
		scans = res['scans']
		for s in scans:
			detail = {}
			detail['address'] = s['target']['address']
			detail['description'] = s['target']['description']
			detail['target_id'] = s['target_id']
			detail['scan_id'] = s['scan_id']
			detail['scan_session_id'] = s['current_session']['scan_session_id']#
			detail['severity_counts'] = s['current_session']['severity_counts']#漏洞等级
			details.append(detail)
	# print(details)
	with open('./data/scans.json','w',encoding='utf-8') as f:
		json.dump(details,f)
		print('[+]scans.json文件生成成功！')
def reports():
	r = requests.get(url=report_api_url, headers=headers, verify=False).json()
	count = r['pagination']['count']
	page = count/100
	intpage = int(page)
	if page > intpage:
		intpage = intpage + 1#目标总页数
	upath = [report_api_url+"?c="+str(i*100)+'&l=100' for i in range(0,intpage)]
	report_list = []
	for u in upath:
		res = requests.get(url=u, headers=headers, verify=False).json()
		# print(res)
		details = res['reports']
		for detail in details:
			# break
			report = {}
			report['download_url'] = auth['awvs_url']+detail['download'][1]#0为下载html的地址
			generation_date = detail['generation_date'][0:10]
			description = detail['source']['description'].split(';')[1].replace('/','-')
			report['report_id'] = detail['report_id']
			report['report_file_name'] = generation_date + '_' + description + '.pdf'
			report_list.append(report)
	with open('./data/reports.json','w',encoding='utf-8') as f:
		json.dump(report_list,f)
		print('[+]reports.json文件生成成功！')
	return report_list
def PDF():
	import os
	import time
	report_list = reports()
	count = len(report_list)
	i = 1#计数和标志
	for r in report_list:
		url = r['download_url']
		report_name = r['report_file_name']
		res = requests.get(url,headers=headers,verify=False)
		savepath = 'report' + os.sep + report_name
		print(f'[+]共有 {count} 个报告待下载，正在下载第 {i} 个')
		print(f'[+]当前正在下载 {report_name}')
		i = i + 1
		with open(savepath,"wb") as fp:
			fp.write(res.content)
			time.sleep(1)
def main():
	targets()
	scans()
	reports()

	