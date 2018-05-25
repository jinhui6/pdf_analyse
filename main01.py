from tkinter import *
from png2gif_genpic import png2gif,save_pic
import os
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import tkinter.messagebox

#　根窗口
root = Tk()
root.title('2017224005--yjh') #主窗口标题
root.geometry('900x800')  #主窗口大小，中间的为英文字母x
root.maxsize(900, 800)  # 固定尺寸900x700
root.minsize(900, 800)  # 固定尺寸900x700


# 变量定义
x=[]        # 全局变量 x[]
var1 = StringVar()
var2 = StringVar()
var3 = StringVar() # 拿来循环get_entry_input()
var4 = StringVar()   # 从entry里面取数的变量



def ecdf(data):
    """Compute ECDF for a one-dimensional array of measurements."""
    # Number of data points: n
    n = len(data)
    # x-data for the ECDF: x
    x = np.sort(data)       #将x由小到大排列
    # y-data for the ECDF: y
    y = np.arange(1, n+1) / n       #生成50个等差数列，间距为1/50=0.02   ==y
    return x, y #返回类型是array([1, 2, 3.....])
def fig15(y):
    yy = y
    for x in yy:
        if 0.1501 <= x <= 0.1699:       #最大只能判断10000个数
            return y.index(x)
def fig85(y):
    yy = y
    for xx in yy:
        if 0.8501 <= xx <= 0.8699:       #最大只能判断10000个数
            return yy.index(xx)


def cout(sma1,sma2):
    fre=0
    for s in x:
        if sma1<= s< sma2:
            fre+=1
#    print('该组频数=',fre)
    return fre/len(x)
def mid(sma,big):
    y=sma+(big-sma)/2
#    print('中值inter',y)
    return y

def png222gif():
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

def paint_normal_pdf():

    xx=x
    mu=np.mean(xx)   #计算 mu
    sigma=np.std(xx) #计算标准差sigma
    xa = mu + sigma * np.random.randn(10000) #在均值周围产生符合正态分布的x值
    num_bins = 50
    n, bins, patches = plt.hist(xa, num_bins, normed=1, facecolor='green', alpha=0.5)
    #直方图函数，x为x轴的值，normed=1表示为概率密度，即和为一，绿色方块，色深参数0.5.返回n个概率，直方块左边线的x值，及各个方块对象

    y = mlab.normpdf(bins, mu, sigma)   #画一条逼近的曲线
    plt.plot(bins, y, 'r--')
    plt.xlabel('Speed')
    plt.ylabel('Probability density')
    plt.title('Histogram of IQ:mu=%d,sigma=%d' %(mu,sigma))#中文标题 u'xxx'
    plt.subplots_adjust(left=0.15)#左边距
    save_pic('ztfbnhx')
    plt.show()

def paint_hist():
    xx=x
    plt.hist(xx,bins=8)
    plt.title('tongjizhifangtu')
    save_pic('jzft')
    plt.show()

def paint_speed_fre():
    xx=x
    frequency=[]
    middle=[]
    xx.sort()    #小到大排序
    zs=8  # 组数
    big= max(xx)
    sma= min(xx)
    #print(big,' ',sma)
    inter=int((big-sma)/(zs-1))  # 速度区间间隔
    #print('间隔inter=',inter)
    s=1
    while(1): # 循环传递 8 次参数
        frequency.append(cout(sma+inter*s-inter,sma+inter*s)) #传递组距临界最大值,并将返回的频率添加到 frequency列表里面
    #    print('sma+inter*s-inter,sma+inter*s',sma+inter*s-inter,'  ',sma+inter*s)
        middle.append(mid(sma+inter*s-inter,sma+inter*s)) #得到每组的中间值
        if s==(zs):
            break
        s+=1
    #print(frequency,'纵坐标')
    #print(middle,'横坐标')
    #print(sum(frequency))

    plt.plot(middle,frequency)
    save_pic('csplfbqx')
    plt.show()

def paint_cdf():

    xx = x
    # Compute mean and standard deviation: mu, sigma
    mu=np.mean(xx)   #计算 mu
    sigma=np.std(xx) #计算标准差sigma

    # Sample out of a normal distribution with this mu and sigma: samples
    samples=np.random.normal(mu,sigma,10000)    #以mu sigma 为参数，生成10000个正态分布曲线的y

    # Get the CDF of the samples and of the data
    xxx,y=ecdf(xx) #X是从小到大重新排列的50个数据，Y是生成50个等差数列   0.02 0.04  0.06
    x_theor,y_theor=ecdf(samples)   #x_theor是从小到大重新排列的10000个数据   y_theor是00001  0.0002....


    # Plot the CDFs and show the plot
    _ = plt.plot(x_theor, y_theor)  #画出一万个数据的线图
    _ = plt.plot(xxx, y, marker='.', linestyle='none')    #画出原始数据的散点图
    plt.margins(0.02)
    _ = plt.xlabel('speed')
    _ = plt.ylabel('CDF')

    save_pic('ljpvfbqx')

    plt.show()

def paint_15_85():
    xx=x
    # Get the CDF of the samples and of the data
    xa, ya = ecdf(xx)  # X是从小到大重新排列的50个数据，Y是生成50个等差数列   0.02 0.04  0.06
    yyy = list(ya)
    xxx = list(xa)  # 将tumple([]) 转换成list[]
    external_x = xxx[fig15(yyy)]        #15%最低速度
    external_y = xxx[fig85(yyy)]        #85%最高速度
    # print('15%最低速度=', xxx[fig15(yyy)])
    # print('85%最高速度=', xxx[fig85(yyy)])
    return external_x, external_y

def retn(s):
    fire_abdir = os.getcwd() + '\\'     # 给出当前目录的绝对地址给 image
    file = fire_abdir + s
    return file



def get_entry_input():  # 获得entry 的文本字符串输入并处理其变成数组 x =[1,2,3,4....]
    var = var4.get()
    global x
    x = var.split(',')      # 去掉 var字符串中的','   x=['1','2','3','4'....]
    new = []
    for s in x:
        new.append(int(s))
    x =new

def paint_pic():        # 生成图片
    paint_normal_pdf()  # 生成正态分布拟合
    paint_hist()        # 生成统计直方图
    paint_cdf()         # 生成累计频率分布图
    paint_speed_fre()   # 生成速度频率分布图


# 点击b2确定按钮时对应的操作
# def enter_button():     # 点击enter，要显示画图，计算好15,85%车速
#     get_entry_input()   # 从entry获得输入存入 x[]
#     paint_pic()         # 生成图片
#     png222gif()           # 转化格式


def enter_button():
    s_name=['csplfbqx.gif','jzft.gif','ljpvfbqx.gif','ztfbnhx.gif']     # 固定好的四张图的名字
    fire_abdir = os.getcwd() + '\\'     # 给出当前目录的绝对地址
    get_entry_input()
    for s in s_name:
        if  s in os.listdir(os.getcwd()):
            fire_f = fire_abdir + s
            os.remove(fire_f)
    paint_pic()
    png222gif()

    # 弹窗提示上下速度
    var15,var85 = paint_15_85()
    spd = '15%车速是 ' + str(var15) + ' km/h, '
    spd = spd + '85%车速是 ' + str(var85) + ' km/h'
    tkinter.messagebox.askokcancel('上下限速度显示框', spd)
    # 弹窗提示上下速度

    #显示输入到 t1文本框
    global x
    tx = x
    t1.insert(END,tx)
    # 显示输入到 t1文本框



    global img_gif1,img_gif2,img_gif3,img_gif4
    img_gif4 = PhotoImage(file=retn('ztfbnhx.gif'))
    img_gif1 = PhotoImage(file=retn('jzft.gif'))
    img_gif2 = PhotoImage(file=retn('csplfbqx.gif'))
    img_gif3 = PhotoImage(file=retn('ljpvfbqx.gif'))

    label_img4 = Label(root, image=img_gif4)
    label_img4.pack()
    label_img4.place(x=20, y=529, anchor=NW)

    label_img1 = Label(frm, image=img_gif1)
    label_img1.pack()


    label_img2 = Label(frm, image=img_gif2)
    label_img2.pack()


    label_img3 = Label(frm, image=img_gif3)
    label_img3.pack()


def clear_button():     # 清空按钮,清空输入框e 和车速的 l
    global var4
    var4.set('')        #清空entry输入框
    global img_gif1, img_gif2, img_gif3, img_gif4
    img_gif4 = PhotoImage(file=retn('a2.gif'))
    img_gif1 = PhotoImage(file=retn('a2.gif'))
    img_gif2 = PhotoImage(file=retn('a2.gif'))
    img_gif3 = PhotoImage(file=retn('a2.gif'))

    label_img4 = Label(root, image=img_gif4)
    label_img4.pack()
    label_img4.place(x=20, y=529, anchor=NW)

    label_img1 = Label(frm, image=img_gif1)
    label_img1.pack()

    label_img2 = Label(frm, image=img_gif2)
    label_img2.pack()

    label_img3 = Label(frm, image=img_gif3)
    label_img3.pack()

    t1.delete(0.0,END)
    root.destroy()


# 次级窗口
l1 = Label(root,text='请输入数据，以“，”间隔:',font=('Arial,12')) # 显示对话，请输入数据
l1.pack()
l1.place(x=20, y=60, anchor=NW)

e = Entry(root, show=None,textvariable=var4,borderwidth = 1,foreground = 'blue',font = ('Helvetica', '13', 'bold'))      # entry 文本框获得输入
e.pack()
e.place(in_=l1, relx=1.03)


b1 = Button(root,text = '关闭',command=clear_button,width=10,height=2)   # 清空按钮,清空输入框e 和车速的 l
b1.pack()
b1.place(x=250, y=140, anchor=NW)

b2 = Button(root,text = '确定',command=enter_button,width=10,height=2) # 确定按钮
b2.pack()
b2.place(x=90, y=140, anchor=NW)

l2 = Label(root, text='您输入的数据是：',font=('Helvetica,14'))  # 显示车速提示标签  l2    font=('Arial,14')
l2.pack()
l2.place(x=40, y=230, anchor=NW)

t1 = Text(root,height = 8, width= 48)       # 显示 用户输入的数据
t1.pack()
t1.place(x=40, y=260,anchor =NW )


#
# l3 = Label(root, text=var15)  # 显示15%，l3
# l3.pack()
# l3.place(x=130, y=280, anchor=NW)
#
# l4 = Label(root, text=var85)  # 显示85%， l4
# l4.pack()
# l4.place(x=130, y=320, anchor=NW)



# 定义frame，左侧显示图表
frm = Frame(root)
frm.pack()
frm.place(x=450,y=20)


# 事件循环
root.mainloop()