// parser.h
#ifndef PARSER_H
#define PARSER_H

#include <string>
#include <vector>
#include <memory>

// Basic DOM node structure
struct DOMNode {
    std::string tag;
    std::string content;
    std::vector<std::shared_ptr<DOMNode>> children;
};

// Function declarations
std::shared_ptr<DOMNode> parseHTML(const std::string& html);
std::string renderDOM(const std::shared_ptr<DOMNode>& node, int indent = 0);

#endif