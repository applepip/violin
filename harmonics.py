#!/usr/bin/python
#-*-coding:utf-8 -*-

from thinkdsp import *

signal = TriangleSignal(200)
duration = signal.period*3
segment = signal.make_wave(duration, framerate=10000)
segment.plot()
decorate(xlabel='Time (s)')
plt.show()