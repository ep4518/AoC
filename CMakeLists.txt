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
    add_executable(AoC2 2024/Day02/day2.cpp)
    add_executable(AoC3 2024/Day03/day3.cpp)
    add_executable(AoC4 2024/Day04/day4.cpp)

    # Include Boost headers (header-only library)
    target_include_directories(AoC2 PRIVATE ${Boost_INCLUDE_DIRS})
else()
    message(FATAL_ERROR "Boost libraries not found!")
endif()
