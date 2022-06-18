import os
import sys
from _datetime import datetime as dt
import configparser
import subprocess
import shutil
import json

#function to create a directory
def create_dir():
    try:
        os.mkdir(param1)
        os.mkdir(param2)
    except FileExistsError as fefe:
        print("Exception is Caught:" + str(fefe))


#function to add files in directories
def add_files():
    os.chdir(os.path.join(parent_dir,param1))
    open("first-01.txt","w")
    open("first-02.txt","w")
    open("firfile-1.txt","w")


    os.chdir(os.path.join(parent_dir, param2))
    open("second-01.txt", "w")
    open("second-02.txt", "w")
    open("secfile-1.txt", "w")

    os.chdir(parent_dir)


# function to copy files in directories
def copy_files():
    try:
        os.mkdir("third")
    except:
        pass

    for root,subdirs,files in os.walk(parent_dir):
        if "third" in subdirs:
            for file in files:
                if ".txt" in file:
                         shutil.copy(os.path.join(root,file), "third")




#list files using subprocess
def list_files():
    os.chdir(os.path.join(parent_dir, param1))
    subprocess.run("dir", shell=True)

    os.chdir(os.path.join(parent_dir, param2))
    subprocess.run("dir", shell=True)

    os.chdir(os.path.join(parent_dir, "third"))
    subprocess.run("dir", shell=True)

    os.chdir(parent_dir)



'''
Function to read the properties
'''
def read_properties():
    cfg = configparser.ConfigParser()
    cfg.read("new.properties")
    print(cfg.sections())
    print(cfg.get("main","count"))

def parse_json():
    json_d = {}
    print(json.loads(json_text))




#main

print("*".center(80, "*"))
print("start time: " +  str(dt.now()))
print("*".center(80, "*"))
param1 = sys.argv[1]
param2 = sys.argv[2]


parent_dir = os.getcwd()
create_dir()
add_files()
copy_files()
list_files()
read_properties()


print("*".center(80, "*"))
print("end time: " + str(dt.now()))
print("*".center(80, "*"))

json_text = '{ "id":"02", "name": "Nick", "lastname": "Thameson" }'
parse_json()

print(param1,param2)

