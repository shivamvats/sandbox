cmake_minimum_required( VERSION 2.8.9 )
project( sandbox )
add_compile_options(-std=c++14)

include_directories( include )

add_executable( rvo rvo.cpp src/rvo.cpp )
add_executable( template_executable src/template_recursion.cpp )
