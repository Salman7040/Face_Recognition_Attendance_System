import os

dir_name="salmanfile"
curren_dir="C:/Users/DELL/Desktop/face_recognition_Attandence/"

path=os.path.join(curren_dir,dir_name)
os.mkdir(path)
print(path)