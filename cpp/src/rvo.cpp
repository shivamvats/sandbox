#include <iostream>
#include "rvo.h"

MyClass::MyClass(){
    m_val = 0;
    std::cout<<"Default Constructor called.\n";
}

MyClass::MyClass( int a ){
    m_val = a;
    std::cout<<"Int Constructor called.\n";
}

MyClass::MyClass( const MyClass& obj ){
    m_val = obj.m_val;
    std::cout<<"Copy constructor called.\n";
}
