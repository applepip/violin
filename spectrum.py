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

# 产生余弦信号
cos_sig = CosSignal(freq=440, amp=1.0, offset=0)

# 信号叠加求和
mix = sin_sig + cos_sig

# wave表示信号在一系列时间点下求出的值，每个时间点成为'帧'
wave = mix.make_wave(duration=0.5, start=0, framerate=11025)

'''
频谱是相加产生信号的正弦波的集合，其中频率最低的被称为基频。
基频具有最高的幅度就是主频，感知到声音的音高是由其基频决定的，
即使他不是主频。
'''
spectrum = wave.make_spectrum()

spectrum.plot()
decorate(xlabel='Frequency (Hz)')
plt.show()