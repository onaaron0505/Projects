CXXFLAGS := -std=c++14 -Wall -Werror -ggdb -O0

SOURCES := $(wildcard *.cpp)
OBJS := $(SOURCES:%.cpp=%.o)


TARGET := pokerSim

.PHONY : all
all : $(TARGET)

$(TARGET) : $(OBJS)
	 $(CXX) $(CXXFLAGS) $^ -o $@ 

.PHONY : run
run :
	./pokerSim

.PHONY : clean
clean : 
	rm -rf $(TARGET) $(OBJS)