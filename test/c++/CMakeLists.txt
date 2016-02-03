include_directories(${TRIQS_INCLUDE_ALL})
link_libraries (triqs toto_a1_c gtest)

triqs_add_all_cpp_tests_in_current_dir()
