#!/bin/bash

echo "🛠️ Cleaning old build..."
rm -rf build
mkdir build && cd build

echo "⚙️ Running CMake..."
cmake ..

echo "🚀 Compiling..."
make -j$(nproc)

echo "✅ Build complete!"