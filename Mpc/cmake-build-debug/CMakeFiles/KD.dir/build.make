# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.17

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Disable VCS-based implicit rules.
% : %,v


# Disable VCS-based implicit rules.
% : RCS/%


# Disable VCS-based implicit rules.
% : RCS/%,v


# Disable VCS-based implicit rules.
% : SCCS/s.%


# Disable VCS-based implicit rules.
% : s.%


.SUFFIXES: .hpux_make_needs_suffix_list


# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /snap/clion/135/bin/cmake/linux/bin/cmake

# The command to remove a file.
RM = /snap/clion/135/bin/cmake/linux/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/karrylee/PycharmProjects/KD/Mpc

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/karrylee/PycharmProjects/KD/Mpc/cmake-build-debug

# Include any dependencies generated for this target.
include CMakeFiles/KD.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/KD.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/KD.dir/flags.make

CMakeFiles/KD.dir/kd.cpp.o: CMakeFiles/KD.dir/flags.make
CMakeFiles/KD.dir/kd.cpp.o: ../kd.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/karrylee/PycharmProjects/KD/Mpc/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/KD.dir/kd.cpp.o"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/KD.dir/kd.cpp.o -c /home/karrylee/PycharmProjects/KD/Mpc/kd.cpp

CMakeFiles/KD.dir/kd.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/KD.dir/kd.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/karrylee/PycharmProjects/KD/Mpc/kd.cpp > CMakeFiles/KD.dir/kd.cpp.i

CMakeFiles/KD.dir/kd.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/KD.dir/kd.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/karrylee/PycharmProjects/KD/Mpc/kd.cpp -o CMakeFiles/KD.dir/kd.cpp.s

CMakeFiles/KD.dir/kd_aby.cpp.o: CMakeFiles/KD.dir/flags.make
CMakeFiles/KD.dir/kd_aby.cpp.o: ../kd_aby.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/karrylee/PycharmProjects/KD/Mpc/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object CMakeFiles/KD.dir/kd_aby.cpp.o"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/KD.dir/kd_aby.cpp.o -c /home/karrylee/PycharmProjects/KD/Mpc/kd_aby.cpp

CMakeFiles/KD.dir/kd_aby.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/KD.dir/kd_aby.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/karrylee/PycharmProjects/KD/Mpc/kd_aby.cpp > CMakeFiles/KD.dir/kd_aby.cpp.i

CMakeFiles/KD.dir/kd_aby.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/KD.dir/kd_aby.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/karrylee/PycharmProjects/KD/Mpc/kd_aby.cpp -o CMakeFiles/KD.dir/kd_aby.cpp.s

# Object files for target KD
KD_OBJECTS = \
"CMakeFiles/KD.dir/kd.cpp.o" \
"CMakeFiles/KD.dir/kd_aby.cpp.o"

# External object files for target KD
KD_EXTERNAL_OBJECTS =

lib/KD.cpython-38-x86_64-linux-gnu.so: CMakeFiles/KD.dir/kd.cpp.o
lib/KD.cpython-38-x86_64-linux-gnu.so: CMakeFiles/KD.dir/kd_aby.cpp.o
lib/KD.cpython-38-x86_64-linux-gnu.so: CMakeFiles/KD.dir/build.make
lib/KD.cpython-38-x86_64-linux-gnu.so: lib/libaby.a
lib/KD.cpython-38-x86_64-linux-gnu.so: lib/libotextension.a
lib/KD.cpython-38-x86_64-linux-gnu.so: lib/libencrypto_utils.a
lib/KD.cpython-38-x86_64-linux-gnu.so: /usr/local/lib/libboost_system.so.1.74.0
lib/KD.cpython-38-x86_64-linux-gnu.so: /usr/local/lib/libboost_thread.so.1.74.0
lib/KD.cpython-38-x86_64-linux-gnu.so: /usr/local/lib/libgmp.so
lib/KD.cpython-38-x86_64-linux-gnu.so: /usr/local/lib/libgmpxx.so
lib/KD.cpython-38-x86_64-linux-gnu.so: /usr/lib/x86_64-linux-gnu/libcrypto.so
lib/KD.cpython-38-x86_64-linux-gnu.so: lib/librelic_s.a
lib/KD.cpython-38-x86_64-linux-gnu.so: /usr/local/lib/libgmp.so
lib/KD.cpython-38-x86_64-linux-gnu.so: CMakeFiles/KD.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/karrylee/PycharmProjects/KD/Mpc/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Linking CXX shared module lib/KD.cpython-38-x86_64-linux-gnu.so"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/KD.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/KD.dir/build: lib/KD.cpython-38-x86_64-linux-gnu.so

.PHONY : CMakeFiles/KD.dir/build

CMakeFiles/KD.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/KD.dir/cmake_clean.cmake
.PHONY : CMakeFiles/KD.dir/clean

CMakeFiles/KD.dir/depend:
	cd /home/karrylee/PycharmProjects/KD/Mpc/cmake-build-debug && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/karrylee/PycharmProjects/KD/Mpc /home/karrylee/PycharmProjects/KD/Mpc /home/karrylee/PycharmProjects/KD/Mpc/cmake-build-debug /home/karrylee/PycharmProjects/KD/Mpc/cmake-build-debug /home/karrylee/PycharmProjects/KD/Mpc/cmake-build-debug/CMakeFiles/KD.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/KD.dir/depend

