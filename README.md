# Compiler-Final
Intermediate code generation

1. We have made the lexer first in my "Compiler-lexer" repository. Refer that in case of any dought in lexer. 

2.

3. Here, we wrote a Intermediate Code Generator(in Ass3 folder) for the source langauge JAVA. The output for it is a linked list of Three Address Code(3AC). So, we designed the 3AC code, attached semantic rules to the grammar designed in "Compiler-parser" repository to genertae a three-address code for JAVA langauge as a linked-list of three-address statements and print the 3-address code on the standard output.

4. Here, we then wrote an Assembly Code Generator from the above INtermediate Code Generator. The output of this is assembly code in MIPS. Here , we have implemented a register allocator,implement the translator to translate staements in three-address code to assembly instruction, set up the data regions to handle global data and constants, and provided some of the library support for useful programs. 

