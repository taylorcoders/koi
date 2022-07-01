 #导入shutil模块和os模块
import shutil,os
 

#test
#os.rename('raw_main_config.sh', 'config.sh') # 重命名文件
#重命名文件
#shutil.move("\\root\\ql\\scripts\\raw_main_config.sh","\\root\\ql\\scripts\\config.sh")
#移动文件
shutil.move(r'.\raw_main_config.sh', r'.\config/config.sh')
