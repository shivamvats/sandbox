#include <iostream>
#include <variant>

int main(){
    std::variant<int, std::string> t;
    t = "Hello";
    try{
        auto o = std::get<int>( t );
        std::cout<<o<<"\n";
    } catch ( const std::bad_variant_access& ){}
    try{
        auto o = std::get<std::string>( t );
        std::cout<<o<<"\n";
    } catch ( const std::bad_variant_access& ){}
}
