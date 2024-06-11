#!/bin/bash

gcc -c minimal.S && ld minimal.o
gcc logisim.c -o logisim.out -static
