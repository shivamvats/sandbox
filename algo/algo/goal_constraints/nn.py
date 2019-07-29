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

def plotPoints( points, clr ):
    points = np.array(points)
    plt.scatter( points[:, 0], points[:, 1], marker='o', color=clr )
    plt.show()

def plotDecisionBoundary( points, preds ):
    points = np.array(points)
    points_0 = np.array([ point for point, label in zip(points, preds) if label
                        == 0 ])
    points_1 = np.array([ point for point, label in zip(points, preds) if label
                        == 1 ])
    plt.scatter( points_0[:, 0], points_0[:, 1], marker='o', color='r' )
    plt.scatter( points_1[:, 0], points_1[:, 1], marker='o', color='b' )
    plt.show()


if __name__ == "__main__":
    # All data is sampled from this rectangle
    x_lims = [0, 10]
    y_lims = [0, 10]

    x_lims_positive = [3, 8]
    y_lims_positive = [3, 8]

    #X = [[4,4], [5,5], [6,6], [4,7], [7,4], [0,0],
    #[10,10],[10,0],[0,10],[2,9],[2,2],[9,9]]

    n_positive = 100
    X_positive = np.array(sampleRandomPointsFromRect( n_positive, x_lims_positive,
            y_lims_positive ))
    y_positive = np.ones(n_positive)


    n_negative = 100
    X_negative = np.array(sampleRandomPointsFromRect( 10*n_negative, x_lims,
            y_lims ))
    reject_positive = lambda x: ((x[0] < x_lims_positive[0] or x[0] >
            x_lims_positive[1]) and (x[1] < y_lims_positive[0] or x[1] >
            y_lims_positive[1]))
    X_negative = list(filter( reject_positive, X_negative ))[:n_negative]
    y_negative = np.zeros(n_negative)

    X = np.concatenate(( X_positive, X_negative ))
    y = np.concatenate((y_positive, y_negative ))

    clf = MLPClassifier(solver='lbfgs', alpha=1e-5, activation='relu',
                        hidden_layer_sizes=(100,), random_state=1)
    clf.fit( X, y )
    test_samples = sampleRandomPointsFromRect(500, x_lims, y_lims)
    preds = clf.predict( test_samples )
    plotDecisionBoundary( test_samples, preds )
