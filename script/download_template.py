#coding:utf-8
#author:胖胖小飞侠
#下载target模板文件
import os
def csv():
	import csv
	file_name = 'targets-template.csv'
	exist = False
	for root,dirs,files in os.walk('./'):
		for filename in files:
			if file_name == filename:
				print(f'[+]{file_name}已存在！')
				exist = True			
		break
	if exist == False:
		csvfile = open(file_name,'w',encoding='utf-8',newline='')
		writer = csv.writer(csvfile)
		name = 'http://www.baidu.com'
		dizhi = '百度搜索主页'
		writer.writerow([name,dizhi])
		csvfile.close()
		print(f'[+]{file_name}模板导出成功')
	
def txt():
	file_name = 'targets-template.txt'
	exist = False
	for root,dirs,files in os.walk('./'):
		for filename in files:
			if file_name == filename:
				print(f'[+]{file_name}已存在！')
				exist = True
		break
	if exist == False:
		with open(file_name,'w',encoding='utf-8') as f:
			f.write('域名;资产名\n')
			f.write('#请删除本行，域名和资产名之间以英文分号“;”作为分隔符\n')
			f.write('http://www.baidu.com;百度搜索主页\n')
			print(f'[+]{file_name}模板导出成功')
def main():
	txt()
	csv()
	
	
