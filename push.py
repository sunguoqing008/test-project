# coding = UTF-8
import os
import time

'''
	遍历hall37的项目,并pull
'''

projectDir = '/home/qipai/hall37/source/'

for p in os.listdir(projectDir):
	if os.path.isdir(projectDir + str(p)):
		os.chdir(projectDir + str(p))
		print 'start pull \033[1;31m' + str(p) + '\033[0m!'
		os.system('git pull')
		#print os.getcwd()
		time.sleep(2)
		print 'finish pull \033[1;35m' + str(p) + '\033[0m!'
		os.chdir(projectDir)
