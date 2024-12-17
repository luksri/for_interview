###calc squares and cubes of a list
import time

a_list = [2,3,4,5]

def calc_squares(a_list):
    for i in a_list:
        time.sleep(0.2)
        print(i*i,end=' ')

def calc_cubes(a_list):
    for i in a_list:
        time.sleep(0.2)
        print(i*i*i,end=' ')

t = time.time()
calc_squares(a_list)
calc_cubes(a_list)

print("\ntime taken is: ",time.time()-t)

###calc squares and cubes of a list with threading
import threading

a_list = [2,3,4,5]

def calc_squares1(a_list):
    for i in a_list:
        time.sleep(0.2)
        print("square is: ",i*i)

def calc_cubes1(a_list):
    for i in a_list:
        time.sleep(0.2)
        print("cube is:",i*i*i)

t = time.time()

t1 = threading.Thread(target=calc_squares1, args=(a_list,))
t2 = threading.Thread(target=calc_cubes1, args=(a_list,))

t1.start()
t2.start()

t1.join()
t2.join()

print("\ntime taken is: ",time.time()-t)