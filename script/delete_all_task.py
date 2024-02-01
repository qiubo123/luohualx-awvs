#coding:utf-8
#author:胖胖小飞侠
import script.delete_one_task as deleteOneTask
import json
def targets():
	with open('./data/targets.json','r',encoding='utf-8') as f:
		details = json.load(f)
		for d in details:
			target_id = d['target_id']
			deleteOneTask.target(target_id)
def scans():
	with open('./data/scans.json','r',encoding='utf-8') as f:
		details = json.load(f)
		for d in details:
			scan_id = d['scan_id']
			deleteOneTask.scan(scan_id)
def reports():
	with open('./data/reports.json','r',encoding='utf-8') as f:
		details = json.load(f)
		# print(details)
		for d in details:
			report_id = d['report_id']
			print(f'[+]正在删除 {report_id}')
			deleteOneTask.report(report_id)
def main():
	targets()
	scans()
	reports()