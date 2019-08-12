#include <meta/gridworld.h>

int main(){
    GridWorld<FourConnectivity> grid( 10, 10, 0.2 );
    auto point = std::make_pair( 5, 5 );
    auto succs = grid.Succs(point);
    for(auto& pt: succs){
        std::cout<<pt.first<<"\t"<<pt.second<<"\n";
    }
}
