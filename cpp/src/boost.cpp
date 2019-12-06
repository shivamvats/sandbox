#include <vector>
#include <utility>
#include <iostream>
#include <boost/geometry.hpp>
#include <boost/geometry/geometries/point.hpp>
#include <boost/geometry/index/rtree.hpp>

namespace bg = boost::geometry;
namespace bgi = boost::geometry::index;

using Point = bg::model::point<double, 2, bg::cs::cartesian>;
using Box = bg::model::box<Point>;
using Value = Point;//std::pair<Point, unsigned int>;
using RTree = bgi::rtree< Value, bgi::rstar<16> >;

int main()
{

    RTree tree;
    tree.insert( Point(0, 0) );
    tree.insert( Point(0, .1) );
    tree.insert( Point(2, .3) );
    tree.insert( Point(1, 2) );
    tree.insert( Point(0.1, 0.5) );
    tree.insert( Point(0.7, 0.8) );

    double radius = 1.5;
    Box box( Point(0.1 - radius, 0.1 - radius), Point(0.1 + radius, 0.1 + radius) );

    std::vector<Point> neighbours;
    tree.query( bg::index::within(box), std::back_inserter(neighbours) );

    std::cerr<< neighbours.size()<< " Points found\n";
    std::cerr<< "Points: \n";
    for( auto& neighbour : neighbours )
    {
        std::cerr<< neighbour.get<0>() << " "<< neighbour.get<1>() << "\n";
    }
}
