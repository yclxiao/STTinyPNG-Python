#-*- encoding: UTF-8 -*-

import tinify
import os
import os.path

#tiny官网注册的key
tinify.key = "saO2EtqhoHCfVlbYxHvf-NITmTNX2sXr"

#文件源路径
fromFilePath = "/Users/yclxiao/Project/python/STTinyPNG-Python/big"
#文件目标路径
toFilePath = "/Users/yclxiao/Project/python/STTinyPNG-Python/bignew"

#遍历每一层路径  root是指遍历的文件目录
for root, dirs, files in os.walk(fromFilePath):
	for name in files:
		fileName, fileSuffix = os.path.splitext(name)
		if fileSuffix == '.png' or fileSuffix == '.jpg':

			print root

			toFullPath = toFilePath + root[len(fromFilePath):]
			toFullName = toFullPath + '/' + name

			fromFullPath = fromFilePath + root[len(fromFilePath):]
			fromFullName = fromFullPath + '/' + name

			#如果目录不存在则创建
			if os.path.exists(toFullPath):
				pass
			else:
				os.mkdir(toFullPath)

			#利用tiny的的api进行图片压缩
			source = tinify.from_file(fromFullName)
			source.to_file(toFullName)
