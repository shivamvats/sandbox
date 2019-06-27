#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

const int size = 3;
int graph[size][size] = {0};

int parent[size] = {0};
// 0: unseen
// 1: visited
// 2: all successors visited
int color[size] = {0};

vector<int> succs(int i){
    vector<int> succs;
    for(int j=0;j<size;j++){
        if(j == i)
            continue;
        if(graph[i][j]){
            succs.push_back(j);
        }
    }
    return succs;
}

template<typename T>
void printVec(T& vec){
    for(auto& a: vec)
        cout<<a<<"\t";
    cout<<"\n";
}

void dfs(int start){
    cout<<start<<"\n";
    color[start] = 1;
    auto s = succs(start);

    for(int a: s){
        if(color[a] == 0)
            dfs(a);
    }
    color[start] = 2;
}

void initialize(){
    for(int i=0;i<size;i++){
        parent[i] = -1;
        for(int j=0;j<size;j++)
            graph[i][j] = 1;
    }

}
int main() {
    initialize();
    dfs(0);
}
