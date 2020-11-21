import os
import time

os.path.exists("basics.py")

# If you are step over the directory of this file, the output would be True, meaning that the file is on the current directory.

while os.path.exists("basics.py"):
    with open("basics.py") as myfile:
        content = myfile.read()
    print(content)
    time.sleep(2)