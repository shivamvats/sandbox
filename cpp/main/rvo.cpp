#include <iostream>

#include "rvo.h"

MyClass foo( int a ){
    MyClass obj;
    obj.m_val = a;
    return obj;
}

int main(){
    MyClass obj1(5);

    std::cout<<"Testing RVO\n";
    MyClass obj2 = foo(10);
    std::cout<<"Test over.\n";
    std::cout<<"The copy constructor is called when a class object\n"
        "is returned by value. The copy constructor is called again when the\n"
        "returned object is copied to another variable (in the calling function).\n"
        "However, Return Value Optimization ensures that the copy constructor is\n"
        "not called and the object's memory location is directly passed to the new variable.\n";
}
