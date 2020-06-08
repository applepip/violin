#!/usr/bin/python
#-*-coding:utf-8 -*-

from thinkdsp import *

"""
变量之间的相关意味着如果知道某一个值，那么便得到一些关于其他值的信息，对相
关性定量，常用的是皮尔森矩阵相关系数
"""
def make_sine(offset):
    signal = SinSignal(freq=440, offset=offset)
    wave = signal.make_wave(duration=0.5, framerate=10000)
    return wave

wave1 = make_sine(offset=0)
wave2 = make_sine(offset=3)

wave1.segment(duration=0.01).plot()
wave2.segment(duration=0.01).plot()
decorate(xlabel='Time (s)')
plt.show()

print(np.corrcoef(wave1.ys, wave2.ys))

print(wave1.corr(wave2))

"""
以上的对角线矩阵代表自身的相关性，非对角线矩阵代表wave1和wave2的相关性
"""


def compute_corr(offset):
    wave1 = make_sine(offset=0)
    wave2 = make_sine(offset=-offset)

    wave1.segment(duration=0.01).plot()
    wave2.segment(duration=0.01).plot()

    corr = wave1.corr(wave2)
    print('corr =', corr)

    decorate(xlabel='Time (s)')

    plt.show()

from ipywidgets import interact, interactive, fixed
import ipywidgets as widgets

PI2 = np.pi * 2
slider = widgets.FloatSlider(min=0, max=PI2, value=1)
interact(compute_corr, offset=slider);

"""
序列相关：各个值与随后值（或者之前值）的相关性
"""

# 计算平移后波形与自身的相关性
def serial_corr(wave, lag=1):
    N = len(wave)
    y1 = wave.ys[lag:]
    y2 = wave.ys[:N-lag]
    corr = np.corrcoef(y1, y2)[0, 1]
    return corr

# UU噪声我们预期不相关
from thinkdsp import UncorrelatedGaussianNoise

signal = UncorrelatedGaussianNoise()
wave = signal.make_wave(duration=0.5, framerate=11025)
print serial_corr(wave)

# 布朗噪声中，各个值是前一个值与一个随机“步长”的和，我们预期会有强相关性
from thinkdsp import BrownianNoise

signal = BrownianNoise()
wave = signal.make_wave(duration=0.5, framerate=11025)
print serial_corr(wave)


# 粉噪声介于布朗噪声和UU噪声间，我们预期他会是中度相关性
from thinkdsp import PinkNoise

signal = PinkNoise(beta=1)
wave = signal.make_wave(duration=0.5, framerate=11025)
print serial_corr(wave)

# 粉噪参数为beta=0，为不相关噪声，逐步变化到beta=2，为布朗噪声，对
# 应序列相关性从0变化到非常接近于1.

np.random.seed(19)

betas = np.linspace(0, 2, 21)
corrs = []

for beta in betas:
    signal = PinkNoise(beta=beta)
    wave = signal.make_wave(duration=1.0, framerate=11025)
    corr = serial_corr(wave)
    corrs.append(corr)

plt.plot(betas, corrs)
decorate(xlabel=r'Pink noise parameter, $\beta$',
         ylabel='Serial correlation')

plt.show()


# 不同参数粉噪的自相关方式，beta=1.7时，即使针对很长的时滞，序列
# 的相关性也很高该现象称为长相关性。即信号中各个值依赖于前面很多值

def autocorr(wave):
    """Computes and plots the autocorrelation function.

    wave: Wave

    returns: tuple of sequences (lags, corrs)
    """
    lags = np.arange(len(wave.ys) // 2)
    corrs = [serial_corr(wave, lag) for lag in lags]
    return lags, corrs

def plot_pink_autocorr(beta, label):
    signal = PinkNoise(beta=beta)
    wave = signal.make_wave(duration=1.0, framerate=10000)
    lags, corrs = autocorr(wave)
    plt.plot(lags, corrs, label=label)


np.random.seed(19)

for beta in [1.7, 1.0, 0.3]:
    label = r'$\beta$ = %.1f' % beta
    plot_pink_autocorr(beta, label)

decorate(xlabel='Lag',
         ylabel='Correlation')
plt.show()

from thinkdsp import read_wave

wave = read_wave('data/autocorrelation/28042__bcjordan__voicedownbew.wav')

spectrum = wave.make_spectrum()
spectrum.plot()
decorate(xlabel='Frequency (Hz)', ylabel='Amplitude')
plt.show()

spectro = wave.make_spectrogram(seg_length=1024)
spectro.plot(high=4200)
decorate(xlabel='Time (s)',
                 ylabel='Frequency (Hz)')

plt.show()