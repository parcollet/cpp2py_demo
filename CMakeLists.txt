# Append triqs installed files to the cmake load path
list(APPEND CMAKE_MODULE_PATH ${TRIQS_PATH}/share/triqs/cmake)

# start configuration 
cmake_minimum_required(VERSION 2.8)
project(funpy CXX)
message(${CMAKE_PROJECT_NAME})
set(CMAKE_BUILD_TYPE Release)
enable_testing()

# We use shared libraries
option(BUILD_SHARED_LIBS "Build shared libraries" ON)

# Load TRIQS, including all predefined variables from TRIQS installation
find_package(TRIQS REQUIRED)

# We want to be installed in the TRIQS tree
set(CMAKE_INSTALL_PREFIX ${TRIQS_PATH})

# Get hash
triqs_get_git_hash(${CMAKE_SOURCE_DIR} "APPLICATION_A")
if(${GIT_RESULT} EQUAL 0)
 message(STATUS "Hash: ${APPLICATION_A_GIT_HASH}")
endif(${GIT_RESULT} EQUAL 0)

include_directories(c++)

# Compile C++ code
#add_subdirectory(c++)

# Python interface
if (${TRIQS_WITH_PYTHON_SUPPORT})
add_subdirectory(python)
endif()

