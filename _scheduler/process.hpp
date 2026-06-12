struct Process{
    int pid;
    int arrival_time;
    int burst_time;
    int priority;
    // The fields below will be set by simulator
    int remaining_time;
    int start_time;
    int finish_time;
    enum state{ready, running, waiting, terminated};
    Process(int id, int arr_time,int bt ,int prio = 0){
        this->pid = id;
        this->arrival_time = arr_time;
        this->burst_time = bt;
        this->priority = prio;
        remaining_time = burst_time;
        start_time = finish_time = -1;
    }
};