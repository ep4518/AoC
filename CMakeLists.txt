cmake_minimum_required(VERSION 3.28)
project(AoC)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Boost settings
set(Boost_USE_STATIC_LIBS OFF)
set(Boost_USE_MULTITHREADED ON)
set(Boost_USE_STATIC_RUNTIME OFF)

# Find Boost
find_package(Boost REQUIRED)

if(Boost_FOUND)
    # Add the executable
    add_executable(AoC 2024/Day02/day2.cpp)

    # Include Boost headers (header-only library)
    target_include_directories(AoC PRIVATE ${Boost_INCLUDE_DIRS})
else()
    message(FATAL_ERROR "Boost libraries not found!")
endif()
