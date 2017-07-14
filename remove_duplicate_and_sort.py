import os

def list_Remove_Duplicates(x):
	return sorted(set(x))

def Main():
	os.chdir("links")
	inputfn = input("enter the file name without extension : ")
	po = open(inputfn+".txt","r")
	line = "esf"
	link = []
	while(line!=""):
		line = po.readline()
		link.append(line)
	result = sorted(set(link))

	poa = open("new_"+inputfn+".txt",'w')
	print("writing into file")
	for w in result:
		print(w)
		poa.write(w)
