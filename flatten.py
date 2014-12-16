import os
import shutil
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("root")
args = parser.parse_args()

root = args.root[0]
root_dir = os.path.abspath(root)

def move_files(root,root_dir):
    for rootdir,dir,files in os.walk(root):
        for file in files:
            filename = file
            file = os.path.join(rootdir,file)
            shutil.move(file,root_dir+filename)
    

