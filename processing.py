import my_code as x
import threading as t
import time


def create_key():
    print("Enter Key, Value and Time-To-Live(optional) for Creating Key")
    arr = input().split(" ")
    if len(arr)==2:
        x.create(arr[0], int(arr[1]))
    else:
        x.create(arr[0], int(arr[1]), int(arr[2]))

def read_key():
    print("Enter Key for Reading")
    arr = input()
    
    l = x.read(arr)
    if l!=None:
        print(l)

def delete_key():
    print("Enter Key for Deleting")
    arr = input()

    x.delete(arr)
    
while True:
    print("Enter a number:\n\t 1 For Creating Key\n\t 2 For Reading Key\n\t 3 For Deleting Key\n\t Other For Exit\n")
    num = input()
    #num = int(num)

    if num == "1":
        t1 = t.Thread(target=create_key)
        t1.start()
        t1.join()
    elif num == "2":
        t2 = t.Thread(target=read_key)
        t2.start()
        t2.join()
    elif num == "3":
        t3 = t.Thread(target=delete_key)
        t3.start()
        t3.join()
    else:
        break
#t1.join()
#t2.join()

