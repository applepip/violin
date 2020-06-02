#!/usr/bin/python
#-*-coding:utf-8 -*-

"""
chirp是一种可变频率信号，他能创建三角波信号，其频率线性的扫过某个频率段
"""

from thinkdsp import *

signal = Chirp(start=220, end=880)
wave = signal.make_wave(duration=2)

wave.segment(start=0, duration=0.01).plot()
decorate(xlabel='Time (s)')
plt.show()

wave.segment(start=0.9, duration=0.01).plot()
decorate(xlabel='Time (s)')
plt.show()


"""
如果想要感知音高线性增加，频率就需要指数型增加
"""
signal = ExpoChirp(start=220, end=880)
wave2 = signal.make_wave(duration=2)

wave2.segment(start=0, duration=0.01).plot()
decorate(xlabel='Time (s)')
plt.show()

wave2.segment(start=0.9, duration=0.01).plot()
decorate(xlabel='Time (s)')
plt.show()

"""
chirp的频谱,该频谱在220Hz到440Hz之间大体上是平整的，
这意味着这个信号在该区间内的各个频率上的时间是相等
的。我们不能在该频谱中得出该信号的频谱是增加还是下降。
"""
signal = Chirp(start=220, end=440)
wave = signal.make_wave(duration=1)
spectrum = wave.make_spectrum()
spectrum.plot(high=700)
decorate(xlabel='Frequency (Hz)')
plt.show()

"""
我们将chrip分解成小的部分，然后绘制出各部分的频谱。其
结果称为STFT。STFT可视化方式很多，通用是频谱图，它的x
轴为时间，轴为频率。
"""
def plot_spectrogram(wave, seg_length):
    """
    """
    spectrogram = wave.make_spectrogram(seg_length)
    print('Time resolution (s)', spectrogram.time_res)
    print('Frequency resolution (Hz)', spectrogram.freq_res)
    spectrogram.plot(high=700)
    decorate(xlabel='Time(s)', ylabel='Frequency (Hz)')

# x轴显示的时间为0~1s，y轴显示的频率为0~700Hz
signal = Chirp(start=220, end=440)
wave = signal.make_wave(duration=1, framerate=11025)
plot_spectrogram(wave, 512)
plt.show()