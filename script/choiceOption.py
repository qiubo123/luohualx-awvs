#coding:utf-8
#author:胖胖小飞侠
import os
import script.banner as banner
import script.options as options
# import script.getTargets as getTargets
import script.saveTargetsCsv as saveTargetsCsv
import script.add_one_target as add_one_target
import script.add_file_target as add_file_target
import script.delete_one_task as delete_one_task
import script.delete_all_task as delete_all_task
import script.createReport as createReport
import script.ceshi as ceshi
import script.download_template as template
import script.start_one_scan as start_one_scan
import script.awvsConfiguration as awvsConfig
import script.awvsStats as stats

def main():
	banner.main()
	args = options.main()
	if vars(args)['target_number'] == True:
		stats.main()
		exit()
	if vars(args)['download_template_csv'] == True:#生成模板文件
		template.main()
	if vars(args)['start_one_scan'] != None:#启动一个扫描
		target_id = vars(args)['start-one-scan']
		start_one_scan.main(tagetr_id)
	if vars(args)['create_all_report'] == True:#生成报告但不下载
		# ceshi.main()
		createReport.main()
######################################################
	if vars(args)['save_targets_csv'] == True:#导出扫描目标信息
		saveTargetsCsv.main()
		exit()
	if vars(args)['save_targets_json'] == True:
		awvsConfig.targets()
		exit()
	if vars(args)['save_scans_json'] == True:#导出扫描目标信息
		# saveScansJson.main()
		awvsConfig.scans()
		exit()
	if vars(args)['save_reports_json'] == True:#导出报告信息
		# saveScansJson.main()
		awvsConfig.reports()
		exit()
	if vars(args)['export_all_report'] == True:#导出所有报告
		awvsConfig.PDF()
		exit()
	if vars(args)['save_all'] == True:#一键导出当前所有信息
		awvsConfig.main()
		exit()
######################################################
	if vars(args)['add_one_target'] != None:
		target_url = vars(args)['add_one_target']#添加单个地址
		if vars(args)['desc'] != None:
			url_desc = vars(args)['desc']#目标描述
		else:
			url_desc = target_url
		target_id = add_one_target.main(target_url,url_desc)
		print(f'[+]目标地址为：{target_url}')
		print(f'[+]目标描述为：{url_desc}')
		print(f'[+]目标描述为：{target_id}')
		result = input('[+]添加完成，是否扫描（Y）:')
		if result == 'y' or result == 'Y' or result == 'yes' or result == 'YES':
			start_one_scan.main(target_id)
	if vars(args)['file'] != None:#导入target信息文件
		filename = vars(args)['file']
		tids =add_file_target.main(filename)#获取添加目标后的target_id
		result = input('[+]添加完成，是否扫描（Y）:')
		if result == 'y' or result == 'Y' or result == 'yes' or result == 'YES':
			#遍历target添加结果，获取target_id,将target_id传入扫描任务
			for tid in tids:
				start_one_scan.main(tid)
		else:
			print('[+]您未选择继续扫描！')
			exit()
######################################################
	if vars(args)['delete_target_id'] != None:#删除一个扫描目标
		target_id = vars(args)['delete_target_id']
		delete_one_task.target(target_id)
	if vars(args)['delete_scan_id'] != None:
		scan_id = vars(args)['delete_scan_id']#删除一个扫描任务
		delete_one_task.scan(scan_id)
	if vars(args)['delete_report_id'] != None:#删除一个报告
		report_id = vars(args)['delete_report_id']
		delete_one_task.report(report_id)
	if vars(args)['delete_all_target'] == True:#删除所有扫描目标
		delete_all_task.targets()
	if vars(args)['delete_all_scan'] == True:#删除所有扫描任务
		delete_all_task.scans()
	if vars(args)['delete_all_report'] == True:#删除所有扫描任务
		delete_all_task.reports()
	if vars(args)['clean'] == True:#删除所有报告
		delete_all_task.main()
######################################################
	
	
	# if vars(args)['ceshi'] != None:#
	# 	filename = vars(args)['ceshi']
	# 	add_file_target.main(filename)
	# if vars(args)['cs'] == True:#
	# 	add_file_target.main()
