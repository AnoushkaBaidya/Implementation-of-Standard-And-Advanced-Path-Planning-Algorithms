from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
import numpy as np
import random

''' CREATES OBSTACLE GRID OF VARYING COVERAGE DENSITY '''
#Set up variables for the obstacle grid
OBS_COL = (0,0,0) #Black for obstacles 
BGR_COL = (255,255,255) #White color for background display
obs_shape=(4,2)


def current_coverage(image: Image)-> float:
    #finding out the current coverage 
    T= 128*128
    obs_pixel=0

    for pixel in image.getdata():
        if pixel == (0,0,0):
            obs_pixel+=1

    #coverage is in percent so obs_pixel/T
    ans= (obs_pixel/(128*128))
    #print("pixels")
    #print(obs_pixel)
    return ans


def occupied_cell(image: Image, x: int , y : int ):
    #Check if the random position is occupied or not 
    #considering that we put object from left most corner as (x,y)
    #check for neighbouring cells
    for i in range(x,x+2,1):
      for j in range(y,y+4,1):
        cord = j,i
        if(image.getpixel(cord)) == 1:
                return True

    # if the space is empty for the obstacle
    return False



def tetrominoes_in_image (coverage :int):

    #create grid then place teros
    grid = np.zeros((128, 128))

    tetrominoes= np.array([[[1,1], [1,1], [1,1], [1,1]],
            [[1,0], [1,0], [1,0], [1,1]],
            [[1,0], [1,0], [1,1], [0,1]],
            [[0,1], [0,1], [1,1], [0,1]]])

    #creates image from numpy array 
    #grid_img = Image.fromarray(np.uint8(grid * 255),mode='L')
    grid_img=  Image.new("RGB", (128,128), color=(255, 255, 255))
    
    #choosing random x and y position to place on grid 
    cov_required=coverage
    des_cov = cov_required/100
    cur_cov=0
    

    while cur_cov < des_cov:
        #random x and y from the grid 
        x= random.randint(1,124)
        y= random.randint(1,124)
        #choosing a random shape
        random_idx= np.random.randint(0, 3)
        tet_rand= tetrominoes[random_idx]
        #print(tet_rand)
        #check if the cell for obstacle placement is occupied or not 
        #is_occupied = occupied_cell(grid_img, x, y)
        is_occupied = 0

        if is_occupied == 0:
            #place the obstacle here 
            for i in range(4):
                for j in range(2):
                    if tet_rand[i][j]==1:
                        #make pixel =1 
                        cordinates=x+j,y+i
                        grid_img.putpixel(cordinates,OBS_COL)
        
        cur_cov = current_coverage(grid_img)
        #print("curr cov")
        #print(cur_cov)

    print("Final Coverage of the grid ")    
    print(current_coverage(grid_img))
   

    #plots the final plot that we see 
    plt.imshow(grid_img)
    return grid_img


#val=input(" Enter percentage coverage-> Ex: 10 percent then enter 10: ")
#tetrominoes_in_image(int(val))



