import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KernelDensity

if __name__ == "__main__":
    """This script plays with the KernelDensity algorithm implemented in
    sklearn.

     Kernel Density Estimation fits a density function  """
    data_train = np.random.rand(100, 2)
    kde = KernelDensity(kernel='gaussian', bandwidth=0.2).fit(data_train)
    data_test = np.random.rand(200, 2) * 2
    log_density = kde.score_samples(data_test)
    density = np.exp(log_density)

    plt.scatter(data_test[:,0], data_test[:,1], c=density)
    plt.show()
