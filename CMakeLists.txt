cmake_minimum_required(VERSION 3.10)
project(NebulaBrowser)

set(CMAKE_CXX_STANDARD 17)

# Find necessary packages
find_package(Python3 REQUIRED COMPONENTS Interpreter Development)
find_package(pybind11 REQUIRED CONFIG)
find_package(CURL REQUIRED)

# Add the source files for the C++ engine
add_library(nebula_engine MODULE 
    engine/engine.cpp 
    engine/networking/fetcher.cpp 
    engine/core/parser.cpp 
)

# Add to CMakeLists.txt
find_package(Lua REQUIRED)
target_link_libraries(nebula_engine PRIVATE ${LUA_LIBRARIES})
target_include_directories(nebula_engine PRIVATE ${LUA_INCLUDE_DIR})

# Set target properties to remove the 'lib' prefix
set_target_properties(nebula_engine PROPERTIES PREFIX "")

# Link libraries
target_link_libraries(nebula_engine PRIVATE pybind11::pybind11 CURL::libcurl)
