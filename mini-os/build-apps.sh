#!/bin/bash

CODE_PATH=./initramfs/code/
APPS_PATH=./initramfs/apps/

mkdir -p $APPS_PATH

# 1. A minimal print out "Hello World", the output file is hello.out
gcc -c $CODE_PATH/minimal.S -o $APPS_PATH/minimal.o
ld $APPS_PATH/minimal.o -o $APPS_PATH/hello.out
objdump -d $APPS_PATH/minimal.o > $APPS_PATH/minimal.S.out
objdump -d $APPS_PATH/hello.out > $APPS_PATH/hello.S.out

# 2. A static link of C program, the output file is logisim.out
gcc $CODE_PATH/logisim.c -o $APPS_PATH/logisim.out -static
objdump -d $APPS_PATH/logisim.out > $APPS_PATH/logisim.S.out

# 3. A dynamic link of C program, the output file is logisim_.out
gcc $CODE_PATH/logisim.c -o $APPS_PATH/logisim_.out
objdump -d $APPS_PATH/logisim_.out > $APPS_PATH/logisim_.S.out
