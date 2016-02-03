# Generated automatically using the command :
# c++2py.py ../c++/fun.hpp -mfunpy -o funpy --moduledoc "This is module funpy doc"
from wrap_generator import *

# The module
module = module_(full_name = "funpy", doc = "This is module funpy doc")

# All the triqs C++/Python modules

# Add here all includes beyond what is automatically included by the triqs modules
module.add_include("../c++/fun.hpp")

# Add here anything to add in the C++ code at the start, e.g. namespace using
module.add_preamble("""
#include <triqs/python_tools/converters/tuple.hpp>
#include <triqs/python_tools/converters/arrays.hpp>
""")
module.add_function ("std::tuple<array<double,1>,array<double,1>> fun (std::string filename, int n)", doc = "This is the doc of my function ...")

module.generate_code()
