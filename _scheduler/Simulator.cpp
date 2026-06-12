#include "Simulator.hpp"

void Simulator :: submit(int pid, int arr , int bt, int prio = 0){
    Jobs.emplace_back(Process(pid, arr, bt,prio)); // memory trick i observed
}

void Simulator :: run_algorithm(){
    if(algo == "fcfs"){

    }
    else if(algo == "rr"){

    }
    else{
        std :: cerr << "Algo not available. \n";
    }
}