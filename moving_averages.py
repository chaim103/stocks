



import numpy as np
def simple_moving_average(data, window):
    weights = np.repeat(1.0, window) / window
    sma = np.convolve(data, weights, 'valid')
    return sma

def exponential_moving_average(data, window):
    weights = np.exp(np.linspace(-1., 0., window))
    weights /= weights.sum()
    ema = np.convolve(data, weights, mode='full')[:len(data)]
    ema[:window] = ema[window]
    return ema


if __name__ == '__main__':
    pass