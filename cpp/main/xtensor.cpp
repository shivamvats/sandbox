#include <iostream>
#include "xtensor/xarray.hpp"
#include "xtensor/xio.hpp"
#include "xtensor/xview.hpp"

int main(int argc, char** argv)
{
    xt::xarray<double> arr1
    {{1.0, 2.0, 3.0},
     {2.0, 5.0, 7.0},
     {2.0, 5.0, 7.0}};

    xt::xarray<double> arr2
    {5.0, 6.0, 7.0};

    auto res = xt::view(arr1, 0) * arr2;
    std::cout<<"Output:\n";
    std::cout<<res;
    std::cout<<typeid(res.shape()).name()<< "\n";
    std::cout<<"Shape: "<< res.shape()<< "\n";
    return 0;
}
