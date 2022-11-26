import os
import shutil

from_dir="C:/Users/INTEL/Desktop/test"
to_dir="C:/Users/INTEL/Desktop/python"

list_of_dir = os.listdir(from_dir)

for trushna in list_of_dir:
    name,ext=os.path.splitext(trushna)
    if ext=="":
        continue
    if ext in [".pdf",".doc",".text"]:
        path1=from_dir+'/'+trushna
        path2=to_dir+'/'+"pdf_file"
        path3=to_dir+'/'+"pdf_file"+'/'+trushna
        if os.path.exists(path2):
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            shutil.move(path1,path3)