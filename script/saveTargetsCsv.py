#coding:utf-8
#author:胖胖小飞侠
#导出当前所有target
def main():
	import time
	import csv
	import json
	import os
	today = time.strftime('_%Y_%m_%d')
	filename = 'data'+ os.sep+'targets' + today + '.csv'
	print(f'[+]{filename}')
	csvfile = open(filename,'w',encoding='utf-8',newline='')
	writer = csv.writer(csvfile)
	writer.writerow(['名称','地址','targetID'])
	with open('./data/targets.json','r',encoding='utf-8') as f:
		details = json.load(f)
	# print(type(details))
	for d in details:
		# print(d)
		addr_name = d['addr_name']
		address = d['address']
		target_id = d['target_id']
		data = [addr_name,address,target_id]
		writer.writerow(data)
	csvfile.close()
	print(f'[+]导出成功 {filename}')
