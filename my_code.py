import threading 
from threading import*
import time

dictionary = {}

# Create function
def create(key, value, timetolive = 0):
    if key in dictionary:
        print("Error: Entered key already exist")
    else:
        if key.isalpha():
            temp = 1024*1024
            if len(dictionary)<1024*temp and value<=16*temp:
                if timetolive==0:
                    my_list = [value, timetolive]
                else:
                    my_list = [value, time.time()+timetolive]

                if len(key)<=32:
                    dictionary[key] = my_list
                else:
                    print("key length should be less than or equal to 32 characters")
            else:
                print("Error: Memory Limit Exceeded")
        else:
            print("Error: Please enter valid key name!!! It must contain alphabets only")

# read function
def read(key):
    if key not in dictionary.keys():
        print("Error: entered key doesn't exist in database")
    else:
        arr = dictionary[key]

        if arr[1]==0:
            return str(key)+" : "+str(arr[0])
        else:
            if time.time()<arr[1]:
                return str(key)+" : "+str(arr[0])
            else:
                print("Error: Time-to-Live is expired for", key)            


# delete function
def delete(key):
    if key not in dictionary.keys():
        print("Error: entered key doesn't exist in database!! Enter valid key")
    else:
        arr = dictionary[key]

        if arr[1]==0:
            del dictionary[key]
            print("Key", key, " deleted successfully!!")
        else:
            if time.time()<arr[1]:
                del dictionary[key]
                print("Key", key, "deleted successfully!!")
            else:
                print("Error: Time-to-Live is expired for", key)
