#!/usr/bin/python
#-*- coding:utf-8 -*-

from thinkdsp import *

"""
假定给予一系列振幅，和一系列频率，要求构建一个信号，
此信号是这些频率元素的和
"""

def synthesize1(amps, fs, ts):
    """
    :param amps: 振幅列
    :param fs: 频率列
    :param ts: 对信号求值的时间序列
    :return:
    """
    components = [CosSignal(freq, amp)
                  for amp, freq in zip(amps, fs)]
    signal = SumSignal(*components)

    # evaluate计算出每个ts时间的信号值
    ys = signal.evaluate(ts)
    return ys

# 合成应用测试
"""
这个例子构建的信号包含一个位于100hz的基频和3个谐波频率，
然后以11025帧每秒的帧率生成1s的信号，再把这些结果放在
wave对象中
"""
amps = np.array([0.6, 0.25, 0.1, 0.05])
fs = [100, 200, 300, 400]
framerate = 11025

ts = np.linspace(0, 1, framerate, endpoint=False)

ys = synthesize1(amps, fs, ts)
wave = Wave(ys, ts, framerate)

wave.plot()
decorate(xlabel='Time (s)')
plt.show()

# 数组合成
def synthesize2(amps, fs, ts):
    # np.outer计算ts和fs的外积，将结果存放在数组中，
    # 数组中每一行对应ts的一个元素，每一列对应fs的一个
    # 元素，数组的各元素是一个频域值和一个时间的乘积ft。
    args = np.outer(ts, fs)
    # 各列包含在一系列的时间点取值的，拥有自己特定频率的y
    # 余弦信号
    M = np.cos(PI2 * args)
    # 计算频率元素的加权和
    ys = np.dot(M, amps)
    return ys

ys = synthesize2(amps, fs, ts)
wave = Wave(ys, framerate)

ys1 = synthesize1(amps, fs, ts)
ys2 = synthesize2(amps, fs, ts)
print np.max(np.abs(ys1 - ys2))

"""
假设已知一个波形，且它由一系列给定频率的余弦信号相加而成
，求各个元素的振幅，根据上面组合数组，可用np.linalg.solve
求解线性系统，但这样做时间很长。
"""

def analyze1(ys, fs, ts):
    args = np.outer(ts, fs)
    M = np.cos(PI2 * args)
    amps = np.linalg.solve(M, ys)
    return amps
n = len(fs)
amps2 = analyze1(ys[:n], fs, ts[:n])
print amps2
