#include <iostream>
#include <vector>
#include "process.hpp"

class Simulator{

    std :: vector<Process>Jobs;
    std :: vector<Process> finished;
    std :: string algo;
    int quantum;

    public:
    Simulator(std :: string algo, int quantum = 0) : algo(algo), quantum(quantum){}

    void submit(int pid, int arrival_time, int burst_time, int priority = 0);

    void run_algorithm();
};