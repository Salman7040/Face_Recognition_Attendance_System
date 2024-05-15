import os, glob
from os import listdir


img_name = []
folder_dir = "./my_image"
for images in os.listdir(folder_dir):
	img_name.append(images.split(".")[:1])





stdName=""
keys = []
values = []
nameAndEmail = {}
inc=0
for x in img_name:
	stdName=stdName.join(x).strip().replace(' ','_')
	keys.append(stdName)
	values.append(f'{stdName.replace("_","")}@gmail.com')
	inc+=1
	if(inc>5):
		break


for i in range(len(keys)):
	nameAndEmail[keys[i]] = values[i]

for k,v in nameAndEmail.items():
	print(f"{k} : {v}")



