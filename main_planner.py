"""   MAIN PLANNING FILE -> IMPLEMENT MP ALGORITHMS"""
from PIL import Image
import matplotlib.pyplot as plt
from planning_alg import adjacency_list, adjacency_list_weighted_graph, bfs, dfs, random_planner, dijkstra
from obstacle_environment import tetrominoes_in_image
import numpy as np 
import pickle

""" Associating different colours for different Algorithm Plot """
blue = (51, 255, 255) #BFS Algorithm
red = (204, 0, 102) #Start Position 
green = (34, 139, 34) #Goal Position
yellow = (255,255,0) #Dijkstra Algorithm
orange = (255,140,0)  #Random Planner 
light_coral = (240,128,128) #DFS Algorithm

#Initialising Fixed start and Goal Locations
start=(0,0)
goal=(127,127)


""" IMPLEMNETING THE PLANNING ALGORITHMS ONE BY ONE WITH VARYING COVERAGE AND DUMPING THE DATA USING A PICKLE FILE """
def motion_planning_combined(coverage):
    # Creating obstacle grid with varying coverage -> varying Obstacle Density 
    grid = tetrominoes_in_image(coverage)

    #Graph representation of our Image Grid
    graph = adjacency_list(grid)
    graph_weight = adjacency_list_weighted_graph(grid)


    #Placing start and goal locations on the grid
    grid.putpixel(start, red)
    grid.putpixel(goal, green)
    plt.imshow(grid)
 
    #Steps Taken -> Steps or iterations taken to find the goal
    path_found_bfs, path_bfs ,steps_taken = bfs(graph, start, goal)
    path_found_dfs,steps_taken,path_dfs = dfs(graph, start, goal)
    path_rand = random_planner(graph,start,goal)
    path_dij, steps_taken = dijkstra(graph_weight,start,goal)

    #Final path from start to goal 
    for node in path_bfs:
        grid.putpixel(node, blue)

    #Final path from start to goal 
    for node in path_dfs:
       
        grid.putpixel(node, light_coral)

    #Final path from start to goal 
    for node in path_rand:
       
        grid.putpixel(node, orange)

    #Final path from start to goal 
    for node in path_dij:
       
        grid.putpixel(node, yellow)

    plt.imshow(grid)
    plt.show()
    return True

def bfs_planning_alg(coverage: int):

    # Creating obstacle grid with varying Coverage 
    grid = tetrominoes_in_image(coverage)
    #Graph representation of our Image Grid
    graph = adjacency_list(grid)

    #Placing start and goal locations on the grid 
    grid.putpixel(start, red)
    grid.putpixel(goal, green)
    plt.imshow(grid)

    #Steps Taken -> Steps or iterations taken to find the goal 
    path_found, path ,steps_taken = bfs(graph, start, goal)

    # If no path found regenerate the Obstacle Grid 
    counter= 0
    while path_found != True :
              
            grid = tetrominoes_in_image(coverage)
            graph = adjacency_list(grid)
            #Can choose different start and goal locations if path not found
            path_found, path,steps_taken= bfs(graph, start, goal)
            counter+=1
            print("Trying to find a path for Attempt number : :"+"{vt}".format(vt= counter))
            if counter>14:
                break

    #Final path from start to goal 
    for node in path:
        grid.putpixel(node, blue)

    plt.imshow(grid)
    plt.title('Breadth First Search Algorithm')
    plt.show()
    
    path_len=len(path)
    print("Path length : :"+"{path}".format(path= path_len))
    print("Steps Taken to find goal : :"+"{steps}".format(steps= steps_taken))

    return steps_taken, path_len

def dfs_planning_alg(coverage: int):
    # Create obstacle grid with desired size and coverage
    grid = tetrominoes_in_image(coverage)

    # Get graph representation from image
    graph = adjacency_list(grid)

    # Place start and goal on the grid
    grid.putpixel(start, red)
    grid.putpixel(goal, green)
    plt.imshow(grid)

    path_found,steps_taken,path = dfs(graph, start, goal)
    # If no path found regenerate the obstacle and map 
    counter= 0
    while path_found != True :
              
            grid = tetrominoes_in_image(coverage)
            graph = adjacency_list(grid)
            #can choose different start and goal locations if path not found
            path_found,steps_taken, path = dfs(graph, start, goal)
            counter+=1
            print("Trying to find a path Attempt number : :"+"{vt}".format(vt= counter))
            if counter>14:
                break

    # Final path of the traversal 
    for points in path:
        if points == start:
            continue
        if points == goal:
            continue

        grid.putpixel(points, light_coral)

    plt.imshow(grid)
    plt.title('Depth First Search Algorithm ')
    plt.show()
    path_len=len(path)

    print("Path length : :"+"{path}".format(path= path_len))
    print("Steps Taken to find goal : :"+"{steps}".format(steps= steps_taken))

    return steps_taken, path_len

def random_alg(coverage):

    # Create obstacle grid with desired size and coverage
    grid = tetrominoes_in_image(coverage)

    # Get graph representation from image
    graph = adjacency_list(grid)

    #place strat and goal locations
    grid.putpixel(start, red)
    grid.putpixel(goal, green)
    plt.imshow(grid)
    

    path = random_planner(graph,start,goal)

    #Generate the path on the grid 
    for points in path:
        if points == start:
            continue
        if points == goal:
            continue
        grid.putpixel(points,orange)
    

    plt.imshow(grid)
    plt.title('Random Planner Implementation ')
    plt.show()

    #length of the path from start to goal -> This is equal to steps_taken 
    print("Iterations taken:", len(path))
    
    return len(path)

def dijkstra_alg(coverage):
    #Create obstacle grid with desired size and coverage
    grid = tetrominoes_in_image(coverage)

    #Get graph representation from image
    graph = adjacency_list_weighted_graph(grid)

    #Place start and goal on the grid
    start=(0,0)
    goal=(126,126)
    grid.putpixel(start, red)
    grid.putpixel(goal, green)
    plt.imshow(grid)

    path ,steps_taken  = dijkstra(graph, start, goal)

    #Construct the final Path for the the grid
    for points in path:
        if points == start:
            continue
        if points == goal:
            continue
        grid.putpixel(points, yellow)

    plt.imshow(grid)
    plt.title('Dijkstra Algorithm ')
    plt.show()

    path_len = len(path)

    print("Path length : :"+"{path}".format(path= path_len))
    print("Steps Taken to find goal : :"+"{steps}".format(steps= steps_taken))
    return steps_taken, path_len




if __name__ == "__main__":

    for coverage in range(5,15,5):
        print("path generated for coverage : :"+"{vt}".format(vt= coverage))
        motion_planning_combined(coverage)


    #Declaring list to store the values later to be plotted 
    bfs_steps=[]
    dfs_steps=[]
    rand_steps=[]
    dij_steps=[]
    
    #To append the coverage data 
    coverage_data=[]

    bfs_path=[]
    dfs_path=[]
    rand_path=[]
    dij_path=[]

   
    for coverage in range(5,80,5):
        print("path generated for coverage : :"+"{vt}".format(vt= coverage))
        steps_bfs,path_len_bfs = bfs_planning_alg(coverage)
        bfs_steps.append(steps_bfs)
        bfs_path.append(path_len_bfs)

        steps_dfs,path_len_dfs = dfs_planning_alg(coverage)
        dfs_steps.append(steps_dfs)
        dfs_path.append(path_len_dfs)

        steps_rand = random_alg(coverage)
        rand_steps.append(steps_rand)
        rand_path.append(steps_rand)

        steps_dij,path_len_dij = dijkstra_alg(coverage)
        dij_steps.append(steps_dij)
        dij_path.append(path_len_dij)

        coverage_data.append(coverage)



    #Save the values to be plotted in a graph for Visualization
    with open('datafile_bfs.txt','wb') as fh0:
        pickle.dump(bfs_steps,fh0)

    with open('datafile_cov.txt','wb') as fh1:
        pickle.dump(coverage_data,fh1)

    with open('datafile_dfs.txt','wb') as fh2:
        pickle.dump(dfs_steps,fh2)

    with open('datafile_rand.txt','wb') as fh3:
        pickle.dump(rand_steps,fh3)

    with open('datafile_dij.txt','wb') as fh4:
        pickle.dump(dij_steps,fh4)

    with open('datafile_bfs_pathlen.txt','wb') as fh5:
        pickle.dump(bfs_path,fh5)

    with open('datafile_dfs_pathlen.txt','wb') as fh6:
        pickle.dump(dfs_path,fh6)

    with open('datafile_rand_pathlen.txt','wb') as fh7:
        pickle.dump(rand_path,fh7)

    with open('datafile_dij_pathlen.txt','wb') as fh8:
        pickle.dump(dij_path,fh8)



    

 
   
    


