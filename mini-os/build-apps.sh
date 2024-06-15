#!/bin/bash

CODE_PATH=./initramfs/code/
APPS_PATH=./initramfs/apps/

CC_TOOL=aarch64-linux-gnu-gcc
LD_TOOL=aarch64-linux-gnu-ld
DP_TOOL=aarch64-linux-gnu-objdump

mkdir -p $APPS_PATH

# 1. A minimal print out "Hello World", the output file is hello
# $CC_TOOL -c $CODE_PATH/minimal.S -o $APPS_PATH/minimal.o
# $LD_TOOL $APPS_PATH/minimal.o -o $APPS_PATH/hello
# $DP_TOOL -d $APPS_PATH/minimal.o > $APPS_PATH/minimal.S
# $DP_TOOL -d $APPS_PATH/hello > $APPS_PATH/hello.S

# 2. A static link of C program, the output file is logisim
$CC_TOOL $CODE_PATH/logisim.c -o $APPS_PATH/logisim -static
$DP_TOOL -d $APPS_PATH/logisim > $APPS_PATH/logisim.S

# 3. A dynamic link of C program, the output file is logisim_
$CC_TOOL $CODE_PATH/logisim.c -o $APPS_PATH/logisim_
$DP_TOOL -d $APPS_PATH/logisim_ > $APPS_PATH/logisim_.S
