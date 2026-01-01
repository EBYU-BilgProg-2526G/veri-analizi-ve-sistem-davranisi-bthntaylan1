# -*- coding: utf-8 -*-
"""
Basit sinyal işleme fonksiyonları
"""

def moving_average(x, window_size):
    y = []

    for i in range(len(x)):
        start = i - window_size + 1
        if start < 0:
            start = 0

        window = x[start:i+1]
        avg = sum(window) / len(window)
        y.append(avg)

    return y
