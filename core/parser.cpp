// parser.cpp
#include <iostream>
#include <sstream>
#include "parser.h"

// Simple HTML parser (placeholder for a more robust implementation)
std::shared_ptr<DOMNode> parseHTML(const std::string& html) {
    auto rootNode = std::make_shared<DOMNode>();
    rootNode->tag = "html";
    
    // For now, just create a basic structure
    auto bodyNode = std::make_shared<DOMNode>();
    bodyNode->tag = "body";
    
    auto contentNode = std::make_shared<DOMNode>();
    contentNode->tag = "div";
    contentNode->content = html.substr(0, 200) + "... [truncated]";
    
    bodyNode->children.push_back(contentNode);
    rootNode->children.push_back(bodyNode);
    
    return rootNode;
}

// Function to render DOM for display
std::string renderDOM(const std::shared_ptr<DOMNode>& node, int indent) {
    std::stringstream ss;
    std::string indentStr(indent * 2, ' ');
    
    ss << indentStr << "<" << node->tag << ">" << std::endl;
    
    if (!node->content.empty()) {
        ss << indentStr << "  " << node->content << std::endl;
    }
    
    for (const auto& child : node->children) {
        ss << renderDOM(child, indent + 1);
    }
    
    ss << indentStr << "</" << node->tag << ">" << std::endl;
    
    return ss.str();
}