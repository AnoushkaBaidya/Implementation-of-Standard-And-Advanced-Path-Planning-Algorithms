from queue import Queue, PriorityQueue
from collections import deque
from typing import Dict, Tuple
from PIL import Image
import random
import math 
import sys

""" Motion Path Planning algorithms -> BFS, DFS, Dijkstra and Random Sampler Planning Algorithms """


#This is will have all the planning algorithms -> BFS, DFS, Dijkstra and Random Sampler Planning Algorithm 


# List of all nodes that can be traveresed by a current_node -> left, right, up and down which is not an obstacle and inside the grid
def traversable_nodes(image:Image , curr_node: Tuple): 
    #taking the x and y cordinate of the current node 
    x_cord,y_cord= curr_node[0], curr_node[1]
    #Creating an Empty list to append traversable neighbours of current node
    trav_neighbours=[]
    
    #List of all neighbours irrespective of obstacle -> up,doown,left and right
    all_neighbours= [(x_cord,y_cord+1), (x_cord,y_cord-1), (x_cord+1,y_cord), (x_cord-1,y_cord)]

    for nb in all_neighbours:
        #check to see if it is not outside the grid 
        if not(0 <= nb[0] <= 127 and 0 <= nb[1] <= 127):
            continue
        else: 
            #if it is also not an obstacle then append in the list
            if(image.getpixel(nb) != (0,0,0)):
                trav_neighbours.append(nb)

    return trav_neighbours


#Creating an Adjacency list Represenattion for our unweighted graph
def adjacency_list(image:Image) -> Dict:
    #Empty adjacency dict for all the nodes in our graph 
    adj={}
    for i in range(128):
        for j in range(128):
            cur_node= (i,j)
            adj[i,j]= traversable_nodes(image,cur_node)

    return adj 

def children_not_visited(node: Tuple, grid:Dict , visited):
    # to get the unvisited children of a particular node
    #create an empty list 
    unv_child=[]
    for child in grid.get(node,[]):
        if child not in visited:
            unv_child.append(child)

    return unv_child

#Adjacency list of our grid with dist as cost for every node 
def adjacency_list_weighted_graph(image:Image) -> Dict:
    #Empty adjacency dict for all the nodes in our graph 
    adj={}
    for i in range(128):
        for j in range(128):
            cur_node= (i,j)
            adj[i,j]= traversable_nodes_with_weights(image,cur_node)

    return adj 

def  traversable_nodes_with_weights(image:Image , curr_node: Tuple) -> Dict:
    x_cord,y_cord= curr_node[0], curr_node[1]
    #Creating an Empty list to append traversable neighbours of current node
    trav_neighbours={}
    
    #List of all neighbours irrespective of obstacle -> up,doown,left and right
    all_neighbours= [(x_cord,y_cord+1), (x_cord,y_cord-1), (x_cord+1,y_cord), (x_cord-1,y_cord),(x_cord+1,y_cord+1), (x_cord-1,y_cord-1), (x_cord+1,y_cord-1), (x_cord-1,y_cord+1)]
    #all_neighbours= [(x_cord,y_cord+1), (x_cord,y_cord-1), (x_cord+1,y_cord), (x_cord-1,y_cord)]

    for nb in all_neighbours:
        #check to see if it is not outside the grid 
        if not(0 <= nb[0] <= 127 and 0 <= nb[1] <= 127):
            continue
        else: 
            if(image.getpixel(nb) != (0,0,0)):
                trav_neighbours[nb] = math.dist(curr_node,nb)

    return trav_neighbours



'''  Path Planning -> Motion Planning ALgorithms '''

""" BREADTH FIRST SEARCH ALGORITHM IMPLEMENATATION """
def bfs(grid: Dict, start: Tuple, goal: Tuple):
    """
    Performs a breadth-first search traversal from start to goal node in a graph.
    :param start: starting node
    :param goal: goal node
    :param graph: dictionary of nodes and their adjacent nodes
    """
    #Creating a queue data structure to store all the nodes 
    queue_track = deque()
    #Adding start node to queue to 
    queue_track.append(start)
    
    path_traversed = [] #initialised to keep track of the all the nodes we traverese 
    final_path = []  # Initialised to keep track of final path 

    #creating dict and set to keep track of already visted node and parents of each node  
    visited=set()
    #Keeping track of parent node 
    prev_node = {key: None for key in grid.keys()}

    #set start node as visited 
    visited.add(start)

    # Initialised a variable to check if path found or not 
    found=False

    while len(queue_track):
        curr_node= queue_track.popleft()
        path_traversed.append(curr_node)

        for adj_child in grid[curr_node]:
            if adj_child not in visited:
            
                if adj_child == goal: 
                    #if goal reached then break out of the loop
                    found=True
                    visited.add(adj_child)
                    prev_node[adj_child]=curr_node
                    break

                visited.add(adj_child)
                prev_node[adj_child]=curr_node

                queue_track.append(adj_child)
    if found:
        print("Path found from start to goal ")
        node = goal
        while node!= start:
            next_node= prev_node[node]
            final_path.append(next_node)
            node = next_node 

        final_path.pop()

        steps_taken = len(path_traversed)
        print("BFS Implementation Done!")
        
    else: 
        print(" Path not found from start to goal. Regenarating Grid ")
        steps_taken = len(visited)

    return found, final_path, steps_taken
        



def dfs(grid: Dict, start: Tuple, goal: Tuple):
    """
    Performs a depth-first search traversal from start to goal node in a graph.
    :param start: starting node
    :param goal: goal node
    :param graph: dictionary of nodes and their adjacent nodes
    """
    #creating a queue to keep track of the nodes 
    queue_track = deque()
    #Initialising a list to keep track of the final path from start to goal 
    final_path = []
    path_traversed = []

    #creating dict and set to keep track of visited nodes and parent nodes
    visited=set()
    prev_node = {key: None for key in grid.keys()}

    #starting from the start node and adding start to the visited  and track 
    current_node = start
    visited.add(current_node)
    queue_track.append(current_node)
    path_traversed.append(current_node)

    #Initialised To check if path found or not 
    found=False

    while len(queue_track):
        children = children_not_visited(current_node, grid, visited)
        if not children:
            current_node = queue_track.pop()

        for child in children:
            if child not in visited:

                if child == goal:  
                    #if we reached then we should terminate the traversal
                    found = True
                    visited.add(child)
                    prev_node[child] = current_node
                    path_traversed.append(child)
                    #clear the queue
                    queue_track.clear()
                    break

                visited.add(child)
                prev_node[child] = current_node
                path_traversed.append(current_node)
                queue_track.append(current_node)
                current_node = child
                break

    if found:
        print("Path found from start to goal ")
        #if path is found, regenerate the steps it took to find the path 
        current = goal
        while current != start:
            next = prev_node[current]
            final_path.append(next)
            current = next

        final_path.pop()
        steps_taken=len(visited)
        print("DFS Implementation Done!")
    else:
         print("Path not found from start to goal. Regenarating Grid ")

    return found, steps_taken, final_path


""" MOVES TO RANDOM PLACES -> NEIGHBOURING CELL """
def random_planner(graph: Dict, start: Tuple, goal: Tuple):
    
    """
    Performs a random search traversal from start to goal node in a graph.
    :param start: starting node
    :param goal: goal node
    :param graph: dictionary of nodes and their adjacent nodes
    """
    #Initialising a list to keep track of all nodes it is traversing
    path_traversed = []
    # Initialising visited set to keep track of the visited nodes
    visited = set()
    #Keeping track of parent node 
    prev_node = {key: None for key in graph.keys()}

    #Keeping track of current node 
    curr_node = start
    #add current start node to visited node
    visited.add(curr_node)
    path_traversed.append(curr_node)
    #Initialisng a max iteratin variable to make sure if it stuck in infinite loop it can break out after those iterations
    max_iterations= 1000
    #Keep count of current iterations
    num_iters=0

    while curr_node != goal:
        #if the total num of iterations or execution is more than set limit break out of the loop
        if num_iters> max_iterations :
            break

        #get the unvisited children list
        child_nodes = children_not_visited(curr_node,graph,visited)
        if not child_nodes:
            #no where to go and stuck -> take a step back 
            curr_node= prev_node[curr_node]
            continue

        # choosing any random neighbour 
        next_node = random.choice(graph[curr_node])
        if next_node in visited:
            continue

        #if we reach goal somehow
        if next_node == goal:
            visited.add(next_node)
            path_traversed.append(next_node)
            prev_node[next_node]= curr_node
            break
        
        visited.add(next_node)
        prev_node[next_node]=curr_node
        path_traversed.append(next_node)
        curr_node=next_node

    print("Random Planner Implementation Done!")

    return path_traversed

""" DIJKSTRA ALGORITHM IMPLEMENTATION """
def dijkstra(graph: Dict[Tuple, Dict[Tuple, int]], start: Tuple, goal: Tuple):
   
    """
    Performs a dijkstra search traversal from start to goal node in a graph.
    :param start: starting node
    :param goal: goal node
    :param graph: dictionary of nodes and their adjacent nodes dict with distance cost
    """
    #Creating a queue data structure to store all the nodes 
    #Initialised to keep track of the all the nodes we traverese 
    queue_track = PriorityQueue()
    #Initially setting all distances of node to infinity 
    dist_cost = {key: sys.maxsize for key in graph.keys()}
    #Keeping track of parent node 
    parent = {key: None for key in graph.keys()}  
    steps_taken =0

    #Adding start node to queue and also putting distance to zero 
    #Here We are calculatig and updating distance of all nodes wrt to the start node 
    dist_cost[start] = 0
    queue_track.put((0, start))

    while not queue_track.empty():
        #Pop the node and assigning it as a current node 
        current_node = queue_track.get()[1]
        steps_taken +=1
        #If the goal is reached we need t trace our path back to calculate the final path and break out of the loop 
        if current_node == goal:
            final_path = []
            while current_node != start:
                final_path.append(current_node)
                current_node = parent[current_node]
            final_path.append(start)
            final_path = final_path[::-1]
            break
        
        #if not goal node then check for all neighbours and calc distance 
        children = graph[current_node]
        for child in children.keys():

            new_dist = (
                dist_cost[current_node] + graph[current_node][child]
            )
            #If the new distance is less than the previous one then we need to update the dist and also the parent node
            if new_dist < dist_cost[child]:  
                dist_cost[child] = new_dist
                parent[child] = current_node
                queue_track.put((new_dist,child))
                

    print("Dijkstra Implementation Done!")
    print("Distance of end goal from start is: : "+" {vt}".format(vt= dist_cost[goal]))

    return final_path, steps_taken



   

        








    