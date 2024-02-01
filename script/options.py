#coding:utf-8
#author:胖胖小飞侠
import argparse
def main():
	parser = argparse.ArgumentParser(description='帮助信息！如有问题可联系胖胖小飞侠解决!欢迎使用luohualx系列脚本！')
	parser.add_argument('-i','--initfolder',action='store_true',default=False,help='初始化文件夹')
	parser.add_argument('-aot','--add-one-target',type=str,required=False,help='添加扫描目标')
	parser.add_argument('-ds','--desc',type=str,required=False,help='目标描述,配合“-a”使用')
	parser.add_argument('-dti','--delete-target-id',type=str,required=False,help='待删除的target-id')
	parser.add_argument('-dsi','--delete-scan-id',type=str,required=False,help='待删除的scan-id')
	parser.add_argument('-dri','--delete-report-id',type=str,required=False,help='待删除的scan-id')
	parser.add_argument('-stj','--save-targets-json',action='store_true',default=False,help='生成target信息的json配置文件')
	parser.add_argument('-ssj','--save-scans-json',action='store_true',default=False,help='生成scan信息的json配置文件')
	parser.add_argument('-srj','--save-reports-json',action='store_true',default=False,help='导出报告信息')
	parser.add_argument('-stc','--save-targets-csv',action='store_true',default=False,help='导出目标地址信息csv文件')
	parser.add_argument('-sall','--save-all',action='store_true',default=False,help='一键导出当前所有信息')
	parser.add_argument('-sos','--start-one-scan',type=str,help='启动扫描单个，后跟target_id')
	parser.add_argument('-tn','--target-number',action='store_true',default=False,help='查看总任务数量')
	parser.add_argument('-dtc','--download-template-csv',action='store_true',default=False,help='下载target样例（csv和txt格式）')
	parser.add_argument('-f','--file',type=str,required=False,help='批量导入target信息文件（支持csv和txt格式，可按照样例文件填写）')
	# parser.add_argument('-sai','--start-all-id',action='store_true',default=False,help='批量扫描目标')
	parser.add_argument('-dat','--delete-all-target',action='store_true',default=False,help='删除所有扫描目标')
	parser.add_argument('-das','--delete-all-scan',action='store_true',default=False,help='删除所有扫描任务')
	parser.add_argument('-dar','--delete-all-report',action='store_true',default=False,help='删除所有扫描报告')
	parser.add_argument('-clean',type=str,required=False,help='清空所有信息，请谨慎使用')
	parser.add_argument('-car','--create-all-report',action='store_true',default=False,help='生成所有报告,生成后才可导出报告')
	parser.add_argument('-eap','--export-all-report',action='store_true',default=False,help='导出所有报告,必须先执行生成报告')
	args = parser.parse_args()
	return args