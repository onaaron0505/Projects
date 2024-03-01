CXXFLAGS := -std=c++14 -Wall -Werror -ggdb -O0
SRC_DIR = ../
SOURCES := $(wildcard $(SRC_DIR)*.cpp) main.cpp
OBJS := $(SOURCES:%.cpp=%.o)
OBJS := $(filter-out $(SRC_DIR)main.o, $(OBJS))

TARGET := test

.PHONY : all
all : $(TARGET)

$(TARGET) : $(OBJS)
	 $(CXX) $(CXXFLAGS) $^ -o $@ 

.PHONY : run
run :
	./test

.PHONY : clean
clean : 
	rm -rf $(TARGET) $(OBJS)