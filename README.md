# Implementation of Standard And Advanced Path Planning Algorithms 

## Environment Setup
Two-dimensional 128X128 grid size has the following properties: 
1. Point robot that occupies one cell/node at a time and the robot moves a single node/cell  in a single step
2. Multiple randomly placed obstacles of varying coverage density 
<img width="727" alt="Screenshot 2023-02-23 at 12 23 06 PM" src="https://user-images.githubusercontent.com/115124698/220983481-9bc321cb-44e0-42b1-8125-cc3945bf398b.png">


## Implementation of Forward Search Planning Algorithms 
Once the environment is configured with desirable density, a robot is spawned at the northwest position of the grid which utilizes the Forward Search Planning Algorithms to make its way to the southeast corner to the goal Location. [Start- Red Color Goal- Green Color]

### A] Breadth-First Search Algorithm 
Breadth-First Search (BFS) is a popular graph traversal algorithm that starts at a source node and explores all its neighbors before visiting the neighbors of neighbors. The algorithm uses a queue data structure to keep track of the nodes to be visited next, ensuring that the search is performed in a breadth-wise manner. BFS is used to solve problems such as finding the shortest path between two nodes, checking the connectivity of a graph, and finding the level of each node in a tree. The time complexity of BFS is O(V + E), where V is the number of nodes and E is the number of edges in the graph, making it suitable for small to medium-sized graphs. 
<img width="727" alt="Screenshot 2023-02-23 at 12 19 36 PM" src="https://user-images.githubusercontent.com/115124698/220983500-7db46855-6679-4798-9ae3-36ece9b0d222.png">

### B] Depth First Search Algorithm 
Depth-First Search (DFS) is a graph traversal algorithm that starts at a source node and explores as far as possible along each branch before backtracking. Unlike BFS, DFS explores the nodes in a depth-wise manner, going as deep as possible before backtracking to explore other nodes. The algorithm uses a stack data structure to keep track of the nodes to be visited next. DFS is used for tasks such as finding a path between two nodes, topological sorting and checking the connectivity of a graph. The time complexity of DFS is O(V + E), where V is the number of nodes and E is the number of edges in the graph. DFS is more suitable for large graphs with a few strongly connected components, as it can be faster than BFS in this case.
<img width="727" alt="Screenshot 2023-02-23 at 12 19 45 PM" src="https://user-images.githubusercontent.com/115124698/220983513-c077bdc7-6d4e-4132-9c39-34b513b64066.png">


### C] Dijkstra Algorithm
Dijkstra's Algorithm is a popular graph search algorithm that finds the shortest path from a source node to all other nodes in a weighted graph. It works by maintaining a priority queue of nodes, where the priority of each node is determined by the shortest distance from the source node. At each iteration, the algorithm selects the node with the lowest priority and updates the distances of its neighbors. The algorithm continues until all nodes have been processed or the goal node has been reached. Dijkstra's Algorithm guarantees to find the shortest path in a graph if all edge weights are non-negative.
<img width="727" alt="Screenshot 2023-02-23 at 12 21 01 PM" src="https://user-images.githubusercontent.com/115124698/220983533-fa8905c3-9ac9-4d57-a300-2be428720e6b.png">

### D] Random Planner 
The Robot Moves randomly at cell location at each step. 
<img width="727" alt="Screenshot 2023-02-23 at 12 21 21 PM" src="https://user-images.githubusercontent.com/115124698/220983552-01d1ad75-b50e-4c4a-b622-7c45fd63115f.png">

## How to install dependencies/libraries
1. Create a new virtual environment in the working directory
2. Clone the git repo in the directory
3. Activate virtual env
4. Use ```pip install -r requirements.txt``` to install all dependencies

## How to run code
1. Activate the virtual environment
2. Enter the directory containing the script
3. Run ```python <filename>.py``` to run code
