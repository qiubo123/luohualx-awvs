#coding:utf-8
#author:胖胖小飞侠
#从文件读取target信息
import script.add_one_target as add_one_target
def main(filename):
	targets_id = []
	if '.txt' in filename:
		with open(filename,'r',encoding='utf-8') as f:
			for i in  f:
				i = i.strip().split(';')
				url = i[0]
				desc = i[1]
				print(f'[+]正在添加\t{desc}\t --> \t{url}')
				tid = add_one_target.main(url,desc)
				targets_id.append(tid)
	
	if '.csv' in filename:
		import csv
		with open(filename,'r') as f:
			reader = csv.reader(f)
			for row in reader:
				url = row[0]
				desc = row[1]
				print(f'[+]正在添加\t{desc}\t --> \t{url}')
				tid = add_one_target.main(url,desc)
				targets_id.append(tid)
	return targets_id