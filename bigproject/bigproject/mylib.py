import numpy as np
import matplotlib.pyplot as plt

def sinusoides(n_periods: int, n_points=10_000) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    x = np.linspace(0, n_periods*2*np.pi, n_points)
    y_cos = np.cos(x)
    y_sin = np.sin(x)
    return x, y_cos, y_sin 

def show_sinusoides(x, y_cos, y_sin):
    plt.plot(x, y_cos, x, y_sin)
    plt.show()

if __name__ == '__main__':
    x, y1, y2 = sinusoides(3)
    show_sinusoides(x, y1, y2)