#!/usr/bin/python
#-*-coding:utf-8 -*-

from thinkdsp import *

'''
现在开始研究波形和其对应频谱之间的关系，这里我们从三角波开始，
三角波就像正弦波的直线版本
'''

signal_t = TriangleSignal(200)
signal_t.plot()
decorate(xlabel='Time (s)')
plt.show()

'''
period是信号的周期
'''
duration = signal_t.period*3
segment_t = signal_t.make_wave(duration, framerate=10000)
segment_t.plot()
decorate(xlabel='Time (s)')
plt.show()

# 生成声音
wave_t = signal_t.make_wave(duration=0.5, framerate=10000)
# wave.write(filename='data/harmonics/output_t.wav')

spectrum_t = wave_t.make_spectrum()
spectrum_t.plot()
decorate(xlabel='Frequency (Hz)')
plt.show()

"""
方波
"""

signal_s = SquareSignal(200)
duration = signal_s.period*3
segment_s = signal_s.make_wave(duration, framerate=10000)
segment_s.plot()
decorate(xlabel='Time (s)')
plt.show()

# 生成声音
wave_s = signal_s.make_wave(duration=0.5, framerate=10000)
# wave_s.write(filename='data/harmonics/output_s.wav')

spectrum_s = wave_s.make_spectrum()
spectrum_s.plot()
decorate(xlabel='Frequency (Hz)')
plt.show()