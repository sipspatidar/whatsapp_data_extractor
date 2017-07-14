inputfn = input("enter the file name without extension which you want to divide : ")
with open(inputfn+".txt","r") as file:
	fcount = 0
	emails = "hi"
	while(emails != ""):
		count = 0
		while(count!=100):
			emails = file.readline()
			filename = "whatsapplink"+str(fcount)+".txt"
			with open(filename,"a") as emailfile:
				emailfile.write(str(count)+". "+emails)
				count+=1
		fcount+=1
			