cmake_minimum_required( VERSION 2.8.9 )
project( sandbox )
add_compile_options(-std=c++11)

include_directories( include )

add_executable( rvo rvo.cpp src/rvo.cpp )
