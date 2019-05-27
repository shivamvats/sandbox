import numpy as np
import cv2

class ValueIteration:
    def __init__( self, start_, goal_ ):
        assert( start_.dtype == int and goal_.dtype == int )
        self.start = start_
        self.goal = goal_
        self.n_rows, self.n_cols = 10, 10
        self.occ_grid = np.zeros( ( self.n_rows, self.n_cols ), dtype=int )
        self._addRandomObs( 0 )
        self._initVizMap()

        self.actions = [ (1, 0), (-1, 0), (0, 1), (0, -1) ]


    def _addRandomObs( self, seed_ ):
        if seed_ == 0:
            self.occ_grid[ 3:8, 4:6 ] = 1
        else:
            raise NotImplementedError

    def _initVizMap( self ):
        self.viz_map = np.zeros_like( self.occ_grid, dtype=str )
        self.viz_map[ self.occ_grid == 0 ] = '.'
        self.viz_map[ self.occ_grid == 1 ] = 'x'
        self.viz_map[ self.start[0], self.start[1] ] = 's'
        self.viz_map[ self.goal[0], self.goal[1] ] = 'g'

    def reward( self, s_ ):
        assert( s_.dtype == int )
        if np.all( s_ == self.goal ):
            return 1
        else:
            return 0

    def nextState( self, state_, action_id_ ):
        row, col = state_
        action = self.actions[ action_id_ ]
        new_row = min( row + action[0], self.n_rows )
        new_col = min( col + action[1], self.n_cols )
        return np.array( [new_row, new_col], dtype=int )

    def visualizeMap( self ):
        print( self.viz_map )

    """The viz_maps before and after the function call should be identical."""
    def visualizeState( self, s_ ):
        assert( s_[0] < self.n_rows and s_[1] < self.n_cols )
        cache = self.viz_map[ s_[0], s_[1] ]
        self.viz_map[ s_[0], s_[1] ] = 'o'
        print( self.viz_map )
        self.viz_map[ s_[0], s_[1] ] = cache


def main():
    val_iter = ValueIteration( np.array( [0, 0], dtype=int ), np.array( [ 5,
            9], dtype=int ) )
    val_iter.visualizeMap()

    # Test reward function
    state = np.array( (5,9), dtype=int )
    reward = val_iter.reward( state )
    print(reward)

    state = np.array( (2,7), dtype=int )
    val_iter.visualizeState( state )

    # Test nextState
    #nextState = val_iter.nextState( state, )

if __name__ == "__main__":
    main()
