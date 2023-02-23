import matplotlib.pyplot as plt
import pickle

pickle_off_1 = open ("datafile_dfs_pathlen.txt", "rb")
emp_1 = pickle.load(pickle_off_1)

pickle_off_2 = open ("datafile_cov.txt", "rb")
emp_2 = pickle.load(pickle_off_2)

pickle_off_3 = open ("datafile_bfs_pathlen.txt", "rb")
emp_3 = pickle.load(pickle_off_3)

pickle_off_4 = open ("datafile_rand_pathlen.txt", "rb")
emp_4 = pickle.load(pickle_off_4)

pickle_off_5 = open ("datafile_dij_pathlen.txt", "rb")
emp_5 = pickle.load(pickle_off_5)


plt.plot(emp_2, emp_1, color='r', label='dfs')
plt.plot(emp_2, emp_3, color='g', label='bfs')
plt.plot(emp_2, emp_4, color='b', label='random')
plt.plot(emp_2, emp_5, color='y', label='dijkstra')
leg = plt.legend(loc='upper right')



# naming the x axis
plt.xlabel('Coverage Percentage')
# naming the y axis
plt.ylabel('Path Length')
# giving a title to my graph
plt.title('Motion Planning Algorithms')
# function to show the plot
plt.show()


