/*
 * Implements BFS search for a custom 2D gridworld.
 *
*/

#include<iostream>
#include<vector>
#include <queue>

using namespace std;

const int size_x = 5, size_y = 5;
const int start_x = 0, start_y = 0;
const int goal_x = 0, goal_y = 4;

void print_map(int map[size_x][size_y]) {
    for(int i=0; i < size_x; i++){
        for(int j=0; j < size_y; j++){
            cout<<map[i][j]<<"  ";
        }
        cout<<"\n";
    }
}


void init_map(int map[size_x][size_y]) {
    for (int i=0; i < size_x; i++)
        if(i != 2)
            map[i][2] = 1;
}


std::vector< std::pair<int, int> >
get_succs(int map[size_x][size_y], int curr_x, int curr_y) {
    std::vector<std::pair<int, int> > succs;
    if(((curr_x + 1) < size_x) && (map[curr_x + 1][curr_y] == 0)) 
        succs.push_back(std::make_pair(curr_x + 1, curr_y));
    if(((curr_x - 1) >= 0) && (map[curr_x - 1][curr_y] == 0))
        succs.push_back(std::make_pair(curr_x - 1, curr_y));
    if (((curr_y + 1) < size_y) && (map[curr_x][curr_y + 1] == 0))
        succs.push_back(std::make_pair(curr_x, curr_y + 1));
    if (((curr_y - 1) >= 0) && (map[curr_x][curr_y - 1] == 0))
        succs.push_back(std::make_pair(curr_x, curr_y - 1));
    return succs;
}

void print_succs(std::vector<std::pair<int, int> >& succs) {
    for(auto& node : succs) {
        cout<< node.first << ", " << node.second <<"\n";
    }
}

void bfs(int map[size_x][size_y], std::pair<int, int> bp[size_x][size_y]) {
    std::queue<std::pair<int, int> > Q;
    bool visited[size_x][size_y] = {};

    bp[start_x][start_y] = make_pair(start_x, start_y);

    Q.push(make_pair(start_x, start_y));
    visited[start_x][start_y] = true;

    while(!Q.empty()) {
        auto node = Q.front();
        cout<< "\nCurrent node: "<< node.first << ", "<< node.second <<"\n";
        Q.pop();
        auto succs = get_succs(map, node.first, node.second);
        cout<<"Succs: \n";
        print_succs(succs);
        for(auto succ : succs) {
            if(!visited[succ.first][succ.second]) {
                Q.push(succ);
                bp[succ.first][succ.second] = node;
                visited[succ.first][succ.second] = true;
            }
        }
    }
}


void print_path(int map[size_x][size_y], std::pair<int, int> bp[size_x][size_y]) {
    int curr_x = goal_x, curr_y = goal_y;
    int new_map[size_x][size_y] = {};
    for (int i=0; i<size_x; i++)
        for(int j=0; j<size_y; j++)
            new_map[i][j] = map[i][j];

    new_map[curr_x][curr_y] = 8;

    while(true) {
        auto parent = bp[curr_x][curr_y];
        curr_x = parent.first, curr_y = parent.second;
        new_map[curr_x][curr_y] = 8;
        if((curr_x == start_x) && (curr_y == start_y))
            break;
    }
    cout<<"Found path:\n";
    print_map(new_map);
}

int main() {
    int map[size_x][size_y] = {0};
    std::pair<int, int> bp[size_x][size_y];
    print_map(map);
    cout<<"\n";
    init_map(map);
    cout<<"\n";
    print_map(map);
    cout<<"\n";

    bfs(map, bp);
    cout<<"Path:\n";
    print_path(map, bp);

    return 0;
}
