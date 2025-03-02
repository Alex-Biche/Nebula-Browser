// Create engine/scripting/lua_engine.h
#ifndef LUA_ENGINE_H
#define LUA_ENGINE_H

#include <string>
#include <lua.hpp>

class LuaEngine {
public:
    LuaEngine();
    ~LuaEngine();
    
    bool runScript(const std::string& script);
    bool setDOMAccess(/* DOM structure reference */);
    
private:
    lua_State* L;
};

#endif