import numpy as np
import cv2


def visualizeMap( prob_dist ):
    vis_map = np.zeros_like( prob_dist, dtype=str )
    vis_map[ prob_dist == 0 ] = '.'
    vis_map[ prob_dist == 1 ] = 'x'
    print( vis_map )

def main():
    a = np.zeros((10, 10), dtype=int)
    a[4:8, 4:6] = 1
    visualizeMap( a )

if __name__ == "__main__":
    main()
