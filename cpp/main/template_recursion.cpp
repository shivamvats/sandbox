#include <iostream>
#include "template_recursion.h"

int main(){
    std::cout<<"Testing Template Recursion\n";
    std::cout<<"===========================\n";
    std::cout<<"This code demonstrates how you can use templated"
    " functions that take in multiple templates to write\n"
    "recursive code. Is this faster? Found in Andrei's talk at\n"
    "https://www.youtube.com/watch?v=ea5DiCg8HOY, time: 18:17.\n";
    std::cout<<"\n";

    std::cout<<"\nTesting Parameter Packs to define add function with variable number of arguments\n";
    std::cout<<"add(1, 2): "<<add(1, 2)<< "\n";
    std::cout<<"add(1, 2, 3): "<<add(1, 2, 3)<< "\n";
    std::cout<<"The same function was called with different number of arguments\n";
}
