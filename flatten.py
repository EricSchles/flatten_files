import os
import shutil
import argparse
from glob import glob

parser = argparse.ArgumentParser()
parser.add_argument("root")
args = parser.parse_args()

root = args.root


for rootdir,dirs,files in os.walk(root):
    for name in files:
        filename = name
        name = os.path.join(rootdir,name)
        shutil.move(name,root+filename)
    
for rootdir,dirs,files in os.walk(root):
    for name in dirs:
        os.rmdir(os.path.join(root,name))
