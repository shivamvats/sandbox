#include <iostream>
#include <functional>
#include <unordered_map>

inline int sum( int a, int b ){
    return a + b;
}

inline int diff( int a, int b ){
    return a - b;
}

using OperationType = std::function<int( int, int )>;

int main(){
    std::unordered_map<std::string, OperationType> map;
    map["sum"] = sum;
    map["diff"] = diff;
    std::string input;
    std::cin>>input;
    int result;

    if( input == "sum" )
        result = map[input]( 3, 4 );
    else
        result = map[input]( 3, 4 );
    std::cout<<result<<"\n";
}
