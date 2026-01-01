# -*- coding: utf-8 -*-
"""
CSV dosyasından sinyal verisi okuma yardımcı fonksiyonları
"""

import csv
import numpy as np

def load_signal_csv(path):
    """
    CSV formatı:
    t,x
    0.0, 1.23
    0.01, 1.10
    ...

    Parametre:
        path (str): CSV dosya yolu

    Dönen:
        t : zaman vektörü
        x : sinyal vektörü
    """
    t = []
    x = []

    # 1-2. csv modülü ile dosyayı satır satır oku
    with open(path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # başlık satırını atla (t,x)

        # 3. t ve x listelerini doldur
        for row in reader:
            t.append(float(row[0]))
            x.append(float(row[1]))

    # 4. numpy array olarak döndür
    return np.array(t), np.array(x)
