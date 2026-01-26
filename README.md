# ProcessManager
This Project aims to implement the Operating System Scheduler (as of now), in order to better grapsp 
the operating system fundamentals and the FastAPI python based backend development in order to learn
the websockets and general API.
The Project currently supports two schedulers a.) Round Robin (preemptive), b.)FCFS (non preemptive)
Both of them are Non priority based algorithms 
Preemptive Algorithms : In this kind of scheduling , the OS saves the PCB of running process to OS allocated memory, at some intermediate stage when it's the time to swap this process out to some other process ,this saving is called Context Switch.When the process is brought back, it resumes from the point it left.These could suffer from starvation in many cases(not in Round Robin).
Non Preemptive Algorithms : If a process starts , then it cannot be put to wait/suspended state.It has to complete,before some other process is scheduled.These could suffer from Convoy effect(it means that if some large process comes before , the process at the end will have to wait for long DEFINITE time).

Try this project :
i. Install the requirements and dependencies 
ii. Inside the root directory in your terminal : uvicorn api.main:app --reload (the reload would make your backend restart automatically once the system changes, backend will be available at 8000).
iii. Go to the frontend and just : npm start (available at port 3000 of the localhost)
There you have it.