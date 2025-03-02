#ifndef ENGINE_H
#define ENGINE_H

#include <string>

class Engine {
public:
    void start();
    std::string fetchPage(const std::string& url);
};

#endif
