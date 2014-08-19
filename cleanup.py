import os
from datetime import datetime

directory = os.curdir
files = os.listdir(r""+directory)

for file in files:
    if file.endswith(".log"):
        os.remove(file)

        

