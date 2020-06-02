#!/usr/bin/python
#-*-coding:utf-8 -*-

from thinkdsp import *

'''
现在开始研究波形和其对应频谱之间的关系，这里我们从三角波开始，
三角波就像正弦波的直线版本
'''

signal = TriangleSignal(200)
signal.plot()
decorate(xlabel='Time (s)')
plt.show()

'''
period是信号的周期
'''
duration = signal.period*3
print(duration)
segment = signal.make_wave(duration, framerate=10000)
segment.plot()
decorate(xlabel='Time (s)')
plt.show()

# 生成声音
wave = signal.make_wave(duration=0.5, framerate=10000)
wave.write(filename='data/harmonics/output1.wav')