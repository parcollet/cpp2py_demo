set(cpp_sources fun.cpp)
add_library(fun_c ${cpp_sources})
target_link_libraries(fun_c ${TRIQS_LIBRARY_ALL})
include_directories(${TRIQS_INCLUDE_ALL})
triqs_set_rpath_for_target(fun_c)

install(TARGETS fun_c  DESTINATION lib)
