import numpy as np
import sklearn as skl
from sklearn.gaussian_process import GaussianProcessRegressor
import matplotlib.pyplot as plt
import seaborn as sns


mode = 'sklearn'

def gaussian_kernel(x1, x2):
    return np.exp(-(x1 - x2)**2)


if __name__ == "__main__":
    if mode == 'custom':
        N = 10
        xs = np.linspace(0, 10, N)

        mu = np.zeros(N)
        sigma = np.zeros((xs.size, xs.size))
        for i in range(sigma.shape[0]):
            sigma[i] = gaussian_kernel(xs[i], xs)
        print(sigma)
        for i in range(2):
            f = np.random.multivariate_normal(mu, sigma)
            plt.plot(xs, f)
        plt.show()
    elif mode == 'sklearn':
        xs = np.linspace(0, 10, 5).reshape(-1, 1)
        ys = xs**2
        gpr = GaussianProcessRegressor().fit(xs, ys)
        print(gpr.get_params())

        xs_test = np.linspace(0.15, 10, 100).reshape(-1, 1)
        y = xs_test**2
        y_pred = gpr.predict(xs_test)
        plt.plot(xs_test, y_pred, 'r', label='Prediction')
        plt.plot(xs_test, y, 'b', label='Ground Truth')
        plt.legend()
        plt.show()
