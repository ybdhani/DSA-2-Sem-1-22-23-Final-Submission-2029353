# DSA-2-Sem-1-22-23-Final-Submission-2029353

Normal Greedy:

This code is an implementation of a breadth-first search algorithm that finds the shortest path between two nodes in a graph. The implementation is done in Python.
Input

The input to the find_shortest_path function consists of:

    A dictionary graph representing the graph, where the keys are nodes and the values are lists of the node's neighbors.
    The start node start.
    The end node end.

Output

The output of the function is either:

    The shortest path between the start and end nodes in the form of a list of nodes, or
    None if no path exists.

Usage

An example of how to use the code is provided in the code itself:

Explanation

The algorithm uses a breadth-first search approach to find the shortest path. It keeps track of nodes that have been visited using a set visited, and uses a queue to store paths to explore. The algorithm works by starting at the start node and exploring all its neighbors. It adds the neighbors to the queue and marks the start node as visited. The process continues until the end node is found or there are no more paths to explore.


Iterated Greedy:

This code implements an iterated greedy algorithm for solving a machine job scheduling problem. The algorithm starts with a randomly generated solution and repeats the process of partially destructing the solution and reconstructing it until a stopping criterion is met. The code includes functions for initializing the solution, destructing the solution partially, reconstructing the machine selection, and reconstructing the sequence and machine selection.
Getting Started

The code requires Python 3.x to run. To use the code, follow these steps:

    Clone the repository to your local machine.
    Open a terminal and navigate to the directory where the code is located.
    Run the following command:

    python iterated_greedy.py

Configuration

The code can be configured by changing the following variables in the main function:

    num_jobs: the number of jobs to be scheduled
    num_machines: the number of machines available for scheduling
    stopping_criterion: the maximum number of iterations the algorithm should run

Output

The code prints the initial solution and the final solution to the terminal. The solution is represented as a list of integers, where each integer represents the assigned machine for a job.
Conclusion

This code provides a basic implementation of an iterated greedy algorithm for solving a machine job scheduling problem. The code can be used as a starting point for further development and optimization.
