import matplotlib.pyplot as plt
import numpy as np

def plot_chart():
    
    # Данные для графика
    m = np.linspace(0.1, 2 * np.pi, 41)
    n = np.exp(np.sin(m))
    
    plt.stem(m, n)
    plt.show()
