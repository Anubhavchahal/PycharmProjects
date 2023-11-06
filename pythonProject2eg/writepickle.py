import pickle
l=[10,20,30,40]
file=open("text.txt","wb")
pickle.dump(l,file)
file.close()

