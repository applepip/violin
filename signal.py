#!/usr/bin/python
#-*-coding:utf-8 -*-

from thinkdsp import *

# 产生正弦信号
'''
freq:频率
amp:振幅
offset:信号周期
'''
sin_sig = SinSignal(freq=880, amp=0.5, offset=0)

sin_sig.plot()
decorate(xlabel='Time (s)')
plt.show()

# 产生余弦信号
cos_sig = CosSignal(freq=440, amp=1.0, offset=0)

cos_sig.plot()
decorate(xlabel='Time (s)')
plt.show()

# 信号叠加求和
mix = sin_sig + cos_sig

mix.plot()
decorate(xlabel='Time (s)')
plt.show()

"""
duration是指wave的长度，单位为秒。
start为开始时间，单位也是秒。

"""
wave = mix.make_wave(duration=0.5, start=0, framerate=11025)
wave.plot()
decorate(xlabel='Time (s)')
plt.show()

# wave.write(filename='data/signal/output.wav')

# wave.ys *=2
# wave.ts +=1
#
# wave.plot()
# decorate(xlabel='Time (s)')
# plt.show()

# wave.write(filename='data/signal/output2.wav')

# spectrum = wave.make_spectrum(full=True)





