#include <pybind11/pybind11.h>
#include "networking/fetcher.h"
#include "core/parser.h"

namespace py = pybind11;

std::string fetch_page(const std::string& url) {
    return fetchURL(url);
}

std::string parse_page(const std::string& html) {
    return parseHTML(html);
}

// Expose functions to Python
PYBIND11_MODULE(nebula_engine, m) {
    m.def("fetch_page", &fetch_page, "Fetch a webpage");
    m.def("parse_page", &parse_page, "Parse HTML");
}
