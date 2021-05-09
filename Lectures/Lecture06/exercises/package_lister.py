import sys

# take input
# argv - argument values
if len(sys.argv)<2:
    print("Please give the folder name as well!")
    sys.exit()
else:
    folder = sys.argv[1]

def list_all_files(folder_name):
    import os
    out = []
    for root, dir, files in os.walk(folder_name):
        for f in files:
            if f.endswith(".py"):
                out.append(os.path.join(f))

    return out

# open folder and list down all the files
py_files = list_all_files(folder)
print(py_files)

# for each file get the list of all import lines
#   - open files
#   - check if satisfies the import statement rules

# for each import line get the package/module name
#   - separate the line into words and then extract the word which indicates package name
#   - from matplotlib.pyplot import plot
#   - import plot as plt
#   - from lksjfl import sldkf as dsf
