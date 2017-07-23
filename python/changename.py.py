#导入os模块
import os,sys

#取出当前工作目录里的文件名列表。
filenames=os.listdir(os.getcwd())

#在1.bmp到9.bmp的文件名前加0
#len()返回filenames列表的长度，xrange()返回一个从0开始到filenames列表的长度n的数列用于循环。
for num in range(len(filenames)):

    #用if判断语句排除程序文件本身
    #使用os模块中的rename(oldName, newName)函数来更改文件名。
    #0到9的前十个文件名钱加0，即00.bmp 01.bmp...
    #str()函数返回数值类型变量的字符串
    #第二个if语句中依然要注意行首的缩进
    if filenames[num]!='changeall.py':
        if num<10:
            os.rename(filenames[num],'0'+str(num)+'.bmp')
        else:
            os.rename(filenames[num],str(num)+'.bmp')