cmake_minimum_required( VERSION 2.8.9 )
project( sandbox )
add_compile_options(-std=c++14)

find_package(xtensor REQUIRED )
include_directories( include
    ${xtensor_INCLUDE_DIRS})

add_executable( rvo main/rvo.cpp src/rvo.cpp )
add_executable( xtensor_test src/xtensor.cpp )
