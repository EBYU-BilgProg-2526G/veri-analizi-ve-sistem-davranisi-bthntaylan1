# -*- coding: utf-8 -*-
"""
Grafik çizim fonksiyonları
"""

import matplotlib.pyplot as plt

def plot_time(t, x_raw, x_filt, save_path):
    """
    Ham ve filtrelenmiş sinyali zaman domeninde çizer
    """
    plt.plot(t, x_raw)
    plt.plot(t, x_filt)

    plt.xlabel("Time")
    plt.ylabel("Signal")
    plt.title("Signal Plot")

    plt.savefig(save_path)
    plt.close()






