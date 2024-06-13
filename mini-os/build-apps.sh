#!/bin/bash

CODE_PATH=./initramfs/code/
APPS_PATH=./initramfs/apps/

mkdir -p $APPS_PATH

# 1. A minimal print out "Hello World", the output file is hello
gcc -c $CODE_PATH/minimal.S -o $APPS_PATH/minimal.o
ld $APPS_PATH/minimal.o -o $APPS_PATH/hello
objdump -d $APPS_PATH/minimal.o > $APPS_PATH/minimal.S
objdump -d $APPS_PATH/hello > $APPS_PATH/hello.S

# 2. A static link of C program, the output file is logisim
gcc $CODE_PATH/logisim.c -o $APPS_PATH/logisim -static
objdump -d $APPS_PATH/logisim > $APPS_PATH/logisim.S

# 3. A dynamic link of C program, the output file is logisim_
gcc $CODE_PATH/logisim.c -o $APPS_PATH/logisim_
objdump -d $APPS_PATH/logisim_ > $APPS_PATH/logisim_.S
