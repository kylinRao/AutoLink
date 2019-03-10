#coding=utf-8
####定义单例的日志logger模块
import configparser
import  logging
import logging.config
import os,path

# cf = ConfigParser.ConfigParser()
# cf.read(os.path.join(os.path.dirname(__file__),'conf','global.conf'))  # 读配置文件（ini、conf）返回结果是列表
# cf.sections()  # 获取读到的所有sections(域)，返回列表类型
# logconfigPath = cf.get(cf.get('global', 'envType'),'logConfig')
# print logconfigPath
class logControl:
	# printos.path.abspath(__file__)
	##create logger

	logging.config.fileConfig(os.path.join(os.path.dirname(os.path.abspath(__file__)), "conf", 'logger.conf'))

	def __init__(self):
		self.runLogHandle = logControl.getLogger("run")

	def getLogger(self,logerType="run"):
		logger = logging.getLogger(logerType)
		return logger



