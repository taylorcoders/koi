 #导入shutil模块和os模块
import shutil,os
 


 
#重命名文件
shutil.move("\\root\\ql\\scripts\\raw_main_config.sh","\\root\\ql\\scripts\\config.sh")
#移动文件
shutil.move("\\root\\ql\\scripts\\config.sh","\\root\\ql\\config\\config.sh")
