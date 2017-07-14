#Created_By_Sips_Patidar
#Contact sipspatidar@gmail.com
#For More visit http://www.youtube.com/c/SVSTutorials
#its only for Education Purpose Don't Steal others Number And Don't Misuse it I m not reponsible for any damages
import sqlite3
import time
import os
def translator(str):
	new = ""
	str = str.replace("\n","")
	for i in str:
		if(i.isalnum() or i.isspace()):
			new = new+i;
	return new
def extract_contact_id(g_id,c):
	print("Extracting Contacts....................")
	print("Group Id "+g_id[0])
	c.execute("select jid from group_participants where gjid='"+g_id[0]+"'")
	m_id_list = c.fetchall()
	return m_id_list

def extract_number(m_id_list):
	numbers = []
	for n in m_id_list:
		seperate = n[0].split('@')
		if(str(seperate[0]).isdigit()):
			numbers.append(seperate[0])
	return numbers

	
def make_file(name):
	print("Creating file..............")
	if(name!=""):
		fo = open(name+".vcf","w")
	else:
		fo = open(str(time.time())+".vcf","w")
	return fo	
	
def write_into_file(fo,numbers,name):		
	print("Writting to file...................")
	fo.write("BEGIN:VCARD\n")
	fo.write("VERSION:3.0\n")
	try:
		fo.write("N:"+name+"\n")
		fo.write("FN:"+name+"\n")
	except:
		print("Error: can\'t Write Conatct Name \n Write Another name")
		fo.write("N:alternate\n")
		fo.write("FN:alternate\n")
	
	for n in numbers:
		fo.write("TEL;CELL:+"+n)
		fo.write("\n")
	fo.write("END:VCARD");
	fo.close()
	print("Contact File is Created Successfully")
	
def Main():
	aa = input("enter database name : ")
	conn = sqlite3.connect(aa)
	print("Making Connection............")
	c = conn.cursor()
	print("Successfully Connected....")
	c.execute("select key_remote_jid,subject from chat_list")
	g_list = c.fetchall()
	i=0
	try:
		os.mkdir("contacts")
	finally:
		os.chdir("contacts")
	for g_id in g_list:
		m_id_list = extract_contact_id(g_id,c)
		numbers = extract_number(m_id_list)
		numbers.sort()	
		name = translator(str(g_id[1]))
		fo = make_file(name)
		write_into_file(fo,numbers,name)
		i=i+1
		print("File Created : "+str(i)+"\n\n")
		time.sleep(1)
		
#if __name__=='__main__':
#	Main()
#Stay_Connected :p :) 	