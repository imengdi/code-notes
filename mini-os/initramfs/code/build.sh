#!/bin/bash

# 1. A minimal print out "Hello World", the output file is a.out
gcc -c minimal.S && ld minimal.o
objdump -d minimal.o > minimal.S.out
objdump -d a.out > a.S.out

# 2. A static link of C program, the output file is b.out
gcc logisim.c -o b.out -static
objdump -d b.out > b.S.out

# 3. A dynamic link of C program, the output file is c.out
gcc logisim.c -o c.out
objdump -d c.out > c.S.out
