"""
scipy.optimize.leastsq() 使用最小二乘法拟合
"""

import numpy as np
from scipy.optimize import leastsq
import matplotlib.pyplot as plt

# 定义拟合函数形式
# (p,x)为函数的输入形参
def func(p, x):
    k, b = p
    return k*np.sin(x*np.pi)+b

#定义误差函数
def error(p, x, y):
    return func(p, x)-y

# 最小二乘拟合函数，制图
def TestLeastsq(p, Xi, Yi):
    # 使用leastsq()函数进行参数估计,最小二乘法，leastsq()函数返回拟合曲线的信息
    para = leastsq(error, p, args=(Xi, Yi))
    # 系数与常数项求解,para[0]=p，拟合曲线的参数
    k, b = para[0]
    # 结果输出
    print('k=', k, '\n', 'b=', b)
    # 图形可视化
    plt.figure(figsize=(8, 6))
    # 训练训练数据的散点图
    plt.scatter(Xi, Yi, color='b', label='Sample Point', linewidths=2)
    # X坐标
    plt.xlabel('x')
    # y坐标
    plt.ylabel('y')
    x = np.linspace(0, 5, 200)     #np.linspace创建等差数列
    # 函数
    y = k*np.sin(x*np.pi)+b
    #制图
    plt.plot(x, y, color='orange', label='Fitting Line', linewidth=2)
    #图例
    plt.legend()
    #展示图表
    plt.show()

#-------------测试数据-------------
Xi = np.array([0.0833, 0.1666, 0.2500, 0.3333, 0.5, 2.0833, 2.1666, 2.2500, 2.3333, 2.5000])
Yi = np.array([2.5176, 3.0000, 3.4142, 3.7320, 4.0000, 2.5176, 3.0000, 3.4142, 3.7320, 4.0000])
# 随机给出参数的初始值
p = [2, 2]
#函数调用
TestLeastsq(p, Xi, Yi)