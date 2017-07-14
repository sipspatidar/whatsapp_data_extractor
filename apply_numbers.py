import os
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
	i = 0
	for w in result:
		i +=1
		print(str(i)+". "+w)
		poa.write(str(i)+". "+w)
def divi():
	os.chdir("links")
	inputfn = input("enter the file name without extension which you want to divide : ")
	with open(inputfn+".txt","r") as file:
		fcount = 0
		emails = "hi"
		try:
			os.mkdir("divided_links")
		finally:
			os.chdir("divided_links")
		while(emails != ""):
			count = 0
			while(count!=100):
				emails = file.readline()
				filename = "whatsapplink"+str(fcount)+".txt"
				with open(filename,"a") as emailfile:
					emailfile.write(str(count)+". "+emails)
					count+=1
			fcount+=1
				
