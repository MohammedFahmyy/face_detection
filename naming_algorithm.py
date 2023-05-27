import os

f = open("neg.txt",'w')
path = "neg"
Files = os.listdir(path)
for File in Files:
    imgpath = os.path.join(path,File)
    f.write(imgpath+"\n")
f.close()
