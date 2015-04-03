#!/bin/bash

echo "Running Parse Tree generator for trimming output of Parselog."
g++ ptg.cpp
./a.out

echo "Reversing the generated file"
tac output.txt > output1.txt

echo "Converting the generated file to dot format."
g++ dtg.cpp
./a.out > parse_tree.dot

dot -Tps parse_tree.dot -o parsetree.ps
echo "Generating the graph from the dot file into a .ps file"
g++ dtg.cpp
./a.out > parse_tree.dot
# gnome-open parsetree.ps




