#include <memory>

#include <meta/bfs.h>
#include <meta/gridworld.h>

using namespace Planning;
using Environment = GridWorld<FourConnectivity>;

int main(){
    auto grid_ptr = std::make_shared<Environment>( 10, 10, 0.2 );
    Bfs<Environment> bfs(grid_ptr);
    Point start = std::make_pair(0, 0);
    Point goal = std::make_pair(5, 5);
    auto success = bfs.plan( start, goal );
    bfs.printVistedNodes();
}
