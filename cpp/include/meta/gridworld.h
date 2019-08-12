#ifndef GRIDWORLD_H
#define GRIDWORLD_H

#include <iostream>
#include <vector>
#include <string>
#include <memory>
#include <array>

class FourConnectivity {
    public:
    static std::array<std::pair<int, int>, 4> neighbours(std::pair<int, int> point){
        std::array<std::pair<int, int>, 4> nbrs;
        nbrs[0] = std::make_pair(point.first - 1, point.second);
        nbrs[1] = std::make_pair(point.first + 1, point.second);
        nbrs[2] = std::make_pair(point.first, point.second - 1);
        nbrs[3] = std::make_pair(point.first, point.second + 1);

        return nbrs;
    }

};

class EightConnectivity {
    public:
    static std::array<std::pair<int, int>, 8> neighbours(
            std::pair<int, int> point){
        std::array<std::pair<int, int>, 8> nbrs;
        nbrs[0] = std::make_pair(point.first - 1, point.second);
        nbrs[1] = std::make_pair(point.first + 1, point.second);
        nbrs[2] = std::make_pair(point.first, point.second - 1);
        nbrs[3] = std::make_pair(point.first, point.second + 1);
        nbrs[4] = std::make_pair(point.first - 1, point.second - 1);
        nbrs[5] = std::make_pair(point.first + 1, point.second + 1);
        nbrs[6] = std::make_pair(point.first + 1, point.second - 1);
        nbrs[7] = std::make_pair(point.first - 1, point.second + 1);

        return nbrs;
    }

};

template <typename ConnectivityPolicy>
class GridWorld : public ConnectivityPolicy {
    public:
    GridWorld( int size_x, int size_y, double res );
    ~GridWorld();

    auto neighbours(std::pair<int, int> point)
        -> decltype(ConnectivityPolicy::neighbours(point));
    std::vector<std::pair<int, int>> Succs(std::pair<int, int> point);
    bool isValid(std::pair<int, int> point){
        return true;
    }

    public:
    int m_size_x;
    int m_size_y;
    double m_res;
    int m_cols;
    int m_rows;

    int** m_grid;

};

template <typename T>
GridWorld<T>::GridWorld( int size_x, int size_y, double res ) :
        m_size_x{size_x}, m_size_y{size_y}, m_res{res} {
    m_cols = m_size_x/m_res + 0.5;
    m_rows = m_size_y/m_res + 0.5;
    m_grid = new int*[m_cols];
    for( int i=0; i<m_cols; i++ )
        m_grid[i] = new int[m_rows];
}

template <typename T>
GridWorld<T>::~GridWorld(){
    for( int i=0; i<m_cols; i++ )
        delete m_grid[i];
    delete m_grid;
}

template <typename CP>
auto GridWorld<CP>::neighbours(std::pair<int, int> point)
        -> decltype(CP::neighbours(point)){
    return CP::neighbours(point);
}

template <typename T>
std::vector<std::pair<int, int>> GridWorld<T>::Succs(
        std::pair<int, int> point){
    std::vector<std::pair<int, int>> Succs;
    for(auto& nbr: neighbours(point)){
        if(isValid(nbr))
            Succs.push_back(nbr);
    }
    return Succs;
}

#endif
