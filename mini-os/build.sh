#!/bin/bash

CODE_PATH=./initramfs/code/
APP_PATH=./initramfs/app/

mkdir -p $APP_PATH

# 1. A minimal print out "Hello World", the output file is hello.out
gcc -c $CODE_PATH/minimal.S -o $APP_PATH/minimal.o
ld $APP_PATH/minimal.o -o $APP_PATH/hello.out
objdump -d $APP_PATH/minimal.o > $APP_PATH/minimal.S.out
objdump -d $APP_PATH/hello.out > $APP_PATH/hello.S.out

# 2. A static link of C program, the output file is logisim.out
gcc $CODE_PATH/logisim.c -o $APP_PATH/logisim.out -static
objdump -d $APP_PATH/logisim.out > $APP_PATH/logisim.S.out

# 3. A dynamic link of C program, the output file is logisim_.out
gcc $CODE_PATH/logisim.c -o $APP_PATH/logisim_.out
objdump -d $APP_PATH/logisim_.out > $APP_PATH/logisim_.S.out
