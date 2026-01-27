# All about Python scripts for DevOps!

## Dummy Python Scripts to show in Interviews

### 1. Update env files for each environment  
--> Created a Python script which was updating env files and updating some values like urls,ports, servernames etc with given values in the runtime.

### Code Snippet  
_import sys  

def update_value(file_path,key,value):  
  with open(file_path, "r") as file:  
    lines = file.readlines()  
  with open(file_path, "w") as file:  
    for line in lines:  
      if key in line:  
        file.write(key + "=" + value + "\n")  
      else:  
        file.write(line)  

file_path=sys.argv[1]  
key=sys.argv[2]  
value=sys.argv[3]  

update_value(file_path,key,value)_    

