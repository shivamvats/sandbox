"""
Goal:
    We are given a small dataset of 2D points with 0(-ve)/1(+ve) labels.
    It is known that the data has been sampled from a rectangle of known
    dimensions.
    Also, the +ve data points are surrounded by -ve data points
    We are to learn a decision boundary that separated the two.

Approach:
    1. We approximate the decision boundary using a convex polytope.
       A 1-hidden layered nn with relu activation essentially learn a linear
       combination of half-spaces -> a polytope.

       We will evaluate the performance of this approach on synthetic data.
"""

import numpy as np
import random
from sklearn.neural_network import MLPClassifier
import matplotlib.pyplot as plt

def sampleRandomPointsFromRect(n, x_lims, y_lims):
    points = [ [random.uniform( x_lims[0], x_lims[1] ), random.uniform(
            y_lims[0], y_lims[1] )] for i in range(n) ]
    return points

def plotDecisionBoundary( points, preds ):
    points = np.array(points)
    points_0 = np.array([ point for point, label in zip(points, preds) if label
                        == 0 ])
    points_1 = np.array([ point for point, label in zip(points, preds) if label
                        == 1 ])
    plt.scatter( points_0[:, 0], points_0[:, 1], marker='o', color='b' )
    plt.scatter( points_1[:, 0], points_1[:, 1], marker='o', color='r' )
    plt.show()


if __name__ == "__main__":
    # All data is sampled from this rectangle
    x_lims = [0, 10]
    y_lims = [0, 10]

    X = [[4,4], [5,5], [6,6], [4,7], [7,4], [0,0],
            [10,10],[10,0],[0,10],[2,9],[2,2],[9,9]]
    y = [1, 1, 1, 1, 1, 0, 0, 0,0,0,0,0]
    clf = MLPClassifier(solver='lbfgs', alpha=1e-5, activation='relu',
                        hidden_layer_sizes=(5,), random_state=1)
    clf.fit( X, y )
    test_samples = sampleRandomPointsFromRect(500, x_lims, y_lims)
    preds = clf.predict( test_samples )
    plotDecisionBoundary( test_samples, preds )
