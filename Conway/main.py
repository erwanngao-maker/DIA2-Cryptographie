import numpy as np
import time
frame = np.array([[1,1,0,0,0,1,0],
                 [1,1,0,0,1,0,1],
                 [0,0,0,0,0,1,0],
                 [1,1,0,0,0,0,0],
                 [1,1,0,0,0,1,0],
                 [0,0,0,0,0,1,0],
                 [0,0,0,0,0,1,0]])
frame2 = np.array([[0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0],
                 [0,0,0,1,0,0,0],
                 [0,0,0,1,0,0,0],
                 [0,0,0,1,0,0,0],
                 [0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0]])

def compute_number_neighbors(padded_frame, index_line, index_column):
    number_neighbors = sum(padded_frame[x][y] for x in range(index_line, index_line+3) 
                                            for y in range(index_column, index_column+3))
    number_neighbors-=padded_frame[index_line+1][index_column+1]
    return number_neighbors

def compute_next_frame(frame):
    padded_frame=np.pad(frame,1,mode='constant')
    (width, height) = frame.shape
    for x in range(width):
        for y in range(height):
            number_neighbors = compute_number_neighbors(padded_frame,x,y)

            frame[x,y] = 0 if (padded_frame[x+1,y+1] ==0 and number_neighbors !=3) or (padded_frame[x+1][y+1] ==1 and (number_neighbors != 2 and number_neighbors != 3)) else 1
    return frame
while True:
    time.sleep(1)
    print(frame)
    frame = compute_next_frame(frame)