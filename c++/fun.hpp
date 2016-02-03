#pragma once
#include <triqs/arrays.hpp>
#include <iostream>
#include <tuple>

using triqs::arrays::array;

/// This is the doc of my function ... 
std::tuple<array<double,1>, array<double,1>> 
fun (std::string const &filename, int n) { 

 array<double,1> a = {1,2,3,4,5};
 array<double,1> b = 2*a;
 
 if (n<0) TRIQS_RUNTIME_ERROR << "Idiot !";
 return std::make_tuple(a,b);
}

