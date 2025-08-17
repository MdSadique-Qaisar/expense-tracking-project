import os    #1
import sys   #2
# print("***FILE NAME*** : ", __file__)         #3
# print("FILE NAME : ", os.path.dirname(__file__))     #4

project_root = os.path.join(os.path.dirname(__file__), '..')  #5
print("***Project root*** : ",  project_root)

#6
sys.path.insert(0, project_root)
print(sys.path)