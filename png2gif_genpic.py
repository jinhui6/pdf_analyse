import os
import matplotlib.pyplot as plt

def png2gif():
    dirName = os.getcwd()  # 获得当前工作目录
    li = os.listdir(dirName)  # 将当前目录下所有文件名，存入 ls[] 列表
    for filename in li:         #li[] 列表每个单独给 filename
        newname = filename
        newname = newname.split(".")
        if newname[-1]=="png":
            newname[-1]="gif"
            newname = '.'.join(newname)     #将newname['xxx','gif']  == newname['xxx.gif']

            filename = dirName + '\\' + filename
            newname = dirName + '\\' + newname

            os.rename(filename,newname)
            #print (newname,"updated successfully")

def save_pic(s):
    fig = plt.gcf()
    fig.set_size_inches(4.0, 2.5)
    fig.savefig(s, dpi=100)


png2gif()