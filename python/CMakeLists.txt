# make a local pytriqs copy
triqs_prepare_local_pytriqs(${CMAKE_PROJECT_NAME})

triqs_python_extension(funpy)
target_link_libraries(funpy  ${TRIQS_LIBRARY_ALL})
#target_link_libraries(funpy fun_c ${TRIQS_LIBRARY_ALL})
include_directories(${TRIQS_INCLUDE_ALL} ${CMAKE_CURRENT_SOURCE_DIR})
triqs_set_rpath_for_target(funpy)

# add version file
#configure_file(version.py.in version.py)
#install(FILES ${CMAKE_CURRENT_BINARY_DIR}/version.py DESTINATION ${TRIQS_PYTHON_LIB_DEST_ROOT})

