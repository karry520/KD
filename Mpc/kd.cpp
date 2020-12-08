#include <pybind11/pybind11.h>
#include <pybind11/stl_bind.h>
#include <pybind11/stl.h>

#include <vector>

#include "kd_aby.h"


namespace py = pybind11;
using namespace std;

typedef uint8_t uInt;
typedef int8_t Int;
typedef uint32_t uInt32;

PYBIND11_MAKE_OPAQUE(std::vector<Int>);
PYBIND11_MAKE_OPAQUE(std::vector<uInt>);
PYBIND11_MAKE_OPAQUE(std::vector<uInt32>);

PYBIND11_MODULE(KD, m) {

    py::bind_vector<std::vector<Int>>(m, "VectorInt", py::buffer_protocol());
    py::bind_vector<std::vector<uInt>>(m, "VectoruInt", py::buffer_protocol());
    py::bind_vector<std::vector<uInt32>>(m, "VectoruInt32", py::buffer_protocol());

    m.doc() = "C++ module for KD";

    m.def("init_aby", &init_aby, "init_aby");
    m.def("init1_aby", &init1_aby, "init1_aby");
    m.def("shutdown_aby", &shutdown_aby, "shutdown_aby");
    m.def("kd_sru", &kd_sru, "kd_sru");
    m.def("kd_top", &kd_top, "kd_top");

}
