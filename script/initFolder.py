#coding:utf-8
#author:胖胖小飞侠
#检查文件夹是否存在，不存在则创建文件夹，用在脚本初始化
import os
def main():
	folders = ['data','report']
	for f in folders:
		if not os.path.exists(f):
			os.makedirs(f)