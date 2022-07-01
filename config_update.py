import shutil
imoprt os
print(1)
print os.getcwd() #获取当前工作目录路径
print os.path.abspath('.') #获取当前文件目录路径
print os.path.abspath('raw_main_config.sh') #获取当前目录文件下的文件目录路径
shutil.move("/root/ql/scripts/raw_main_config.sh", "/root/ql/config/config.sh")
