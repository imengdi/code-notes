.PHONY: clean

all: libjson11 run_app.cc
	@$(CXX) -O -std=c++11 run_app.cc json11.o -o a.out

test: libjson11 run_test.cc
	@$(CXX) -O -std=c++11 run_test.cc json11.o -o a.out

libjson11: json11.cc json11.h
	@$(CXX) -c -std=c++11 json11.cc -fno-rtti -fno-exceptions

clean:
	@rm -rf *.o *.out
