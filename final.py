import Extract_Links_From_MGSSTORE as link
import Extract_Contact_From_MSGSTORE as contact
import apply_numbers as apn
import remove_duplicate_and_sort as remdup

print("1.Extract link\n2.Extract contact\n3.Apply numbers\n4.Divide into 100 links of different files\n5.remove duplicate and sort")
a = int(input("Enter your choice : "))
if(a == 1 ):
	link.Main()
elif(a == 2 ):
	contact.Main()
elif(a == 3 ):
	apn.Main()
elif(a == 4 ):
	apn.divi()
elif(a == 5 ):
	remdup.Main()

